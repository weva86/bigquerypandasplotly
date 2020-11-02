sequences = [10, 345, 2, 1, 43, 2, 5, 2, 1, 7, 3, 25, 7, 4]

#for element in sequences:
 #   if element > 4:
  #      print(element)

def my_filter(element):
    return element > 4
filter_result = filter(my_filter, sequences)
print(filter_result)