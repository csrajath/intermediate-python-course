import random
def main():
  roll_size = int(input('Enter the dice sides'))
  roll_sum = 0
  dice_num = int(input('Enter number of dice to be rolled'))
  for i in range(0, dice_num):
    roll = random.randint(1, roll_size)
    if roll == 1:
      print(f'You rolled {roll}, Critical Failure')
    elif roll>1:
      print(f'You rolled {roll}, Critical Success!!!')
    else:
      print(f'You rolled {roll}')
    roll_sum += roll
  print(f'total roll value is {roll_sum}')
if __name__ == "__main__":
  main()