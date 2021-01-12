def grayCodeUtil(result, numOfBits, num): 
    if (numOfBits == 0): 
        result.append(num[0]) 
        return
    grayCodeUtil(result, numOfBits - 1, num) 
    num[0] = num[0] ^ (1 << (numOfBits - 1))  
    grayCodeUtil(result, numOfBits - 1, num)  
def grayCode(numOfBits): 
    result = [] 
    num = [0] 
    grayCodeUtil(result, numOfBits, num)  
    return result  
 
numOfBits=int(input());
code = grayCode(numOfBits) 
x=[]
for i in range(len(code)): 
    x.append(code[i]);
print(x);