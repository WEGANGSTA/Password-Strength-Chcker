
username = input("Type your username:")
password = input("Type your password:")  
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0

#Check the password for specific characters  
lowercase = False
uppercase = False
number = False 
special_characters = False 

for character in password:  

    if character in "abcdefghijklmnopqrstuvwxyz":  
        lowercase = True
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True 
    elif character in "0123456789":
        number = True 
    elif character in "!@#$%^&*()-+.":
        special_characters = True


#length = len(password)
#passwordlist = [password]
#for i in range(length):
    #index = uppercase.index(passwordlist[i])
    #if i + 2 == length:
        #break

# checking whether password is in the known passwords text file    
with open(r'knownpasswords.txt', 'r') as file:
        # read all content from a file using read()
        content = file.read()
        # check if string present or not
        if password in content:
            print('Your password is too well known.')
        else:
            score6 = score6 + 1
            print('Your password is not well known.')

# checking whether password is in the names text file
with open(r'names.txt', 'r') as file:
        # read all content from a file using read()
        content = file.read()
        # check if string present or not
        if password in content:
            print('Your password contains a name.')
        else:
            score7 = score7 + 1
            print('Your password does not contain a name.')
    
if lowercase == True:
  print("Your password contains at least one lowercase characters.")
if uppercase == True:
  print("Your password contains at least one uppercase characters.")
if number == True:
  print("Your password contains at least one number.")
if special_characters == True:
  print("Your password contains at least one special character sign")
  
if lowercase == True:
  score1 = score1 + 1
if uppercase == True:
  score2 = score2 + 1 
if number==True:
  score3 = score3 + 1
if special_characters == True:
  score4 = score4 + 1 

if len(password)>=8:
  score5 = score5 + 1
  print("Your password is at least 8 characters long.")

final_score = score1 + score2 + score3 + score4 + score5 + score6 + score7
print("Final score out of 7 is" , final_score)

#Complete code here to check more criteria and display total score
