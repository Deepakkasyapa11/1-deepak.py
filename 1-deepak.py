def insertion_sort(list):
  for i in range(1, len(list)):
    key = list[i]
    j - i - 1 
    while j >= 0 and key < list[j]:
       list[j + 1] = list[j]
       j -= 1
       
    list[j + 1] = key
test_list = [8,4,3,2,4,7]
insertion_sort(test_list)
print(test_list)
