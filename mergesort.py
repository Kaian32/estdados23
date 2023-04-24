#made by Kaian Vinicius
#thanks gringos its strange but it works

def mergesort(arr):
    if len(arr) > 1: #if array is one its already sorted lmao
        left_arr = arr[:len(arr)//2] #subarray from the beggining of the array until the middle, ":len(arr)//2" returns a slice of the origin, beggining at 0, the : before menas "0:"
        right_arr = arr[len(arr)//2:] #subarray from the middle until the end of the array "len(arr)//2:" returns a slice of the origin, until the last value of the array, the : in the end means ":len(arr)"
        #// means an integer division, no decimals around here

        #recursion
        mergesort(left_arr)
        mergesort(right_arr)

        #merge
        i = 0 #idx of leftmost element in the left array
        j = 0 #idx of leftmost element in the right array
        k = 0 #idx of the merged array
        while i < len(left_arr) and j < len(right_arr): #comparison loop
            if left_arr[i] < right_arr[j]: #check leftmost elements of both arrays
                arr[k] = left_arr[i] #saves the left array value to the merged array
                i += 1       
            else:
                arr[k] = right_arr[j] #right array is smaller than left array or equal, saves it
                j += 1
            k += 1 #k always will increase, it's always merging

        while i < len(left_arr): #transfer leftovers of left array to merged array
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr): #transfer leftovers (or "rightovers" *badumtss* please laugh) of right array to merged array
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
mergesort(arr_test)
print(arr_test)
