# merge sorted lists
def mergeLists(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    if n1 == 0: # lst1 is empty
        return list(lst2)
    elif n2 == 0:
        return list(lst1)
    else:
        output_lst = [] # This is the list we will return
        i1 = 0
        i2 = 0
        while (i1 < n1 or i2 < n2):
            if i1 < n1 and i2 < n2: # We are processing both lists
                if (lst1[i1] <= lst2[i2]): # lst[i1] is the smaller elt
                    output_lst.append(lst1[i1]) # append to end of output list
                    i1 = i1 + 1 # advance index i1
                else:
                    output_lst.append(lst2[i2]) # append to end of output list
                    i2 = i2 + 1 # advance index i2
            elif i1 < n1: # We have run past the end of lst2
                output_lst.append(lst1[i1]) # append lst1 to end of output list
                i1 = i1 + 1
            else:  # We have run past the end of lst1
                output_lst.append(lst2[i2]) # append lst2 to end of output list
                i2 = i2 + 1
        return output_lst

******************************************************************************************************************************************************************
      
      
def swap(lst, i, j):
    n = len(lst)
    assert( i >= 0 and i < n)
    assert( j >= 0 and j < n)
    # We can use a simultaneous assignmment to swap
    (lst[i], lst[j]) = (lst[j], lst[i])
    return 

def copy_back(output_lst, lst, left, right):
    # Ensure that the output has the right length for us to copy back
    assert(len(output_lst) == right - left + 1)
    for i in range(left, right+1):
        lst[i] = output_lst[i - left]
    return 
    
def mergeHelper(lst, left, mid, right):
    # Perform a merge on sublists lst[left:mid+1] and lst[mid+1:right+1]
    # This is the same algorithm as merge above but we will need to copy
    # things back to the original list.
    if left > mid or mid > right:  # one of the two sublists is empty
        return
    i1 = left
    i2 = mid + 1
    output_lst = []
    while (i1 <= mid or i2 <= right):
        if (i1 <= mid and i2 <= right):
            if lst[i1] <= lst[i2]:
                output_lst.append(lst[i1])
                i1 = i1 + 1
            else:
                output_lst.append(lst[i2])
                i2 = i2 + 1
        elif i1 <= mid:
            output_lst.append(lst[i1])
            i1 = i1 + 1
        else:
            output_lst.append(lst[i2])
            i2 = i2 + 1
    copy_back(output_lst, lst, left, right)
    return 
    
def mergesortHelper(lst, left, right):
    if (left == right): # Region to sort is just a singleton
        return 
    elif (left + 1 == right): # region to sort has two elements
        if (lst[left] > lst[right]): # compare 
            swap(lst, left, right)   # and swap if needed
    else: 
        mid = (left + right ) // 2  # compute mid point
        mergesortHelper(lst, left, mid) # Sort left half
        mergesortHelper(lst, mid + 1 , right) # Sort right half
        mergeHelper(lst, left, mid, right) # merge them together.
        
# Function mergesort
#   Sort the list in place and modify it so that 
#   lst is sorted when the function returns.
def mergesort(lst):
    if len(lst) <= 1:
        return # nothing to do
    else:
        mergesortHelper(lst, 0, len(lst)-1)
        
# running time complexity of mergesort was Θ(𝑛log(𝑛)) for an input list of size  𝑛
