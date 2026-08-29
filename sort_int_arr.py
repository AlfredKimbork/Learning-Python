int_arr = [90, 89, 11, 32, 121]
for i in range(len(int_arr)):
  for j in range(i+1, len(int_arr)):
    if(int_arr[i] > int_arr[j]):
      temp = int_arr[i]
      int_arr[i] = int_arr[j]
      int_arr[j] = temp
print(int_arr)