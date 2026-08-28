# string = "hello world"
# string_upper = "HELLO WORLD"
# integer_low = 5
# integer_high = 50
# integer_neg = -5

# print(string.upper())
# print(string_upper.lower())
# print(string.replace("o", "O"))
# print(abs(integer_neg))
# print(max(integer_low, integer_high))
# print(min(integer_low, integer_high))
# print(len(string))

a = int(input("side a :: "))
b = int(input("side b :: "))

print(round((a ** 2 + pow(b, 2)) ** .5, 2))