from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Product, User, ChatLog
from chatbot_logic import generate_response
from sqlalchemy import or_

app = Flask(__name__)
CORS(app)

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'chatbot.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return {"message": "E-commerce Chatbot Backend Running"}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and user.password == data.get('password'):
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message', "").lower()

    response_text = "Sorry, I didn't understand that."
    products = []

    # 🔍 Extract category
    category_map = {
        "laptop": "Laptops",
        "mobile": "Mobiles",
        "book": "Books",
        "textile": "Textiles"
    }

    detected_category = next((cat for key, cat in category_map.items() if key in message), None)

    # 🔍 Extract brand (optional simple match)
    brands = ["hp", "dell", "lenovo", "asus", "macbook", "acer", "iphone", "samsung", "oneplus", "redmi", "realme", "vivo"]
    detected_brand = next((brand for brand in brands if brand in message), None)

    # 🔍 Check if sorting requested
    sort_by_price = "sort" in message and "price" in message

    # 🔍 Basic pagination simulation: page=1 always (can extend later)
    page = 1
    page_size = 3
    offset = (page - 1) * page_size

    # 🔍 Build query
    if detected_category:
        query = Product.query.filter(Product.category == detected_category)

        if detected_brand:
            query = query.filter(Product.name.ilike(f"%{detected_brand}%"))

        if sort_by_price:
            query = query.order_by(Product.price.asc())

        products = query.offset(offset).limit(page_size).all()

        response_text = f"Here are some {detected_brand + ' ' if detected_brand else ''}{detected_category.lower()} for you:"
    else:
        response_text = "Please specify a product category like 'laptop', 'mobile', 'book', or 'textile'."

    return jsonify({
        "response": response_text,
        "products": [
            {
                "name": p.name,
                "description": p.description,
                "price": p.price,
                "image": p.image_url or "https://via.placeholder.com/150"
            } for p in products
        ]
    })

@app.route('/products', methods=['GET'])
def search_products():
    keyword = request.args.get('q', '')
    products = Product.query.filter(
    or_(
        Product.name.ilike(f'%{keyword}%'),
        Product.category.ilike(f'%{keyword}%')
    )
    ).all()
    return jsonify([p.serialize() for p in products])

if __name__ == '__main__':
    app.run(debug=True)
