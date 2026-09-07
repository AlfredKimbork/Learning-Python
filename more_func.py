# def print_x_times(message: str, times: int = 3):
#   for i in range(times):
#     print(message, i+1, "out of", times)  

#   return times

# print_x_times("hello world!")
# print_x_times("another message", 1)
# return_val = print_x_times("a third message", 9)

# print(return_val)

# def hypotenuse_calc(a: int = 1, b: int = 1) -> float:
#   return round((a ** 2 + b ** 2) ** .5, 2)

# print(hypotenuse_calc(3, 4))

def shout(message: str = "hello world!", reps: int = 1) -> str:
  if reps <= 10:
    for _ in range(reps):
      print(message.upper())
  else:
    print("that's too much my guy...")
    
  return "done"

print(shout("wassup", 5))