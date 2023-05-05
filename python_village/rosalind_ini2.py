# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

if __name__ == '__main__':
    with open('./rosalind_ini2.txt', 'r') as f:
        a, b = map(int, f.read().split())

    print(a**2 + b**2)