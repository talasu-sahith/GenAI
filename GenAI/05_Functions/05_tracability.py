# we see how to use loops and functions for calculating the VAT for prices

def vat_Rate(price , rate):
    return price + price*(rate/100)

prices = [100,150,200]

for price in prices:
    print(f"order amount is {price} : final amount - ",vat_Rate(price , 10))