#Display the list.items in reverse order and ascending oreder

my_list = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_list = sorted(my_list)
reverse_sorted_list = sorted_list[::-1]
print("Original List:", my_list)
print("Sorted List (Ascending Order):", sorted(my_list))
print("Sorted List (Descending Order):", sorted(my_list , reverse = True))
