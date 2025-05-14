list_for_loops = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

print("list that we will be looping over\n", list_for_loops)
print("regular for x in var loop\n")

for item in list_for_loops:
    print(item)

print("\nnow using range")
for item in range(0,6):
    print(list_for_loops[item])