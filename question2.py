def count(input1):
    count_dict = {}
    for char in input1:
        count_dict[char] = count_dict.get(char, 0) + 1 
    return count_dict
input1= ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print (count(input1))


def group_by_key(input2):
    group_dict = {}
    for dic in input2:
        group_dict[dic["key"]] = group_dict.get(dic["key"], 0) + dic["value"]
    return group_dict

input2 = [ 
{'key': 'a', 'value': 3}, 
{'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5} 
] 
print(group_by_key(input2))