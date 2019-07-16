'''
Today I will continue on the knapsack problem.
Previously, we have implemented via simple recursion, for today,
we will be using tabulation, one of the two methods of DP to more efficiently
implemnt the knapsack problem
for recap
''' 

#this one is removing the nth element per depth
def knapSack_recursion1(W , wt , val , n): 
    # Base Case 
    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        return knapSack_recursion1(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack_recursion1(W-wt[n-1] , wt , val , n-1), 
                   knapSack_recursion1(W , wt , val , n-1)) 

def knapSack_recursion2(W, wt, val, n):

    if n == 0 or W == 0:
        return 0

    if wt[0] > W:
        return knapSack_recursion2(W,wt[1:],val[1:],n-1)

    else:
        return max(val[0] + knapSack_recursion2(W-wt[0],wt[1:],val[1:],n-1), 
            knapSack_recursion2(W,wt[1:],val[1:],n-1))

# To test above function 
val = [80, 60, 100, 120] 
wt = [5, 10, 20, 30] 
W = 50
n = len(val) 

print (knapSack_recursion1(W , wt , val , n))
print (knapSack_recursion2(W , wt , val , n))

'''
For recap, W is the weight limitation, wt is the list of all the weights
and the value is the according value for that weight
n is the number of weights/values there are
we decrement

interesting part about this question is that we are trynna maximize the value
while it is restricted by the weight

I wrote the second version of it and I think I have a pretty good understanding
of this recursion
'''