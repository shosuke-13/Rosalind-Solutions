# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

if __name__ == '__main__':
    with open('./python_village/rosalind_ini6.txt') as f:
        s = f.read().strip()

    words = s.split()
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    
    for word, count in word_count.items():
        print(word, count)