
PRICE = 50
total_inserted = 0
VALID_COINS = [25, 10, 5]

while total_inserted < PRICE:
    try:
        coin = int(input("Coin Insert: "))
    except ValueError:
        continue

    if coin in VALID_COINS:
        total_inserted += coin

    if total_inserted < PRICE:
        print(f"Amount Due: {PRICE - total_inserted}")
    else:
        break

change = total_inserted - PRICE
print(f"Change Owed: {change}")
