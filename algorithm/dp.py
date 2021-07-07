# Dynamic programming - identifying and solving subproblems and using them
# to solve a larger problem 

"""
Longest Increasing Subsequence problem 

for a sequence a1, a2, ... find the length of the longest increasing subsequence-> we can have a length or the entire sequence itself

TIP 1. Visualize Examples

Longest path in the graph -> correlates to graph length + 1
longest increasing subsequence

TIP 2. Finding appropriate subproblem

LIS[k] = LIS ending at index k

TIP 3. Find relationships among subproblems

TIP 4. generalize the relationship

TIP 5. Implement by solving subproblems in order

Increasing subsequence are subsets of original sequence
All increasing subsequences have start and end

[3,1,8,2,5] 

LIS[4] = 1 + max {LIS[0], LIS[1], LIS[2]} = 3 

A = [5, 2, 8, 6, 3, 6, 9, 5] 
LIS[5] = 1 + max{LIS[k] | k < 5 & A[k] < A[5]}

def lis(A):
  L = [1] * len(A)
  for i in range(1, len(L)):
    subproblems = L[k] for k in range i if A[k] < A[i]
    L[i] = 1 + max(subproblems, default = 0)
  return max(L, default=0)



"""
