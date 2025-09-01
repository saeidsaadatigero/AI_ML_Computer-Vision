numbers = [2, 4, 6]
for x in numbers:
    print(x)
print("finish")
    
for i in range(3):
    print(i)
print("finish")

for a in range(1, 10, 2):
    print(a)
    
list_1 = ["a", "b", "c"]
for s, d in enumerate(list_1):
    print(s, d)
    
names = ["saeid", "hasti"]
score = [12, 18]
for n, s in zip(names, score):
    print(n, s)
    
info = {"age":37.5, "hight":1.98}
for k, v in info.items():
    print(k, v)
    
for c in range (10):
    if c == 5:
        break
    
    if c % 2 == 0:
        continue
    print(c)
    
j = 0
while j < 10:
    print(j)
    j += 1
    
    
    