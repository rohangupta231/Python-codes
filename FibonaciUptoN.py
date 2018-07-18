num=int(input("Enter a Number"))
FT=0
ST=1
NT=0
print("0")
print("1")
while(NT<num):
	NT=FT+ST
	FT=ST
	ST=NT
	print(NT," ")