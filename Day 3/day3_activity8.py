TAX_RATE = 0.08

sample_price1 = [x for x in range(1, 200)]
sample_prices2 = [x*2 for x in range(1, 500)]
sample_prices3 = [x for x in range(1, 1500) if x % 2 == 0]

def calculate_total(price_list: list[int | float]) -> float:
    prices_list_with_tax: list[int | float] = []
    subtotal = 0
    subtax = 0

    for price in price_list:
        subtotal += price
        price_with_tax = price * TAX_RATE
        prices_list_with_tax.append(price_with_tax)

    for price in prices_list_with_tax:
        subtax += price

    return f"Prices are {price_list} total price is {subtotal}\nPrices with 8% tax {prices_list_with_tax} total price is {subtax}"


print(calculate_total(sample_price1))
print(calculate_total(sample_prices2))
print(calculate_total(sample_prices3))