items = ["Oil", "Philter", "Candle"]
prices = [1200, 350, 500]
quantities = [2, 1, 4]
total_sum = 0

for i,q in enumerate(items):
    print(f"{i+1}. Item {q} x{quantities[i]}:  | Price: {prices[i] * quantities[i]} UAH")
    total_sum += prices[i] * quantities[i]



print("Total: ",total_sum) #sum(prices)
