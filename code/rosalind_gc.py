# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

if __name__ == '__main__':
    with open('./rosalind_gc.txt', 'r') as f:
        lines = f.readlines()
    
    gc = {}
    key = ''
    for line in lines:
        if line.startswith('>'):
            key = line.strip()[1:]
            gc[key] = ''
        else:
            gc[key] += line.strip()
    
    max_key = ''
    max_value = 0
    for key, value in gc.items():
        gc_content = (value.count('G') + value.count('C')) / float(len(value))
        if gc_content > max_value:
            max_key = key
            max_value = gc_content
    
    print(max_key)
    print(max_value * 100)