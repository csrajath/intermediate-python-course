import random
def main():
  roll_sum = 0
  numberofrolls = 2
  for i in range(0,numberofrolls):
    rolled_num = random.randint(1,6)
    print(f'You rolled {rolled_num}')
    roll_sum += rolled_num
  print(f'Total rolled value is {roll_sum}')
if __name__ == "__main__":
  main()
