items = ["Oil", "Philter", "Candle"]
prices = [1200, 350, 500]
quantities = [2, 1, 4]
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
