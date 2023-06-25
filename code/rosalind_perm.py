# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
import itertools

if __name__ == "__main__":
    with open("./rosalind_perm.txt", "r") as f:
        n = int(f.readline().strip())
    
    temp = []
    for i in range(n):
        temp.append(i + 1)

    list2 = list(itertools.permutations(temp, n))

    print(len(list2))
    for l in list2:
        print(" ".join([str(i) for i in l]))
