''' 
we basically wrote the recursive solution for the knapsack problem
now we will write the dp solution for this
we will be writing with tabulation method
the K will have W and n as the parameter
the solution to this will be K[n][W]

n is going to be the number of items that has an according weight
and a value

W is the weight restriction, aka how many weights are left

we will implement two for loops that will loop through 
W and n, which W will be the weight and n will be the number of weights

'''

def knapSack_tabulation(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

# To test above function 
val = [80, 60, 100, 120] 
wt = [5, 10, 20, 30] 
W = 50
n = len(val) 

print (knapSack_tabulation(W , wt , val , n))

