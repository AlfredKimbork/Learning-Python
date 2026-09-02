# tuple = (int, 'string', (tuple)) immutable
# list = [int, 'string', (tuple)] mutable
# set = {int, 'string', (tuple)} unique entries
# dict = {'key':'string', 'key':int, 'key':(tuple)} key-value

a_tuple = (1,2,3,'string')
# print(a_tuple)
a_list = [1,2,3,'string',2]
# print(a_list)
# print(len(a_list))
# print(a_list)
# a_list.append('another string')
# print(a_list)
a_set = {1,2,3,'string'}
# print(a_set)
# a_set.add('another string')
# print(a_set)

# print(list(set(a_list)))

a_dict = {
  'a': 'uga buga',
  'b': 2,
  'c': 3,
  'd': 3,
}

names = ['lisa','bob','alex','anna','john']
# print(names[1]) # get index
# print(names[1:4]) # get index to index (don't include)
# print(names[1:4:2]) # get index to index (don't include) every x

# print(a_dict['a'])
# print(a_dict)
# a_dict['new key'] = 'hello world'
# print(a_dict)


numbers = [1,2,3,4,5,6,7,8,9,10,]
print(numbers)
sliced_numbers = numbers[7::-2]
print(sliced_numbers)



