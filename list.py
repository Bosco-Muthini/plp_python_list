my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)

my_list.insert(1,15)
print(my_list)

new_list = [10, 20, 30, 40]
my_list.extend(new_list)
print(my_list)

my_list.pop()
# del my_list(-8)
print(my_list)

my_list.sort()
print(my_list)

print (30 in my_list)

index_30 = my_list.index(30)
print("Index of value 30:", index_30)
