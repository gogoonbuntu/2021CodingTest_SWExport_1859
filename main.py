N = int(input())
print("N",N)
PROFIT = 0
for i in range(N):
	K = int(input())
	print("K",K)
	PRICES = list(map(int, input().split()))
	print("P",PRICES)
	MAX_PRICE_INDEX = len(PRICES)-1
	BOUGHT_STOCK = []
	for j in reversed(range(K)):
		if PRICES[j] >= PRICES[MAX_PRICE_INDEX]:
			if len(BOUGHT_STOCK)>0:
				for a in BOUGHT_STOCK:
					print("SELL",a," ON PRICE ",PRICES[MAX_PRICE_INDEX])
					PROFIT += PRICES[MAX_PRICE_INDEX]-a
			MAX_PRICE_INDEX = j
			BOUGHT_STOCK = []
		else :
			BOUGHT_STOCK.append(PRICES[j])
			print("BUY",PRICES[j])
	if len(BOUGHT_STOCK)>0:
				for a in BOUGHT_STOCK:
					print("SELL",a," ON PRICE ",PRICES[MAX_PRICE_INDEX])
					PROFIT += PRICES[MAX_PRICE_INDEX]-a

print(PROFIT)
				
			