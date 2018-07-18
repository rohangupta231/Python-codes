list1=[[1,0],[0,1]]
list2=[[2,2],[2,2]]
list3=[[0,0],[0,0]]
for i in range (0,2):
	for j in range(0,2):
		sum=0
		for k in range(0,2):
			sum=sum+list1[i][k]*list2[k][j]
		list3[i][j]=sum
print(list3)		
