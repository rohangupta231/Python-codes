num=int(input("Enter a Number"))
digit=0
temp=num
rev=0
while(temp!=0):
	digit=temp%10
	temp=int(temp/10)
	rev=rev*10+digit
if(rev==num):
	print("Number is Palindrome")
else:
	print("Number is not Palindrome")
	