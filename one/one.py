def Decode(s):  
    return DecodeRec(s,len(s));  
  
def DecodeRec(s, n):  
    if s == "0": 
        return 0
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] > "0":  
        count = DecodeRec(s,n-1)  
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :  
        count += DecodeRec(s, n - 2)  
    return count  
          
digits = input();
print(Decode(digits))  