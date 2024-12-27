#  Checking if a number is even


# Function to determine the parity of a number
def is_even(g):
    if g % 2 == 0:
        print('Число четное')
    else:
        print('Число нечетное')


# Main function
def main():
    print('Введите введите число:')
    a=int(input())
    res = is_even(a)
    if res is True:
        print('Число',a,'четное')
    else:
        print('Число',a,'нечетное')

if __name__ == '__main__':
    main()