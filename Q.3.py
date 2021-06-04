def func(zip):
    n = int(input("Enter no. of tests: ")) 
    Alice_mark = list(map(int,input("\nEnter Alice scores: ").strip().split()))
    Bob_mark = list(map(int,input("\nEnter Bob scores: ").strip().split()))
    print("\nAlice marks are: ",Alice_mark) 
    print("\nBob marks are: ",Bob_mark) 
    i=0
    j=0
    for l1,l2 in zip(Alice_mark,Bob_mark):
        if l1 < l2:
            
            j+=1
        elif l1 > l2:
            
            i+=1
        
    print("Alice",i)
    print("Bob",j)
   
    if i>j:
        print("Alice won the competition")   
    elif i<j:
        print("Bob won the competition")
print(func(zip))
 

