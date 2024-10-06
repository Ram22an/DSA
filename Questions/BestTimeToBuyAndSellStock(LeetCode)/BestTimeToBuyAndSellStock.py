prices = list(map(int, input().strip().split()))
MinNum=prices[0]
Profit=0
for i in range(len(prices)):
    Profit=max(Profit,prices[i]-MinNum)
    MinNum=min(MinNum,prices[i])
print(Profit)
