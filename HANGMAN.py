
#some design for intros
def hangman():
    print()
    print()
    print()
    print('''
                    O))     O))       O)        O)))     O))    O))))             O))       O))       O)        O)))     O))
                    O))     O))      O) ))      O) O))   O))  O)    O))           O) O))   O)))      O) ))      O) O))   O))
                    O))     O))     O)  O))     O)) O))  O)) O))                  O)) O)) O O))     O)  O))     O)) O))  O))
                    O)))))) O))    O))   O))    O))  O)) O)) O))          O)))))  O))  O))  O))    O))   O))    O))  O)) O))
                    O))     O))   O)))))) O))   O))   O) O)) O))   O))))          O))   O)  O))   O)))))) O))   O))   O) O))
                    O))     O))  O))       O))  O))    O) ))  O))    O)           O))       O))  O))       O))  O))    O) ))
                    O))     O)) O))         O)) O))      O))   O)))))             O))       O)) O))         O)) O))      O))
    ''')

def thankyou():
    print('''

           >===>>=====> >=>    >=>       >>       >==>    >=>  >=>   >=>   >=>      >=>     >===>       >=>     >=> 
                >=>     >=>    >=>      >>=>      >> >=>  >=>  >=>  >=>     >=>    >=>    >=>    >=>    >=>     >=> 
                >=>     >=>    >=>     >> >=>     >=> >=> >=>  >=> >=>       >=> >=>    >=>        >=>  >=>     >=> 
                >=>     >=====>>=>    >=>  >=>    >=>  >=>>=>  >>=>>           >=>      >=>        >=>  >=>     >=> 
                >=>     >=>    >=>   >=====>>=>   >=>   > >=>  >=>  >=>        >=>      >=>        >=>  >=>     >=> 
                >=>     >=>    >=>  >=>      >=>  >=>    >>=>  >=>   >=>       >=>        >=>     >=>   >=>     >=> 
                >=>     >=>    >=> >=>        >=> >=>     >=>  >=>     >=>     >=>          >===>         >====>    
                                                                                                       

    ''')
    
def from1():
    print('''

                ||||||||  |||||||      |||||     |||     |||
                ||        ||   |||    ||    ||   || |   | ||
                ||        ||  ||||   ||      ||  ||  |||  ||
                ||||||||  ||||||    ||        || ||       ||
                ||        ||   ||    ||      ||  ||       ||
                ||        ||    ||    ||    ||   ||       ||
                ||        ||     ||     ||||     ||       ||

''')

def ashim():
    print('''

                >>          >=>>=>    >=>    >=>  >=>  >=>       >=> 
               >>=>       >=>    >=>  >=>    >=>  >=>  >> >=>   >>=> 
              >> >=>       >=>        >=>    >=>  >=>  >=> >=> > >=> 
             >=>  >=>        >=>      >=====>>=>  >=>  >=>  >=>  >=> 
            >=====>>=>          >=>   >=>    >=>  >=>  >=>   >>  >=> 
           >=>      >=>   >=>    >=>  >=>    >=>  >=>  >=>       >=> 
          >=>        >=>    >=>>=>    >=>    >=>  >=>  >=>       >=> 
                                                       

''')



#this is full python script of my hangman game project...enjoyyyy...................

import time
import random
from words import dict1

def man0():
    print()
    print()
    print("   ---------------")
    print("   | ")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("------")
    print()
    print()
    
def man1():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("------")
    print()
    print()
    
def man2():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   | ")
    print("   | ")
    print("   | ")
    print("   |")
    print("------")
    print()
    print()
    
def man3():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   |            / ")
    print("   | ")
    print("   | ")
    print("   |")
    print("------")
    print()
    print()
    
def man4():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   |            / \ ")
    print("   | ")
    print("   | ")
    print("   |")
    print("------")
    print()
    print()
    
def man5():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   |            /|\ ")
    print("   |             |")
    print("   |              ")
    print("   |")
    print("------")
    print()
    print()
    
def man6():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   |            /|\ ")
    print("   |             |")
    print("   |            / ")
    print("   |")
    print("------")
    print()
    print()
    
def man7():
    print()
    print()
    print("   ---------------")
    print("   |             |")
    print("   |             O")
    print("   |            /|\ ")
    print("   |             |")
    print("   |            / \ ")
    print("   |")
    print("------")
    print()
    print()

#This is final function for printing man:

def print_man(error_list):
    if len(error_list)==0:
        man0()
    elif len(error_list)==1:
        man1()
    elif len(error_list)==2:
        man2()
    elif len(error_list)==3:
        man3()
    elif len(error_list)==4:
        man4()
    elif len(error_list)==5:
        man5()
    elif len(error_list)==6:
        man6()
    elif len(error_list)==7:
        man7()


    
    
    
