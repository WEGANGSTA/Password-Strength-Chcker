'''This is where the user gets to input their username and password.'''

username = input("Type your username:")
password = input("Type your password:")

'''This section includes all used variables and conditions in the code.'''

token = ''
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0
score8 = 0
score9 = 0
repeated = False
lowercase = False
uppercase = False
number = False 
special_characters = False

'''This section includes test whether the password includes the following characters:
lowercase, uppercase, digits, and sepcial characters.'''

for character in password:  

    if character in "abcdefghijklmnopqrstuvwxyz":  
        lowercase = True

for character in password:         
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True 

for character in password:   
    if character in "0123456789":
        number = True 
    
for character in password:  
    if character in "!@#$%^&*()-+.":
        special_characters = True

'''This section checks whether the criteria has been met: 1 uppercase, 1 lowercase, 
1 digit, 1 special character, and length is greater than or equal to 8'''

if lowercase == True:
    score1 = score1 + 1
else:
    print("Your password must contain at least one lowercase character.")

if uppercase == True:
    score2 = score2 + 1
else:
    print("Your password must contain at least one uppercase character.")

if number == True:
    score3 = score3 + 1
else:
    print("Your password must contain at least one number.")

if special_characters == True:
    score4 = score4 + 1
else:
    print("Your password must contain at least one special character.")
   

if len(password)>=8:
  score5 = score5 + 1
else:
    print("Your password must contain at least 8 characters.")

'''checking whether password is in the known passwords text file''' 

with open(r'knownpasswords.txt', 'r') as file:
        content = file.read()
        
        if password in content:
            print('Your password is too well known.')
        else:
            score6 = score6 + 1

'''checking whether password is in the names text file'''

with open(r'names.txt', 'r') as file:
        content = file.read()
        
        if password in content:
            print('Your password contains a name.')
        else:
            score7 = score7 + 1

'''This is where the code tests whether the password is close or similar to the username'''

if username in password:  
  print('Your password must not contain username')
else:
  score8 = score8 + 1

'''This part of the code checks for repeated patterns in the password'''

for token in range(0,len(password)):
    if str(token) in password:
        print("Your password must not have a repeated pattern.")
        repeated = True
        break

if repeated == False:
    score9 = score9 + 1

'''Final Score calculator'''

final_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9

if final_score <= 1:
    print("Password is of very low strength.")

if final_score <= 3:
    print("Password is of low strength.")

if final_score <= 5:
    print("Password is of moderate strength.")

if final_score <= 7:
    print("Password is of high strength.")

if final_score == 9:
    print("Password is of very high strength.")

print("Final score out of 9 is" , final_score)
