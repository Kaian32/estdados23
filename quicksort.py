#made by Kaian Vinicius
#hard to learn how it works, thanks gringos

def quicksort(arr,left,right): #using an array and two indexes (left and right) that define the part of the array that will be sorted, default index is the whole array (left = 0, right = array size)
    if left < right: #check if there's at least 2 elements
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1) #calls all elements to the left of the pivot (except the pivot ofc)
        quicksort(arr, partition_pos + 1, right) #calls all elements to the right of the pivot (except the pivot ofc)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right] #pivot always will be the last element of the selection

    while i < j:
        while i < right and arr[i] < pivot: #while i is not at the end of the array and its less than pivot
            i += 1 #i moves to the right of the selection until end or pivot
        while j > left and arr[j] >= pivot: #while j is greater than left and its more than pivot
            j -= 1 #j moves to the left of the selection until end or pivot
        
        if i < j: #check if elements crossed
            arr[i], arr[j] = arr[j], arr[i] #if not, swap
    
    if arr[i] > pivot: #after elements crossed, i is greater than pivot
        arr[i], arr[right] = arr[right], arr[i] #swap array indexes bc the pivot is arr[right] and it needs a new value to continue

    return i #quick sort needs i to split array for next quicksort

arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)
print(arr)