import random

name = (input("Hello! What is your name?: "))
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")

random_number = random.randint(1,20)
remaining_guesses = 5
guesses_left = remaining_guesses
guesses_made = 0

while guesses_left > 0:
    x = int(input("Take a guess: "))
    guesses_made += 1
    if x > random_number:
        guesses_left -= 1
        print("Your guess is too high")
    elif x < random_number:
        guesses_left -= 1
        print("Your guess is too low")
    else:
        print(f"Good job {name}! You guessed my number in {guesses_made} guesses!")
        break
    
    if guesses_left == 0:
        print(f"Nope. The number I was thinking of was {random_number}")
        
        break