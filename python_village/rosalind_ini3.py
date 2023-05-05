# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

if __name__ == '__main__':
    with open('./rosalind_ini3.txt', 'r') as f:
        s = f.readline().strip()
        a, b, c, d = map(int, f.readline().split())

    print(s[a:b+1], s[c:d+1])