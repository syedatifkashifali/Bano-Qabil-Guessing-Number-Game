#Bano-Qabil Number Guessing Application

#printing rules
print("  || INSTRUCTIONS ||")
print(" 1. Guess limit is 10")
print (" 2. Secret number is between 1 to 100")
print(" 3. Lower or Higher hint will be provided after each attempt")
print("     ")#adding extra line space

#Generating random number between 1 to 100 to be guessed by user

import random;#importing random class for creating random number

secretnumber = random.randint(1, 100);#creating random number

guessnumber = 0;#declaring and initializing guessnumber as 0 to get in loop

limit = 0;#declaring and initializing limit as 0 it will increase as user attempt to guess

#getting the guessed number by user
print("   || GUESS A SECRET NUMBER BETWEEEN 1-100 ||");

#creating loop for iteration and to check guess limit

while(guessnumber != secretnumber):#making loop since guessnumber is not equal to secret number

   guessnumber = int(input(" Guess: "));#getting input
   
   if(guessnumber < secretnumber):
       print("  Too Lower ")#print too lower if guess is lower than secret number
       
   elif(guessnumber > secretnumber):
       print("  Too higher")#print too higher if guess is higher than secret number
       
   limit += 1 #adding attempt of user

   if(limit >= 10):#creating exit if limit reached and printing secretnumber
       print("Out of limits!")
       print("The secrect number is : ", secretnumber)
       break;
       
   if(guessnumber == secretnumber):#appreciating on guessing correctly and then exit
       print("Congratulations!, you guessed the correct number", guessnumber)
       break;



#
