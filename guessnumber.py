import random
#ask user for range
low = int(input("Enter lower limit:"))
high = int(input("enter Upper limit:"))

print(f"Range input by you is - {low} to {high}")
num = random.randint(low , high)

ch = 7                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')