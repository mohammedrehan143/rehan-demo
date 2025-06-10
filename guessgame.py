import random
class guess:

    a=-1
    k=-1
    computer = random.randint(1, 100)

    while(a!=computer):#this is used for itterstion while the statement dosent 
        #  get correct it dosent exit but ass soon as the condition comes correct it exists
         k +=1
         a = int(input("enter a number \n"))
         if(a>computer):
              print("lower number please")

         else:
              print("higher number please ")      
     
    print(f"your guess was right finally the guesses were {k}")  

    with open("score.txt", "w") as f:
         f.write(str(k))
         
 
