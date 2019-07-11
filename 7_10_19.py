''' 
For today, I will be doing a lot of readings

2 properties of DP
Overlapping Subproblems property and Optimal Substructure property 

1) DP is used when the solutions of the subproblems r needed again and again
these solutions r stored in a table so it wont need to be computed 
Memoized version doesn't fill all entries

2) if optimal solution of the given problem can be obtained by using 
optimal solutions of its subproblems. good example would be shortest path, 
but the longest problem wouldn't be

Then how do we solve a DP problem?

1) Identify
 - 
2) Decide state expression with least parameters
 - State and Transition
 - State -> set of parameters that can uniquely identify a certain position

3) Formulate state relationship
 - alot of intuition -> depends on the problem 

 ex) when the options are 1, 3, 5
 State(7) = state(6) + state(4) + state(2)
4) Do tabulation / memoization

'''

'''Knapsackproblem
Given weights and values of n items, put these items in a knapsack of 
capacity W to get maximum total value in knapsack
'''

# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W , wt , val , n): 
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 

# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 

print (knapSack(W , wt , val , n))
