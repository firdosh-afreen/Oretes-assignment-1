def function(str):
    upper = ''
    lower = ''
    digit = ''
    count = 0
    special = ''

    for i in range(len(str)):
        if (str[i].isdigit()):
            digit = digit+ str[i]
        elif (str[i] >= 'A' and str[i] <= 'Z'):
            upper += str[i]
        elif (str[i] >= 'a' and str[i] <= 'z'):
            lower += str[i]
        elif (str[i]==" "):
            count += 1
        else:
            special += str[i]

    print(f'Output: {special} {lower} {upper} {digit} {count} ')
 
if __name__ == "__main__":
    str = "131/265 is where I and Sam Live."
    function(str)

