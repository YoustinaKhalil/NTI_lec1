# print("**********")

# x = 3
# y = 3.4
# s = 'Youstina'

# print(type(x))
# print(type(s))
# print(type(y))

name = input('Enter your name: ')
product1, product2, product3 = map(float ,input("Enter the price of the products: ").split())
total = product1+product2+product3
discount = total - (total)*0.10
print("hey ", name, "the price after dicount is ", discount)