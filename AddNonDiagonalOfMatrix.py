list1=[[1,1],[1,1]]
list2=[[2,2],[2,2]]
list3=[[0,0],[0,0]]
for i in range (0,2):
	for j in range(0,2):
		if(i!=j):
			list3[i][j]=list1[i][j]+list2[i][j]
print(list3)		
