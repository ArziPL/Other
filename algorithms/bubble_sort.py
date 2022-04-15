# Take every value one by one and check which of two is greater,
# if one behind, then change places between them, repeat until sorted

to_sort = [52,63,12,6,631,6,24,637,64,421,74,124,0,-5,523,-10,-529]

def bubble_sort(arr:list): # O(n^2)
    n = len(arr)
    for i in range(0,n-1):
        for j in range(1, n):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

bubble_sort(to_sort)
print(to_sort)
            