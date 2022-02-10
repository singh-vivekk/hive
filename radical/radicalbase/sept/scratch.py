data='123456'

sum=0

# [(sum+int(i)) for i in data]
# print(sum)

for i in data:
    sum+=int(i)
print(sum)