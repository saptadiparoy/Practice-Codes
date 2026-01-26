phones = [
    {"name": "Samsung A34", "brand": "Samsung", "price": 20000, "features": ["camera", "battery"]},
    {"name": "iPhone SE", "brand": "Apple", "price": 40000, "features": ["camera"]},
    {"name": "Redmi Note 12", "brand": "Xiaomi", "price": 15000, "features": ["battery", "gaming"]},
    {"name": "Realme Narzo", "brand": "Realme", "price": 18000, "features": ["gaming", "battery"]}
]

print("Welcome to Mobile Recommendation System")

budget = int(input("Enter your budget: "))
brand = input("Preferred brand (or 'any'): ").lower()
feature = input("Required feature (camera/battery/gaming): ").lower()

recommendations = []

for phone in phones:
    if phone["price"] <= budget:
        if brand == "any" or phone["brand"].lower() == brand:
            if feature in phone["features"]:
                recommendations.append(phone["name"])

if recommendations:
    print("Recommended phones for you:")
    for r in recommendations:
        print("-", r)
else:
    print("No phones match your requirements.")
