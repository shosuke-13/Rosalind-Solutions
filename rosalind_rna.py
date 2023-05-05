# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

if __name__ and '__main__':
    with open('./rosalind_rna.txt', 'r') as f:
        dna = f.read()
        
        print(dna.replace('T', 'U'))