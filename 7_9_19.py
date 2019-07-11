'''
Basics of Dynamic programming 
whatever we can do it recursively, we can do it using DP
we simply store the results of subproblems, so we dont have to recompute again

There are two different ways to store the values for DP 
Tabulation (Bottom Up, starts from dp[0] to dp[n])
Memoization (Top down, starts from dp[n] to dp[0])


here I did a quick example of doing a factorial in tabular vs memoization

'''

mem = [-1] * 10


# fill in every single dp list as u go up 
def factorial_tab(a):
    dp = [-1] * 500
    dp[0] = 1 
    for i in range (1, a+1):
        dp[i] = dp[i-1] * (i)
    return dp[a]


# only fill the necessary ones
def factorial_mem(a):

    if a == 0:
        return 1
    elif mem[a] != -1:
        return mem[a]
    else:
        mem[a] = a * factorial_mem(a-1)
        return mem[a]



def test():
    print(factorial_tab(3))
    print(factorial_tab(5))
    print(factorial_mem(3))
    print(mem)
    print(factorial_mem(5))
    print(mem)
    return True

test()