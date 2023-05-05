# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

if __name__ == '__main__':
    with open('rosalind_fib.txt', 'r') as f:
        n, k = [int(x) for x in f.readline().strip().split()]
        
    rabbits = [1, 1]
    for i in range(2, n):
        rabbits.append(rabbits[i-1] + k*rabbits[i-2])

    print(rabbits[-1])