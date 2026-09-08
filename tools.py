# f string
# user_name = "Gunhilda"
# user_age = 17
# user_info = f"{user_name} is {user_age} years old"
# print(user_info)

# single line if
# user_status = "adult" if user_age >= 18 else "child"
# print(user_status)

# user_info = f"{user_name} is a {"adult" if user_age >= 18 else "child"}."
# print(user_info)

# list comprehension
# simple_list = [f'{j}{i}' for i in range(0, 11, 2) for j in ('a', 'b', 'c') if j == 'a']
# for i in range(0, 10, 1):
#   simple_list.append(i+1)
# print(simple_list)

# lambda functions
# def double_val(num: int) -> int: return num*2

# double_val = lambda num: num*2
# print(double_val())

# function as an arg
# random_list = [('anna', 25), ('paul', 40), ('lisa', 10)]
# sorted_list = sorted(random_list, key=lambda user_tuple: user_tuple[1])
# print(sorted_list)

board = [f'{x.upper()}{y}' for y in range(1, 6) for x in ['a','b','c','d','e'] if f'{x}{y}' != 'c3']
print(board)