secret_number = 7
for attempt in range(1, 4):
    guess = int(input("Guess the number: "))
    if guess == secret_number:
     print("Correct! you won!")
    break
else: 
    print("Wrong guess!")
    print("Game Over")
