#WAP to read two set from users and perform set union, intersection and set difference operation and display results.
set1=set(input("Enter the elements of set1 (comma separated):").split(","))
set2=set(input("Enter the elements of set2 (comma separated):").split(","))
print(f"the set operations between set1={set1} and set2={set2} are:")
print(f"Union:",set2.union(set1))
print(f"Difference(set1-set2):",set1.difference(set2))
print(f"Difference(set2-set1):",set2.difference(set1))
print(f"Intersection:",set1.intersection(set2))
print(f"")