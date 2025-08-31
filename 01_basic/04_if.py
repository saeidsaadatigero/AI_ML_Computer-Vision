score = int(input("Inter number: "))

if 10 <= score <= 20:
    print("Success")
elif score in range(0, 10):
    print("Try more and read")    
else:
    print("Nice: Code is work")
    