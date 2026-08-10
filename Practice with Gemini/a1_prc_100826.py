def print_receipt(items, prices, quantities):
    #items = ["Oil", "Philter", "Candle"]
    #prices = [1200, 350, 500]
    #quantities = [2, 1, 4]
    if len(items) == 0:
        print("Look No items!")
        return 0
    #else:

    total_sum = 0

    for i,q in enumerate(items):
        print(f"{i+1}. Item {q} x{quantities[i]}:  | Price: {prices[i] * quantities[i]} UAH")
        total_sum += prices[i] * quantities[i]

    to_pay = total_sum

    if total_sum > 3000:
        discount = total_sum * 0.10
        to_pay = total_sum - discount # some difficult #final_total

        print(f"Total: {total_sum} UAH" )
        print(f"Discount(10%): -{discount} UAH")
        print(f"Final total: {to_pay} UAH") #final_total
    else:
        print(f"Total: {total_sum} UAH")
 #sum(prices)
    print("Total items:", sum(quantities), "pcs" )

    return to_pay #v2total_sum #v1 final_total not fined

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
print_receipt(my_items3, my_prices3, my_quantities3)

r1 = print_receipt(my_items, my_prices, my_quantities)
r2 = print_receipt(my_items2, my_prices2, my_quantities2)
r3 = print_receipt(my_items3, my_prices3, my_quantities3)
r4 = print_receipt(["sword", "shield"], [2500, 1800], [1,1])

daily_total = r1 + r2 + r3 + r4
print("_______________________________")
print(f"Total revenue: {daily_total} UAH") #revenue дохід
