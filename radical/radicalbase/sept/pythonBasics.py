
a ="Sachin"
b=10

print(type(a))

print(id(a))
print(id(b))

print(a,":",b)
a,b=b,a+b

print(a,":",b)

#
# schema=' gfoprsnd_reporting '
# print(schema)
# schema=schema.strip().lower()
# print(schema)

# This is a setup script
# to check if python is working or not
# string : '<>'
# "<>"
# '''<>'''

# print('Ram\'s  Car')
# print("Ram's  Car")
# print("""Ram's  Car""")

# docstring: document docstring

# help(print)

# Method:

# def printName():
#     print(">> first line in method printName")
#
#
#     print(">> second line in method printName")
#
# print("outer to method line")
#
#
# printName()
# printName()

# --------------------------------------------------
# def printName(name, age, location="Mumbai"):
#     print(">> method printName <<")
#     print(f">> name passed in the method is, {name} , age is {age},  and address is {location}  <<")
#     # print(">> name passed in the method is, {0}   <<".format(name))
#
#
# printName("vivek",30, "Pune")
# printName("Nikhil", 22)
# # printName("Sachin")

# variable no. of args:
# args : Args  *
# kwargs : KV

# def pySum(a,*b):
#     print(a)
#     print(b)
#     x=0
#     for i in b:
#         x=x+i
#     print("Sum is : ", x+a)
#
# # pySum(1,45,343,54)
#
# def pySum1(a,*b):
#
#     print("first number is :", a, " \nsecond number is : ",b)



# pySum1(1,2,354,34,23,23,2354,45,23)-
#
# print([i for i in range(10,100,5)])


# range: 3 positional
# 1. start position... default to 0
# 2. end position:
# 3. step. -  by default to 1

#  Args: variable no. of arguments . *
# collection datatypes:
#
# tablename,
# tablename, schemaname, partitions
#
# **Kwargs - Keyword arguments
#
# kwargs
# name:"vivek", age:30, location:"Pune"


# def kwmethod(a, **details):
#     print(a)
#     # cust_name=details['name']
#     # print(details.split(','))
#     for k,v in details.items():
#         print(k,":",v.strip())
#         # print(k, ":", v)
#     # print(f"Select * from {details['schemaname']}.{details['tablename']} ")
#
# kwmethod(12,name="Vivek ",location="Bangalore            ",tablename="student",schemaname="radical", company='LTI')

# create a method getQuery,
#  print(query)
#
#  we are passing, dbname, tablename and filter conditions
#
#
# select * from radical.employee where
# age='',
# location=''
# unique_id=''
#
# input would be  - getQuery(radical, employee, keys, values)
#
# over key iterate


def getQuery(dbname, tblnm, *abc, **xyz):
    wherecondition='';

    print(xyz["country"])
    # print(abc[1])
    # for k, v in kwargs.items():
        # print(k,v)

    for i in abc:
        print(i)

    print(wherecondition)

    # len(abc) :  3
    print(range(3))

    for i in range(3):
        print(i)

    # query=(f'''select * from {dbname}.{tblnm} where {whereconditions}''')
    # print(query)

getQuery("devschema","employee", 15,18, 'nikhil', id=14, name="sachin", address="Pune", state="Pune", country="India", states=19)



