num=int(input("Enter a number"))
num_digit=0
num1=temp=num
namst=0
digit=0
while(num>0):
	num_digit=num_digit+1
	num=num//10
while(temp>0):
	digit=temp%10
	temp=temp//10
	#print(digit)
	namst=namst+pow(digit,num_digit)
	#print(namst)
if(num1==namst):
	print(num1,"It is Amstrong number")
else:
	print("It is not Amstrong number")	
	