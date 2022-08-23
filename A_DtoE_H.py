a=input("Enter a string ")
K=int(input("Enter key value ")) 
print("The cipher text is ")
E=''
for i in a:
    c=ord(i)
    b=c+K
    P=chr(b)
    E=E+P
print(E)
F=''
print("The plain code is ")    
for j in E:
    d=ord(j)
    e=d-K
    p=chr(e)
    F=F+p
print(F)
