def function(s):
    u=''
    l=''
    d=''
    count=0
    special=''
    for i in s:
        if i.isupper():
            u+=i
        elif i.islower():
            l+=i
        elif i.isdigit():
            d+=i
        elif i==' ':
            count+=1
        else:
            special+=i

    result = special+l+' '+u+' '+d+' '+str(count)
    return result
 
print(function('131/265 is where I and Sam Live.'))

