#Write your code below this line 👇
def prime_checker(number):
    mes1= "It's a prime number."
    mes2= "It's not a prime number."
    if number<=1:
        print(mes2)
    elif number==2 or number==3:
        print(mes1)
    elif number%2==0 or number%3==0 or number%5==0:
        print(mes2)
    else:
        for i in range(4,int(number/2)):
            if(number%i==0):
                print(mes2)
        print(mes1)






#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
