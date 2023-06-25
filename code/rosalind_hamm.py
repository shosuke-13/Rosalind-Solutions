# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

if __name__ == '__main__':
    with open('rosalind_hamm.txt') as f:
        s, t = f.readlines()
        s = s.strip()
        t = t.strip()

    hamming_distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1

    print(hamming_distance)