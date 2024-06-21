#importing packages
import string
import random

#initializing the PASSWORD length
length=int(input("Enter the Password Length: "))

print('''-------------select the Character Set fom these options-----------------
                       1.Letters
                       2.Digits
                       3.Special Characters
                       4.EXIT''')
CharacterList=" "

#Getting character set for password
while(True):
  choice=int(input("Enter your Option: "))
   
  if(choice == 1):
    #Adding Letters to possible Characters
    CharacterList=string.ascii_letters
    
  elif(choice == 2):
    #Adding Digits to possible Characters  
    CharacterList=string.digits    
    
  elif(choice == 3):
    #Adding Special characters to the possible characters
    CharacterList=string.punctuation
  elif(choice == 4):
      break
  
  else:
      print("Enter a Valid Option!")
            
password=[]

for i in range(length):
    #Picking a random Character from our Character List
    randomchar=random.choice(CharacterList)
    
    #Appending a random Character to the Password
    password.append(randomchar)
    
print("The Password generated is: "+"".join(password))   
    

