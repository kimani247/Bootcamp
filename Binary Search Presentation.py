#code to implement  a Binary 
# Search.
  
# It returns location of n in given array arr 
# if present, else returns -1
def findValue(arr,l,r,n):
    while l <= r:
      
        mid = l + (r - l) // 2;
          
        # Check if n is present at mid
        if arr[mid] == n:
            return mid
  
        # If  is greater, ignore left half
        elif arr[mid] < n:
            l = mid + 1
  
        # If n is smaller, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element
    # was not present
    return -1
arr = [7, 9, 14, 22, 34]
n = 22

final = findValue(arr,0,len(arr)-1,n)

if final != -1:
    print ("Element is present at index % d" % final)
else:
    print ("Element is not present in array")