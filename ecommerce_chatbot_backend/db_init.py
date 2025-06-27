from app import app, db
from models import Product, User
from faker import Faker
import random

fake = Faker()

categories = ['Mobiles', 'Laptops', 'Books', 'Textiles']
images = {
    'Mobiles': [
        'https://m.media-amazon.com/images/I/71yzJoE7WlL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/81+N4PFF7jL._SX679_.jpg'
    ],
    'Laptops': [
        'https://m.media-amazon.com/images/I/71D5fMDvqDL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/71TPda7cwUL._SX679_.jpg'
    ],
    'Books': [
        'https://m.media-amazon.com/images/I/81dQwQlmAXL.jpg',
        'https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg'
    ],
    'Textiles': [
        'https://m.media-amazon.com/images/I/81nCaaYjOeL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/91vwQwWq5pL._SX679_.jpg'
    ]
}

with app.app_context():
    db.drop_all()
    db.create_all()

    laptops = [
        "HP Pavilion Laptop", "Dell Inspiron Laptop", "Lenovo IdeaPad Slim",
        "Asus VivoBook 15", "Acer Aspire 7", "MacBook Air M1", "MacBook Pro M2"
    ]
    for name in laptops:
        db.session.add(Product(
            name=name,
            category="Laptops",
            price=round(random.uniform(40000, 120000), 2),
            description=fake.sentence(nb_words=12),
            image_url=random.choice(images["Laptops"])
        ))

    # 🔹 Add realistic mobiles
    mobiles = [
        "iPhone 14", "Samsung Galaxy S23", "OnePlus 11R", "Redmi Note 12", "Vivo V27", "Realme Narzo 60"
    ]
    for name in mobiles:
        db.session.add(Product(
            name=name,
            category="Mobiles",
            price=round(random.uniform(12000, 90000), 2),
            description=fake.sentence(nb_words=10),
            image_url=random.choice(images["Mobiles"])
        ))

    # 🔹 Add realistic books
    books = [
        "Atomic Habits", "The Alchemist", "Deep Work", "Think and Grow Rich",
        "Ikigai", "The Psychology of Money"
    ]
    for name in books:
        db.session.add(Product(
            name=name,
            category="Books",
            price=round(random.uniform(200, 1000), 2),
            description=fake.text(max_nb_chars=100),
            image_url=random.choice(images["Books"])
        ))

    # 🔹 Add realistic textiles
    textiles = [
        "Cotton Kurta", "Printed Saree", "Denim Jeans", "Hooded Sweatshirt",
        "Linen Shirt", "Traditional Sherwani"
    ]
    for name in textiles:
        db.session.add(Product(
            name=name,
            category="Textiles",
            price=round(random.uniform(500, 5000), 2),
            description=fake.text(max_nb_chars=80),
            image_url=random.choice(images["Textiles"])
        ))

    # 🔹 Add 100+ randomized mock products
    for _ in range(100):
        category = random.choice(categories)
        db.session.add(Product(
            name=f"{fake.company()} {category[:-1]}",
            category=category,
            price=round(random.uniform(500, 95000), 2),
            description=fake.sentence(nb_words=15),
            image_url=random.choice(images[category])
        ))

    # 🔹 Add test user
    db.session.add(User(username='testuser', password='1234'))

    db.session.commit()
    print("Database seeded with 120+ realistic and randomized mock products.")
