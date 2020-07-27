# Remove Element
# Given a list of numbers and a value as input to a function, remove all instances of that value "in-place" and return the new length of the list
# Input: nums = [3,2,2,3] value = 3
# Output: return a length == 2

def remove_elem(l_1,v):
    for num in l_1:
        if num == v:
            l_1.remove(v)
    print(len(l_1))

def remove_elem2(l_1,v):
    l_1 = [num for num in l_1 if num != v]
    print(len(l_1))

remove_elem([3,2,2,3],3) # 2
remove_elem2([3,2,2,3],3) # 2