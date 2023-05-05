# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

if __name__ == '__main__':
    with open('./rosalind_dna.txt', 'r') as f:
        dna = f.read()
        
        print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
