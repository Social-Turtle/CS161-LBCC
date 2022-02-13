print("Welcome to the prime checker tool!")
user_num = int(input("Please input an integer that you would like to check. "))
#the number we are checking for primality
divisor = 2
#the constant of division to check with (will change later)
prime = "unknown"
#status of prime identity used to determine success/failure message and end testing loop.

while prime == "unknown":
    #check if user's number is cleanly divided. Starts at two, but after two all evens are checked, so we move to three and step by two from there.
    print(divisor,"goes into",user_num,"a total of",user_num//divisor,"times, and leaves a remainder of ", user_num % divisor)
    if divisor == 2:
        divisor+=1
    else:
        divisor += 2
    #if function to produce 1step-2step phenomenon
    if divisor >= user_num**.5 :
        prime = True
    #give up if you've reached the square root of user input
    if user_num % divisor == 0:
        prime = False
    #declare success if you find a factor

if prime == False:
    print(divisor,"goes into",user_num,"a total of",user_num//divisor,"times, and leaves a remainder of ", user_num % divisor, "therefore, it is not a prime.")
if prime == True:
    print("Wohooo! This number is a prime!")
#outputs for user depending on result.