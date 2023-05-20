tuple=("disco",10,1.2)
print(tuple[0])
print(tuple[1])
print(tuple[-1])
a=(4,5,2.2,4.5,8)
print(sorted(a))
b=("Milk",1.2,("Galon","FUel"),10,5.5,("Sugar","water"))
print(b[2][1])
print(b[5][0])
l=[12,4.5,["Milk","sugar"],("green","red"),90]
print(l[3][1])
l.extend(["black",80])
l[0]="Oil"
print(l)
A="Hello World"
print(A.split())
A=["Gree,Black,White,Brown,Red"]
B=A[:]
print(B)
A[0]="Orange"
print(A)


import matplotlib.pyplot as plt

class circle(object):
    def  _init_(self,radius = 3,color='blue'):  
        self.radius = radius
        self.color = color
    def add_radius(self,r):
        self.radius =self.radius + r
        return(self.radius)
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()         