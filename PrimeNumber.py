n=21
flag=0
for i in range(2,int(n/2)):
	if (n%i==0):
		flag=1
		break
	#print("Number is Prime")
if(flag==0):
	print("Number is Prime")
else:
	print("Number is composite")	

		