calculate_discount(price, discount_percent):
    Calculate the final price after applying a discount if it is 20% or higher:
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    return price
price = float(input("200:"))
discount_percent = float(input("25%:"))

final_price = calculate_discount(price, discount_percent)
print(final price)
