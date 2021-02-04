import graphics.rectangle
print("Rectangle")
l=int(input("enter the lenght:"))
b=int(input("enter the breadth:"))
print("Area of rectangle:",graphics.rectangle.area(l,b))
print("Perimeter of rectangle:",graphics.rectangle.perimeter(l,b))

from graphics.circle import area
from graphics.circle import perimeter as p
print("circle")
r=int(input("enter the radius:"))
print("Area of circle:",area(r))
print("Perimeter of circle:",p(r))


from graphics.dgraphics.cuboid import area as a
from graphics.dgraphics.cuboid import perimeter as p
print("Cuboid")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
print("Total surface area:",a(l,b,h))
print("Perimeter of cuboid:",p(l,b,h))


from graphics.dgraphics.sphere import *
print("Sphere")
r=int(input("enter the radius"))
print("Surface area:",area(r))
print("Circumference:",circumference(r))
