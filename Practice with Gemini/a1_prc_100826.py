def print_receipt(items, prices, quantities):
    #items = ["Oil", "Philter", "Candle"]
    #prices = [1200, 350, 500]
    #quantities = [2, 1, 4]
    total_sum = 0

    for i,q in enumerate(items):
        print(f"{i+1}. Item {q} x{quantities[i]}:  | Price: {prices[i] * quantities[i]} UAH")
        total_sum += prices[i] * quantities[i]

    if total_sum > 3000:
        discount = total_sum * 0.10
        final_total = total_sum - discount # some difficult

        print(f"Total: {total_sum} UAH" )
        print(f"Discount(10%): -{discount} UAH")
        print(f"Final total: {final_total} UAH")
    else:
        print(f"Total: {total_sum} UAH")
 #sum(prices)
    print("Total items:", sum(quantities), "pcs" )

my_items = ["Oil", "Philter", "Candle"]
my_prices = [1200, 350, 500]
my_quantities = [2, 1, 4]

my_items2 = ["pencil", "book", "notebook"]
my_prices2 = [12, 500, 45]
my_quantities2 = [4, 1, 4]

my_items3 = []
my_prices3 = []
my_quantities3 = []

print_receipt(my_items, my_prices, my_quantities)
print_receipt(my_items2, my_prices2, my_quantities2)
print_receipt(["sword", "shield"], [2500, 1800], [1,1])

