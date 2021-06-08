def chocolate():
    priceList = []
    i=0
    m=0
    n = int(input("Enter no. of chocolates: "))
    total = int(input("Enter total Money: "))

    for i in range(0,n):
        choco = int(input(f"Enter price of choco{i+1}: "))
        priceList.append(choco)
    print('\n')

    for i in range(0,(len(priceList))-1):
        sum= priceList[i] + priceList[i+1]
        if(total==sum):
            print(f"two chocolate you bought of price: {priceList[i]} and {priceList[i+1]}.")
            break
        else:
            print("u cant buy chocolate.")
if __name__=="__main__":
    chocolate()
