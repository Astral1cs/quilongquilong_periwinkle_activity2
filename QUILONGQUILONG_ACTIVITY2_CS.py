


my_list = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]


print("Original List:  ", end="")
for item in my_list:
    print(item, end=", ")
print()


update_index = int(input("Input Index to Update: "))
new_value = input("Input New Value: ")
slice_start = int(input("Enter Slice Range 1: "))
slice_end = int(input("Enter Slice Range 2: "))
search_item = input("Enter Search Item: ")


print(f"Index to Update: {update_index}")
print(f"New Value: {new_value}")


sliced_list = my_list[slice_start:slice_end]
print(f"Sliced List: ({slice_start}:{slice_end}) ", end="")
for item in sliced_list:
    print(item, end=", ")
print()


found = False
for item in sliced_list:
    if item == search_item:
        found = True
        break

if found:
    print(f"Search Result:  {search_item} is found in the sliced list")
else:
    print(f"Search Result:  {search_item} is not found in the sliced list")


my_list[update_index] = new_value


print("Updated List:  ", end="")
for item in my_list:
    print(item, end=", ")
print()