def CanPlaceCow(Arr,mid,Cows):
	CurrentCow=1
	LastCow=Arr[0]
	for i in Arr:
		if i-LastCow>=mid:
			CurrentCow+=1
			LastCow=i
			if CurrentCow>=Cows:
				return True
	return False
TestCases=int(input())
for i in range(TestCases):
	N,C=map(int,input().split())
	Nums=[]
	for i in range(N):
		temp=int(input())
		if i==0:
			Nums.append(temp)
		else:
			Nums.append(temp)
			if Nums[-2]>Nums[-1]:
				temp2=Nums[-2]
				Nums[-2]=Nums[-1]
				Nums[-1]=temp2
	Left=1
	Right=Nums[-1]
	Ans=-1
	while Left<=Right:
		mid=(Left+Right)//2
		if CanPlaceCow(Nums,mid,C):
			Ans=mid
			Left=mid+1
		else:
			Right=mid-1
	print(Ans)
