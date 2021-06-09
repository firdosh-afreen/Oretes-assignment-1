words=[]
def func(str):
    str = str.split()		
    str1 = []

    for i in str:
        if i not in str1:
            str1.append(i)
			
    for i in range(0, len(str1)):
        print( str1[i], '',len(str1[i]),'', str.count(str1[i]))	

n = int(input("Enter no. of words: "))
for i in range(0, n): 
        a = input(f'Enter word no. {i+1} : ')
        words.append(a)

print('\n')

def main():
	str ='New Old Existing New New '
	func(str)					

if __name__=="__main__":
	main()		
