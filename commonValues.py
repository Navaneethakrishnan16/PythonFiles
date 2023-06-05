tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
common_values=[ element
for element in tuple1
 for element2 in tuple2
  if element == element2]
print("Common values:", common_values)
