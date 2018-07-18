num=int(input("Enter a number"))
flag0=flag1=flag2=flag3=flag4=flag5=flag6=flag7=flag8=flag9=0
while num!=0:
	digit=num%10
	if digit==0:
		flag0=1+flag0
	elif digit==1:
		flag1=1+flag1
	elif digit==2:
		flag2=1+flag2
	elif digit==3:
		flag3=1+flag3
	elif digit==4:
		flag4=1+flag4
	elif digit==5:
		flag5=1+flag5
	elif digit==6:
		flag6=1+flag6
	elif digit==7:
		flag7=1+flag7
	elif digit==8:
		flag8=1+flag8
	elif digit==9: 
		flag9=1+flag9
	num=num//10	
print("'0' =",flag0,"times")		
print("'1' =",flag1,"times")	
print("'2' =",flag2,"times")	
print("'3' =",flag3,"times")	
print("'4' =",flag4,"times")	
print("'5' =",flag5,"times")	
print("'6' =",flag6,"times")	
print("'7' =",flag7,"times")	
print("'8' =",flag8,"times")	
print("'9' =",flag9,"times")	