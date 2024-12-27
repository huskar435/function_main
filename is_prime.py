# Checking for primality of a number

# Function for determining the primality of a number
def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

# Main function
def main():
    print('Введите число ')
    a = float(input())
    result = is_prime(a)
    if result:
        print('простое число')
    else:
        print('не простое число')

if __name__ == '__main__':
    main()