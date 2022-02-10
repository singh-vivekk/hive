# Python program to show the order
# in which methods are resolved:
# MRO - Method Resolution Order

class A:
	def rk(self):
		print(" In class A")
class B:
	def rk(self):
		print(" In class B")

# classes ordering
class C(A, B):
	def __init__(self):
		print("Constructor C")

# classes ordering
class D(B, A):
	def __init__(self):
		print("Constructor D")

r = C()

# it prints the lookup order
print(C.__mro__)
print(C.mro())

# it prints the lookup order
print(D.__mro__)
print(D.mro())
