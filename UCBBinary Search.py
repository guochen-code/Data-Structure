def binarySearchHelper(lst, elt, left, right):
    n = len(lst)
    if (left > right):
        return None # Search region is empty -- let us bail.
    else: 
        # If elt exists in the list, it must be between left and right indices.
        mid = (left + right)//2 # Note that // is integer division 
        if lst[mid] == elt: 
            return mid # BINGO -- we found it. Return its index and that we found it
        elif lst[mid] < elt: 
            return binarySearchHelper(lst, elt, mid+1, right)
        else: # lst[mid] > elt
            return binarySearchHelper(lst, elt, left, mid-1)
          
          
          
def binarySearch(lst, elt):
    n = len(lst)
    if (elt < lst[0] or elt > lst[n-1]):
        return None
    else: # Note: we will only get here if
          # lst[0] <= elt <= lst[n-1]
        return binarySearchHelper(lst, elt, 0, n-1)
      
      

# we get that the running time is  Θ(log(𝑛))
