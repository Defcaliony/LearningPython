items = ["Oil", "Philter", "Candle"]
prices = [1200, 350, 500]

for i, q in enumerate(items):   # i == index; q == item(s)
    print(f"{i+1}. Item {q}:  | Price: {prices[i]} hrn")

print("Total: ", sum(prices), "HRN")
