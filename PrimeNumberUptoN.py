N=int(input("How many first N prime numbers you want"))
k=1
i=2
while k<=N:
	j=2
	flag=0
	while((j<=i//2)):
		if i%j==0:
			flag=1
			break
		j=j+1
	if flag==0:
		print(i," ")
		k=k+1
	i=i+1	