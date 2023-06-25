# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

if __name__ == '__main__':
    with open('./rosalind_subs.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    locations = []
    for i in range(len(s)):
        if s[i:].startswith(t):
            locations.append(i+1)
    
    print(' '.join([str(x) for x in locations]))