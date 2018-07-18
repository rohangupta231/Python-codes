list1=[[1,1],[1,1]]
list2=[[1,2],[1,2]]
list3=[[0,0],[0,0]]
count=0
for i in range (0,2):
	for j in range(0,2):
		if list1[i][j]==list2[i][j]:
			count=count+1
print(count,"are the number of matching corresponding elements")		
