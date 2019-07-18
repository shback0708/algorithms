'''
for recap we wrote knapsack in tabulation and memoization
K = [[0 for x in range(W+1)] for x in range(n+1)] 
this is how we make a 2D array with n rows and w col 

Today will be doing Lngest Increasing subsequence problem (LIS)
ex) LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80}, 
length is 6 and LIS is {10, 22, 33, 50, 60, 80}.
''' 

#trynna do it myself

# def LIS(list):
#     return LIShelper(list,[],0)

# def LIShelper(list,listfinal,length):
#     if list == []:
#         return listfinal,length
#     else:
#         elem = list[0]
#         if length == 0:
#             op1 = LIShelper(list[1:], listfinal + [elem], length + 1)
#             op2 = LIShelper(list[1:], listfinal, length)
#             return max(op1, op2)
#         if elem <= listfinal[length-1]:
#             return LIShelper(list[1:], listfinal, length)
#         #option 1 u add to the list
#         option1 = LIShelper(list[1:], listfinal + [elem], length + 1)
#         #opton 2 u dont add to the list
#         option2 = LIShelper(list[1:], listfinal, length)
#         return max(option1, option2)





'''
problem for this solution was that since we're recursing through, 
we can't return both list and the count of longest increasing subsequence
''' 

def LIS(list):
    return LIShelper(list,[],0)

def LIShelper(list,listfinal,length):
    if list == []:
        return length
    else:
        elem = list[0]
        # print(elem)
        # print(list[1:])
        op1 = LIShelper(list[1:], listfinal + [elem], length + 1)
        op2 = LIShelper(list[1:], listfinal, length)
        if length == 0:
            return max(op1,op2)
        elif elem <= listfinal[length-1]:
            return LIShelper(list[1:], listfinal, length)
        # print ("list is", list)
        # print("list final is", listfinal)
        else:
            print(listfinal)
            print(length)
            return max(op1,op2)


# this function does work, except when I printed stuff out it confused the heck out of me
# because it will still print out wrong lists
# the given solution looks like this 



global maximum 
  
def _lis(arr , n ): 
  
    # to allow the access of global variable 
    global maximum 
  
    # Base Case 
    if n == 1 : 
        return 1
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1
  
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum , maxEndingHere) 
  
    return maxEndingHere


def lis(arr): 
  
    # to allow the access of global variable 
    global maximum 
  
    # lenght of arr 
    n = len(arr) 
  
    # maximum variable holds the result 
    maximum = 1
  
    # The function _lis() stores its result in maximum 
    _lis(arr , n) 
  
    return maximum


arr0 = [1,3,2]
arr1 = [10 , 22 , 9] 
arr2 = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
arr3 = [10,9,8,7,6]
arr4 = [18,4, 58, 7, 106, 2]
print(lis(arr2))

