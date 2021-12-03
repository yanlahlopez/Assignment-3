def total(cash, apple):
  return cash // apple

def change(cash, apple):
  return cash % apple

money = float(input("Amount of money you have: "))
aprice = float(input("Price of apple: "))

print(f"You can buy {total(money,aprice)} apples and your change is {change(money,aprice):.2f} pesos.")
