num=int(input("enter a number"))
temp=num
rev   =0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
   
if rev==temp:
    print("it is a palindrome")
else:
    print("it is not a palindrom")

