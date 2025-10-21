# how to write a function 
k = int(input("enter the value of k"))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * factorial(n-1)
      
# here only return function should be used
print(factorial(k))

# example 2 
def average(scores):
    return sum(scores)/ len(scores)

print(average([1,8,9,6,8]))

# priime checker
def prime(n):
    if(n%2==0):
        print("non prime")
        # anyone of the statement can be used 
        return False
    else:
        print("prime")
        # anyone of the statement can be used
        return True
      
        
print(prime(k))  

# even odd checker

def is_even(n):
    if n%2 == 0:
        return True
        # if you write 2 returns 1st one will be executed
        return "even"
    else:
        return False
         # if you write 2 returns 1st one will be executed
        return "odd"

print(is_even(k))    
          
        