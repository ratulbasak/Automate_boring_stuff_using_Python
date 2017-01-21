import random
print("I'm thinking of a number between 1 and 20")
final_num = random.randint(1,20)
for g_num in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < final_num:
        print("Your guess is too low")
    elif guess > final_num:
        print("Your guess is too high")
    else:
        break

if guess == final_num:
    print("Good job! You've guessed the right number")
else:
    print("Nope, the number I's thinking was "+str(final_num))
