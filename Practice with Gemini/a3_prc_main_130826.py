#product = { "name": "Oil", "price": 1200, "quantity": 4 }
#print(product["name"])

#book = {"title": "My Book", "Price": 600, "quantity": 3}
#print(f"Book Title: {book['title']} | {book['quantity']} pcs |Total: {book['Price'] *book['quantity']} UAH")
import json

cart = [{"title": "Atomic Habits", "price": 450, "quantity": 2},
        {"title": "Noise", "price": 500, "quantity": 1},
        {"title": "Competitive Advantage", "price": 600, "quantity": 2}
]

def print_receipt(cart):
    if not cart:
        print("Cart is empty")
        return 0

    total_sum = 0

    for item in cart:
        item_total = item["price"] * item["quantity"]
    #or: item_total = item["price"] * item["quantity"]
    #    total_sum = total_sum + item_total
        print(f" Book titel: {item['title']}  {item['quantity']} pcs, Total price: {item['price']*item['quantity']} UAH")

        total_sum += item_total


    print("____________________________________")
    print(f"Total revenue: {total_sum} UAH")

    return total_sum

receipt1 = print_receipt(cart) #review for 1st box

print("\n--- 2rd check (empty) ---")
receipt2 = print_receipt([]) #review for empty box

print("___________________________________________")
print(f"Total revenue: {receipt1 + receipt2} UAH")






