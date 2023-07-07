# class A:
#     x=10
#     y=10
#
#     def add(self):
#         print(self.x+self.y)
#
#
# class B(A):
#     x=10
#     y=15
#     def add(self):
#         print(A.x-A.y)
#         super().add()
#
# b=B()
# b.add()
#

class A:
    name="Snail"

class B(A):
    name="Sjail"

b=B
print(b.name)
a=A
print(a.name)