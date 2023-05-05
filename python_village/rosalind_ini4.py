# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

if __name__ == '__main__':
    with open('./rosalind_ini4.txt', 'r') as f:
        a, b = map(int, f.read().split())

    print(sum([x for x in range(a, b+1) if x % 2 == 1]))