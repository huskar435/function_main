# This is a main file of the project
# All rights are reserved
# ===================================


# import modules


import temperature as m1 # import my own module
import is_even as m2 # import my own module
import is_prime as m3 # import my own module


# the main function of project
def main():
    user_choise1 = input("Choose 01 "
        "if you want to convert temperature, else choose D: ")
    print(user_choise1)
    if user_choise1.lower() == '01':
        user_temp = float(input("Input temperature in"
                             "Celcium you want to convert: "))
        print("Your temperature in Farenheit: ", m1.temperature(user_temp)) 

    user_choise2 = input("Choose 02 "
        "if you want to checking if a number is even , else choose D: ")
    if user_choise2.lower() == '02':
        a = float(input("Input number"
                             "you want to checking: "))
        print("your answer: ", m2. is_even(a)) 

    user_choise3 = input("Choose 03 "
        "if you want to checking if a number is even , else choose D: ")
    if user_choise3.lower() == '03':
        a = float(input("Input number"
                             "you want to checking: "))
        print("your answer: ", m3. is_prime(a))
        
    else:
        main()
              
                         
if __name__ == '__main__':
    main()    