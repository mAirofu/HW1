import random
print("Guess computer's number")
comp_num = random.randint(1, 10)
play_num = 0
attempt = 3

while play_num != comp_num:
  play_num = int(input('Your number: '))
  if comp_num > play_num:
    print("Computer's number is bigger")
    attempt -= 1
  elif comp_num < play_num:
    print("Computer's number is lower")
    attempt -= 1
  if attempt == 0:
    print("You lose!")
    print("Computer's number is", comp_num)
    print("Game over")
    break
print("Hurray! You guessed number", comp_num, "correctly!")
