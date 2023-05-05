# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

if __name__ == '__main__':
    with open('./rosalind_revc.txt', 'r') as f:
        dna = f.read()
        
        print(dna[::-1].replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper())