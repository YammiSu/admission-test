count(arr):
    count_dict = {}
    for char in arr:
        count_dict[char] = count_dict.get(char, 0) 
    return count_dict
arr= ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print (count(arr))