# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]

# result=[]

# l=len(l1)

# for i in range(l):
#  # for i in range(len(l2)):
#     result.append(l1[i]+l2[i]);

# print(result)


l1=[]
l2=[]
size=int(input())

for i in range(size):
  x=int(input())
  l1.append(x)

for i in range(size):
  y=int(input())
  l2.append(y)

result=[]
for j in range(size):
  suum=l1[j]+l2[j]
  result.append(suum)
  #result.append(l1[j]+l2[j])

print(result)