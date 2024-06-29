#write a function that accepts a dictionary a dictionary as an argument . if the dictionary contains duplicate values. it should return and empty dictionary . otherwise it should return a new dictionary where the values become the keys and keys become values:
def keyvalue(input_dict):
  
    seen_values = []
    for v in input_dict.values():
        if v in seen_values:
            return {} 
        seen_values.append(v)
    output_dict = {v: k for k, v in input_dict.items()}
    return output_dict
example_dict = {"a": 1, "b": 1, "c": 3}
result = keyvalue(example_dict)
print("Result:", result)