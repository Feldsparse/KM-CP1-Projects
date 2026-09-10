#charles motta: dice roller
import random
while True:
    try:
        dice = int(input("what type of dice would you like to use? D"))
    except:
       print("sorry but that's not a die size")
    else:
        break

roll = random.randint(1,dice)
print(f"you rolled a {roll} !")