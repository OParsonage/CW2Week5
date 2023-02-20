# writing a code to find the volume and surface areas of a cylinder
import math as math

def volumecyl(r,h):
    return (1/3)*math.pi*r**2*h

def surfaceAreacyl(r,h):
    return math.pi*r*(r+math.sqrt(h**2+r**2))

def volumesphere(r):
    return (4/3)*math.pi*r**3

def surfaceAreasphere(r):
    return 4*math.pi*r**2

def volumeprysm(r,h):
    return math.pi*r**2*h

def surfaceAreaprysm(r,h):
    return 2*math.pi*r*(r+math.sqrt(h**2+r**2))

def main():
    shape = input("Enter the shape: ")
    if shape == "cylinder":
        h = float(input("Enter the height: "))
        r = float(input("Enter the radius: "))
        volume = volumecyl(r,h)
        surfaceArea = surfaceAreacyl(r,h)
    elif shape == "sphere":
        r = float(input("Enter the radius: "))
        volume = volumesphere(r)
        surfaceArea = surfaceAreasphere(r)
    elif shape == "prism":
        r = float(input("Enter the width: "))
        h = float(input("Enter the height: "))
        volume = volumeprysm(r,h)
        surfaceArea = surfaceAreaprysm(r,h)
    else:
        print("Invalid shape")
        return
    print("The volume is: ", volume)
    print("The surface area is: ", surfaceArea)

main()
