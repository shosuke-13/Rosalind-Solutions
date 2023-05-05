# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

if __name__ == '__main__':
    with open('./rosalind_ini5.txt', 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if i % 2 == 1:
                print(line.strip())