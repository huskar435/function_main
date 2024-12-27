# Take temperature in Celcium from user
# and convert it to Farenheit
# ======================================

# Convertation function
def temperature(C):
    return C * 1.8 + 32

# function main
def main():
    user_temp = float(input('Введите вашу температуру в градусах Цельсия:'))
    res_temp = temperature(user_temp)
    print(' Ваша температура в градусах Фаренгейта =',res_temp)


if __name__ == '__main__':
    main()