#made by Kaian Vinicius
#thanks gringo ur the best ty

def swap(lst, i ,j): #swap elements
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper): #used to heap and sort list
    while (True):
        l, r = i*2+1, i*2+2 #left and right children idx
        if max(l, r) < upper: #if we have 2 children
            if lst[i] >= max(lst[l], lst[r]): break #if true, nothing else is needed (break)
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l #update to new parent
            else:
                swap(lst, i, r)
                i = r #update to new parent
        elif l < upper: #check if only 1 child exists on the left
            if lst[l] > lst[i]: #check if the one is greater
                swap(lst, i, l)
                i = l
            else: break
        elif r < upper: #same check but right
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else: break
        else: break #no children



def heapsort(lst):
    for j in range((len(lst)-2)//2, -1, -1): #loop to heapify list
        siftDown(lst, j, len(lst))
    
    for end in range(len(lst)-1, 0, -1): #loop for sorting list
        swap(lst, 0, end)
        siftDown(lst, 0, end)

lst = [5, 16, 8, 14, 20, 1, 26]
heapsort(lst)
print(lst)