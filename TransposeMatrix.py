list1=[[1,2],[1,4]]
list2=[[0,0],[0,0]]
for i in range (0,2):
	for j in range(0,2):
		list2[i][j]=list1[j][i]	
print(list1)		
print(list2)		
