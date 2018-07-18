list1=[[1,0],[0,1]]
count=0
flag=0
flag1=0
flag2=0
for i in range (0,2):
	for j in range(0,2):
		if i==j:
			if list1[i][j]==1:
				flag1=1
		if i!=j:
			if list1[i][j]==0:
				flag2=1
if flag1==1:
	if flag2==1:
		flag=1
if flag==1:
	print("Matrix is identity")
else:
	print("Matrix is not Identity")