#now i created a function for some intro
def intro():
    print()
    print()
    print()
    print("\t\t\t\t\t|||"+'~'*65+"|||")
    time.sleep(1)
    print("\t\t\t\t\t\t\t\t    ***WELCOME TO -HANG MAN ***")
    print("\t\t\t\t\t\t\t        ****Developed by- ASHIM PAUDEL****")
    print("\t\t\t\t\t\t\t                *version 3.0*")
    time.sleep(1)
    print("\t\t\t\t\t|||"+'~'*65+"|||")
    print()
    print()
    print()
    time.sleep(2)
    
    
#i've created a function to print the game rules if user want to see that 

def game_rules():
    print()
    print()
    print()
    print("\t\t"+"_"*120)
    print("\t\t"+"|\t\t\t\t\t**Game instructions**")
    print("\t\t"+"|\t\t\t\t\t    =================")
    time.sleep(1)
    print("\t\t"+"|\t\t1.You can guess either :the whole word or any letter. ")
    time.sleep(1)
    print("\t\t"+"|\t\t2.For each wrong attempts ,the program will create a hanging man.")
    time.sleep(1)
    print("\t\t"+"|\t\t3.In total you will have only-7 attempts.")
    time.sleep(1)
    print("\t\t"+"|\t\t4.If you guessed the whole word correctly, whole word will be accepted as your input and you win.")
    time.sleep(1)
    print("\t\t"+"|\t\t5.Else, only first letter of your guess will be accepted and run accordingly.")
    time.sleep(1)
    print("\t\t"+"|\t\t6.The number of characters in probable in word will be equal to no of underscores ' _ '.")
    time.sleep(1)
    print("\t\t"+"|\t\t7. For hint about the word, type ' hint '  . But accessing hint will reduce your attempt too.")
    time.sleep(1)
    print("\t\t"+'|'+"_"*119)
    print()
    print()
    print()
    
    
    
    
    
#now this is key-engine of my game:
#i 've created the whole game in a function
def main_game():
    already_guessed=[]
    error_attempts=[]
    
    random_items=random.choice([item for item in dict1.items()])
    random_word=random.choice(random_items[1]).upper().replace(' ','')
    word_hint=random_items[0]
    
    #creating a random choice/selection of words from a list of some sample words
    print()
    print()
    time.sleep(1)
    while len(error_attempts)!=7:
        print('~'*110)
        print("\t\t\t\t Guess the word:     ",  display(random_word,set(already_guessed)))
        print()
        user_guess=input("\t\t\t\t Please input your guess (the word/letter) :-   ").upper()
        print()
        print()
            
        if user_guess==random_word:
            print()
            print('~'*110)
            print("\t\t\t\t Yay!!!  you've guessed the word: ''{}'' correctly".format(random_word))
            print("\t\t\t\t Congratulations!!! you won. ")
            print()
            print('~'*110)
            print()
            break
        elif user_guess=='HINT':
            print()
            print("\t\t\t Your chance will be reduced by 1.")
            error_attempts.append(user_guess)
            print_man(error_attempts)
            print('\t\t\t---You have requested for word hint.... ---')
            time.sleep(1)
            print('\t\t\t ---Fetching hint from database..... ---')
            time.sleep(3)
            print('\t\t\t','HINT: ',word_hint)
            
           
            
            
            
        elif user_guess[0] in already_guessed:
            print("\t\t\t\t You have already guessed  '{}'".format(user_guess[0]))
            print("\t\t\t\t The letters you've correctly guessed till now are:  {}".format(set(already_guessed)))
            print('\t\t\t\t ', display(random_word,set(already_guessed)))
            if set(already_guessed)==set(random_word):
                print()
                print('~'*110)
                print()
                print("\t\t\t\t Yay!!! you've successfully guessed the correct word.")
                print("\t\t\t\tThe word is:  {}".format(random_word))
                print("\t\t\t\t Congratulations!!! , you won.")
                print()
                print('~'*110)
                print()
                break
            else:
                continue
        elif user_guess[0] in random_word:
            already_guessed.append(user_guess[0])
            print()
            print("\t\t\t\t Awesome guess!!! '{}'  is in that word    ".format(user_guess[0]))
            print("\t\t\t\t You are doing good!!!")
            print()
            print('\t\t\t\t ', display(random_word,set(already_guessed)))
            print()
            print_man(error_attempts)
            if set(already_guessed)==set(random_word):
                print()
                print('~'*110)
                print()
                print("\t\t\t\t Yay!!! you've successfully guessed the correct word.")
                print("\t\t\t\tThe correct word is:  {}".format(random_word))
                print("\t\t\t\t Congratulations!!! , you won.")
                print()
                print('~'*110)
                print()
                break
            else:
                continue
                
        elif user_guess[0] in error_attempts:
            print('\t\t\t\t', "You've already guessed the letter:- ",user_guess[0])
            print('\t\t\t\t ',user_guess[0], "is an incorrect guess")
            print('\t\t\t\t You have incorrectly entered:   ',set(error_attempts))
        elif user_guess[0] not in random_word:
            error_attempts.append(user_guess[0])
            print()
            print('-'*100)
            print("\t\t\t\t Sorry the letter '{}', you guessed is incorrect. \t\t\t\t   ".format(user_guess[0]))
            print('-'*100)
            print()
            display(random_word,set(already_guessed))
            print()
            print_man(error_attempts)
            
        print()
        print('~'*110)
        print()
    if len(error_attempts)==7:
        print()
        print('-'*100)
        print("\t\t\t\t Sorry!!! you ran out of attempts\t\t\t\t\t\t\t  ")
        print("\t\t\t\t Better luck next time!!! ")
        print("\t\t\t\t The correct word was:  '{}'\t\t\t\t\t\t\t  ".format(random_word))
        print('-'*100)
        print()
        print()
        print('~'*110)
        print()
        print()
       
	   
        
