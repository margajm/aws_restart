import random

print("Welcome to guess the number!")
print("The rules are simple. I will think of a number, and you will try to guess it")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    userguess = input("Guess a number between 1 and 10: ")
    if int(userguess) == number:
        print("You guessed {}. That is correct! You win!".format(userguess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(userguess))
        
"""Si el usuario no ha adivinado la respuesta correcta, ingrese el bucle.

Pida al usuario que adivine el número.

¿Es el número correcto?

Si la respuesta es correcta, dígaselo al usuario y salga del bucle.

Si no ha adivinado el número, indique al usuario que fue una suposición incorrecta y continúe con el bucle.
