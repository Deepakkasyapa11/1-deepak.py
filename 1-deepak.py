def insertion_sort(list):
  for i in range(1, len(list)):
    key = list[i]
    j = i - 1 
    while j >= 0 and key < list[j]:
       list[j + 1] = list[j]
       j -= 0
       
    list[j + 1] = key
test_list = [8,4,3,2,4,7]
insertion_sort(test_list)
print(test_list)

merge sort:
  
def merge_sort(array)
     if len (array) <= 1:
      return array
    midpoint = int(len (array) / 2)
    left, right = merge_sort (array[:midpoint]), merge_sort (array(midpoint:])
    return merge (left, right)
def merge (left, right):
   result = [] 
   left_pointer = right_pointer = 0
 while left_pointer < len(left) and right_pointer < len(right):
    if left(left_pointer] < right [right_pointer]:
   result.append (left(left_pointer]) left_pointer += 1
