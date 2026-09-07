# num = 4

# if num < 4:
#   print('less than 4')
# elif num == 4 or num < 4 and num > 4: # && = and, || = or
#   print('it\'s the same as 4')
# else:
#   print('more than 4')

# counter = 0
# while counter <= 10:
#   if counter == 5:
#     print("counter is 5")
#   else:
#     print(counter)
#   counter += 1
# print("while loop finished")

# test_list = [1,2,13,4,5,6,7,8]
# for x in range(len(test_list)):
#   for y in range(x+1, len(test_list)):
#     print(x, y)
# for x in test_list:
#   print(x)

# test_dict = {1:2,3:4,5:6}
# values, keys, items
# for key, val in test_dict.items():
#   print(key, val)

# any and all
# if any([1,1,1,0,1,1]):
#   print("truthy")
# else:
#   print("falsy")

exercise = [1,2,3,4,5]
for val in exercise:
  if val == 2:
    print('the value is 2')
  else:
    print('the value is not 2')
for i in range(5):
  print('last item')