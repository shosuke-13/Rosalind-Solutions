# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

if __name__ == '__main__':
    with open('./rosalind_iprb.txt', 'r') as f:
        k, m, n = map(int, f.read().split())
        
        total = k + m + n
        
        i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
        j = 4 * total * (total - 1)

        rst = 1 - float(i) / j

        print(rst)