#function to replace underscore by guessed letter or word:
def display(word, guessed):
    word = ' '.join([ch if ch in guessed else '_' for ch in word])
    return word


#my main program starts here

time.sleep(1)
hangman()
time.sleep(0.7)
intro()

print()
print("\t\t\t\t",'~'*100)
print("\t\t\t\t\t\t Do you want to look the rules and instructions ? (y/n)")
print("\t\t\t\t",'~'*100)
ask=input()
response=ask[0].upper()
while response!='Y' and response!="N":
    print('\t\t\t\t ',"Sorrry! '{}' was an invalid input. Say (y/n)".format(ask))
    ask=input()
    response=ask[0].upper()
if response=='Y':
    game_rules()
    print()
    time.sleep(1.5)
    print("\t\t\t\t",'~'*100)
    print("\t\t\t\t\t\t\t\t Lets play HANG-MAN !!! ")
    print("\t\t\t\t",'~'*100)
    time.sleep(1.5)
    print()
else:
    print()
    time.sleep(1.5)
    print("\t\t\t\t",'~'*100)
    print("\t\t\t\t\t\t\t\t Lets play HANG-MAN !!! ")
    print("\t\t\t\t",'~'*100)
    time.sleep(1.5)
    print()
    
    
program_active=True #for repitition of the game

while program_active:
    main_game() #key engine of my program
    
    print()
    time.sleep(1.5)
    print("\t\t\t\t",'~'*100)
    print("\t\t\t\t\t\t Do you want to play the game again ? (y/n)")
    print("\t\t\t\t",'~'*100)
    ask1=input()
    response1=ask1[0].upper()
    while response1!='Y' and response1!="N":
        print('\t\t\t\t ',"Sorrry! '{}' was an invalid input. Say (y/n)".format(ask1))
        ask1=input()
        response1=ask1[0].upper()
    if response1=='N':
        program_active= False
        print()
        print("\t\t\t\t",'~'*100)
        print("\t\t\t\t\t\t\t\t Good-Bye! ")
        print("\t\t\t\t",'~'*100)
        print()
    else:
        print()
        print("\t\t\t\t",'~'*100)
        print("\t\t\t\t\t\t\t\t Lets play HANG-MAN again....... ")
        print("\t\t\t\t\t\t\t\t Better luck!!! ")
        print("\t\t\t\t",'~'*100)
        print()
#main program ends here


time.sleep(1)
#collecting feedback
print()
print("\t\t\t\t",'~'*100)
print("\t\t\t\t\t\t Did you enjoy this game ? (y/n)")
print("\t\t\t\t",'~'*100)
ask2=input()
response2=ask2[0].upper()
while response2!='Y' and response2!="N":
    print('\t\t\t\t ',"Sorrry! '{}' was an invalid input. Say (y/n)".format(ask2))
    ask2=input()
    response2=ask2[0].upper()
if response2=='Y':
    print()
    time.sleep(0.5)
    thankyou()
    time.sleep(0.5)
    from1()
    time.sleep(0.5)
    ashim()
    time.sleep(0.5)
    print()
else:
    print()
    print("\t\t\t\t",'~'*100)
    time.sleep(0.5)
    thankyou()
    time.sleep(0.5)
    from1()
    time.sleep(0.5)
    ashim()
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t Ashim will improve this game furthur")
    print("\t\t\t\t",'~'*100)
    print()
    
  

  
print("\t\t\t\t\t\t\t  ENTER ANY KEY TO QUIT")
input()

#and the code ends here
    
