# takes positive integer num and its length returns reverse of that number


# we pop the number and add it to final and left shift final 
# O(n)
def reverse_num(num, num_digits):
    final = 0

    for i in range (num_digits):
        digit = num % 10
        final = final * 10
        final = final + digit
        num = num // 10

    return final 

def test():
    if (reverse_num(12345,5) != 54321):
        return False
    if (reverse_num(2040,4) != 402):
        return False
    return True


print(test())