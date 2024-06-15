#created by Shayan Gates
import random

# 0 = rock
# 1 = scissor
# 2 = paper

rock = '''
     ---------
-----      ------
                  )
           -------
                  )
           -------
                  )
           -------
                  )
------------------
'''
scissor = '''
     ---------
-----      ------------------
                              )
           --------------------
                                )
           --------------------
                  )
           -------
                  )
------------------
'''
paper = '''
     |   |
     |   |
     |   |
     ---------
-----      ------------------
                              )
           --------------------
                                )
           --------------------
                                )
           ---------------------
                                )
--------------------------------
'''

games_imagers = [rock,scissor,paper]
user_input = int(input("Enter a number between 0 to 2: "))

if (user_input >=3 or user_input<0):
    print("You entered an invalid choice!")
else:
    print(games_imagers[user_input])

    cpu_input = random.randint(0,2)
    print("You chose: ",user_input," Computer chose: ",cpu_input)
    print(games_imagers[cpu_input])
    if(user_input == cpu_input):
        print("Draw!")
    elif(user_input==0 and cpu_input==1):
        print("You win!")
    elif(user_input==0 and cpu_input==2):
        print("Computer wins!")
    elif(user_input==1 and cpu_input==2):
        print("You win!")
    else:
        print("Computer wins!")
