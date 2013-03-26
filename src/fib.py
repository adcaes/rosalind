'''
Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months if each pair of reproduction-age 
        rabbits produces a litter of k rabbit pairs in each generation (instead of only 1 pair).
'''


def fib(n, k):
    fib = []
    for i in range(0, n):
        if i < 2:
            fib.append(1)
        else:
            fib.append(fib[i-2]*k + fib[i-1])

    return fib[-1]

with open('rosalind_fib.txt', 'r') as f:
    n, k = f.readline().split()
    print fib(int(n), int(k))
