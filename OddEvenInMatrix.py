list1=[[1,1],[1,4]]
list_even=[]
list_odd=[]
for i in range (0,2):
	for j in range(0,2):
		if(list1[i][j]%2==0):
			list_even.append(list1[i][j])
		elif(list1[i][j]%2!=0):
			list_odd.append(list1[i][j])	
print(list_even," Are Even Numbers")
print(list_odd," Are odd Numbers")		
