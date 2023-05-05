"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

if __name__ == '__main__':
    with open('rosalind_iev.txt', 'r') as f:
        couples = [int(x) for x in f.readline().strip().split()]
    
    # AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    # 1, 1, 1, 0.75, 0.5, 0
    print(sum([x*y for x, y in zip(couples, [1, 1, 1, 0.75, 0.5, 0])])*2)