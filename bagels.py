import random

def generate_secret_number():
    return random.randint(100,999)

p = "PICO"
f = "FERMI"
b = "BAGELS"

num = str(generate_secret_number())

def provide_hint(input):
    input = str(input)
    sol = b
    cls_sol_exec = False
    for i in range(0,3):
        for j in range(0,3):
            if input[i] == num[j]:
                if not cls_sol_exec:
                    sol = ""
                    cls_sol_exec = True
                if i == j:
                    sol += (f + " ")
                else:
                    sol += (p + " ")
    return sol

game = True
print("Bagels, a deductive logic game.\nBy Aryan Mishra (2241013129)\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say: That means:\nPico : One digit is correct but in the wrong position.\nFermi : One digit is correct and in the right position.\nBagels : No digit is correct.")
print(num)
while game:
    print("\nI have thought up a number.\nYou have 10 guesses to get it.\n(if you enter invalid number, you lose instantly, so type carefully!)\n")
    for i in range(0,10):
        try:
            ask = int(input("Guess " + "#" + str(i+1) + " : "))
        except ValueError:
            print("Enter valid number !")
            break
        if (ask >=100) and (ask <= 999): 
            final_sol = provide_hint(ask)
            if final_sol == 3*(f + " "):
                print("You got it !")
                break
            else:
                print(final_sol)
        else:
            print("Sorry, you entered wrong value, you lost ...")
            break

    print("The number was : " + num)
    while True:
        cont = input("Do you want to play it again ? (yes or no)\n")
        cont.lower()
        cont.strip()
        if cont == "yes":
            num = str(generate_secret_number())
            break
        elif cont == "no":
            print("Thanks for playing !")
            game = False
            break
        else:
            print("Enter correct response !")
            continue