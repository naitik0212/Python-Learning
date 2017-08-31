    seq=['Naitik','Kevin','Rohit','Sangeeta']
    
     j=1
    
     for i in seq:
     print (i)
    
      print("Family member {}: ".format(j) +i )
      j=j+1



 def myfuncofsum(n):
     sum=0
     for i in range(0,n):
         sum= sum+i

     print (sum)

 myfuncofsum(5)


 list=[1,2,3,4,5]

 def myfuncofsum(n):
     sum=0
          for i in n:
          sum= sum+i

     print (sum)

 myfuncofsum(list)


def square(num):
     return num**2
print(square(2))


l=[1,2,3,4,5]
print(list(map(square,l)))

l=[1,2,3,4,5]
print(list(map(lambda num:num**2,l)))

print(list(filter(lambda n: n%2 ==1,l)))

# upper
# lower
# split

list=[1,2,3,4]
list.pop(1)
print(list)

# 7 to the power of 4
print (7**4)

s="hi there dad!"

print (list(s.split()))

planet = "Earth"

name = "I can't go"
num = 12
name = "Naitik"
print("Hello! My name is {one} and roll no. is {two},more {one}".format(one=name,two= num))
s="hello"

print (s[0])

my_list = ['Hi','wassup','?',["Wassup", "4"]]

print (my_list[3][0])

