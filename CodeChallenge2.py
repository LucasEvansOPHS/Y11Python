x=1
while x ==1:    #loops the program
  print("welcome new user!")    #prints welcome message
  print("")
  check="n"  #allows a loop to re-enter incorrect data
  while check=='N' or check=='n':
    age=str(input("please enter your age >>>"))    #allows user to enter age
    gender=str(input("please enter your gender as M(male) F(female) or O(other) >>>"))    #allows user to enter gender
    if gender=='M' or gender=='m':    #allows the gender to be displayed in full from a character
      genDisplay="male"
    elif gender=='F' or gender=='f':
      genDisplay='female'
    else:
      genDisplay='other'
    email=str(input("please enter a valid email address >>>"))    #allows user to enter email address 
    playName=str(input("please enter a nickname/player name >>>"))    #allows user to enter a player name
    print("")
    print("you are: "+age+" years old")
    print("your gender is: "+genDisplay)
    print("your email adress is : "+email)
    print("your nickname/player name is : "+playName)
    check=str(input("is this information correct? Y or N >>>"))
  print("you are: "+age+" years old")
  print("your gender is: "+genDisplay)
  print("your email adress is : "+email)
  print("your nickname/player name is : "+playName)

 
  
