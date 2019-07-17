''' 
yesterday I wrote the knapsack in tabulation
today I will write it in memoization
the benefit will be I won't have to hit every single weight

'''

#make sure we're maximizing the value
def knapSack_memoization(W, wt, val, n, K): 
    #initializing the list
    
    print(K)

    if K[n][W] != 0:
        print("this is when it's saved")
        return K[n][W]
    if n == 0 or W == 0:
        return 0

    #if the weight of the last element is greater than the leftover weight
    #limit, then we really can't include that
    if wt[n-1] > W:
        K[n][W] = knapSack_memoization(W,wt[:n-1], val[:n-1], n-1,K)
        return K[n][W]
    else:
        # see which one is greater
        K[n][W] = max(val[n-1] + 
            knapSack_memoization(W - wt[n-1],wt[:n-1], val[:n-1], n-1, K), 
            knapSack_memoization(W,wt[:n-1], val[:n-1], n-1, K))
        print("start")
        print(K)
        return K[n][W]


# To test above function 
val = [80, 60, 100, 120] 
wt = [5, 10, 20, 30] 
W = 50
n = len(val) 
K = [[0 for x in range(W+1)] for x in range(n+1)] 

print (knapSack_memoization(W , wt , val , n, K))

''' Initially, K was inside the perimiter of knapsack memoization, but that
caused some serious problem because the list K was changing every single time
Thus I had to make it as a global variable and parameter, 
pass onto the argument every single recursive call 
This might be faster than tabulization because instead of filling up 
every single thing in the DLL, all we needed to do is fill in the 
necessary value
''' 