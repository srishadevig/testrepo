list1=['physics','chemistry',2000,1999]
list2=[1,2,3,4,5,6]

print(list1)
print(list2)

print(list1[1])
print(list2[1])

print(list2[1:4])

list1[2]=2001

print(list1[2])

del list1[2]

tup=('physics','chemistry',2000,1999)
tup1=(1,2,3,4,5,6,7)
print(tup)
print(tup1)

print(tup[1])
print(tup[2])

print(tup1[0])
print(tup[2])
print(tup1[1:5])

del tup1   #it will delete tuple1

dict={'Name':"Zara",'Age':7,'Class':'First'}

print(dict)
print(dict['Name'])
print(dict['Age'])

dict['Age']=8
dict['School']="DPS"

print(dict)
