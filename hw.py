num = int(input("Enter the number: "))
rev = 0

while num != 0:
    c = num % 10         
    rev = rev * 10 + c   
    num = num // 10     

print("Reverse order of the number is:", rev)
