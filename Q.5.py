def BookList():
    list1 = []
    list2 = []
    list3 = []
    n = int(input("Enter no. of books: "))
    print('\n')
    for i in range(0,n):
        a=int(input(f'Enter no. of pages of book {i+1} : '))
        list1.append(a)
        
        b=int(input(f'Enter price of book {i+1} : '))
        list2.append(b)

        c=int(input(f'Enter chapter of book {i+1} : '))
        list3.append(c)
        print('\n')
        
    for i in range(0,n):
        print(f"Book No.:{i} ","Page No.:",list1[i],"Price :",list2[i] ,"Chapter:",list3[i])

    print('\n')
    for i in range(0,3):
        att = int(input('Enter Selected attribute: '))
        if att==1:
            print('Pages List:' , list1)
        elif att==2:
            print('Price List:' , list2)
        elif att==3:
            print('Chapter List:' , list3)

if __name__== "__main__":
    BookList()

    
        



    
