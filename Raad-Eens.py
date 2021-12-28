import random
number = random.randint(1,1000)

guess = 9
points = 1

a = number + 50
b = number + 20
c = number - 50
d = number - 20
e = number + 51
f = number - 51

while guess == 0 or points < 20:
    print("Raad een nummer tussen 1 en 1000 , als u wilt stopOen dan scrijf 00")
    raad = int(input("Raad een nummer:"))
    if raad == number :
        points += 1
        print("geraad! U heeft nu " , points , "punt!")
        print("Nog een getal raden?")
        number = random.randint(1,1000)
        if points == 20:
            break
    elif raad == 00:
        break
    elif raad > e :
        print("Uw raad is hoger! U mag",  guess , "raden")
        guess -= 1
        if guess == 0:
            break
    elif raad < f :
        print("Uw raad is lager! U mag",  guess , "raden")
        guess -= 1
        if guess == 0:
            break
    elif raad < a and raad > b :
        print("U bent warm! U mag",  guess , "raden")
        guess -= 1
        if guess == 0:
            break
    elif raad < b and raad > number :
        print("U bent heel warm! U mag", guess , "raden")
        guess -= 1
        if guess == 0:
            break
    elif raad  > c and raad < d :
        print("U bent warm! U mag",  guess , "raden")
        guess -= 1
        if guess == 0:
            break
    elif raad > d and raad < number :
        print("U bent heel warm!  U mag",  guess , "raden")
        guess -= 1
        if guess == 0:
            break
if points == 20:
    print("Goed gedaan! u bent klaar , uw eindscore is" , points)
elif guess == 00:
    print("U heeft gestopt met de game")
else:
    print("Helaas , U heeft verloren")