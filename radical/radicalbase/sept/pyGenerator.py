list1=[1,2,3,4,5,6]

def gen(object):
    for i in object:
        yield(i)

x=gen(list1)
print(x.__next__())
# print(x.__next__())

y=[i for i in x]
print(y)


print("------")
print(list1)


# + : addition

num1=10
num2=20

print(num1+num2)

fname='Shubham'
lname='Kumar'

print(fname+lname)

class animal():
    def color(self,a):
        print("Black")
    def color(self,a, sal):
        print("Red")

a=animal()

a.color(4,5)


public void test(params)
public int test(params)
public float test(params)
- return type overloading

-no. of arguments
public void test(param1)
public void test(param1,param2)
public void test(param1,param2,param3)

-type of arguments
public void test(String[] param1)
public void test(int[] param1)
public void test(float[] param1)