from models import Product

def generate_response(message):
    keywords = message.lower().split()
    results = Product.query.all()

    filtered = []
    for kw in keywords:
        for p in results:
            if kw in p.name.lower() or kw in p.category.lower():
                filtered.append(p)

    if not filtered:
        return "Sorry, I couldn’t find anything matching your request."

    reply = "Here are some matching products:\n"
    for p in filtered[:3]:
        reply += f"- {p.name} ({p.category}) - ₹{p.price}\n"

    return reply
