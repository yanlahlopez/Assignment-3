import math

def aprice():
  apple = int(input("How many apples do you want? "))
  return apple
  
def oprice():  
  orange = int(input("How many oranges do you want? "))
  return orange

appleprice = 20 * aprice()
orangeprice = 25 * oprice()

def aototal():
  total = appleprice + orangeprice
  return total

print(f"The total amount is {aototal()}")
