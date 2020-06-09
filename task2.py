#cuboid project Nathan Wagstaff Calculate the area and volume of any cuboid!


#intro
print("Please enter values in feet.")
print()

#length
length = eval(input("Enter the length: "))
print()

#width
width = eval(input("Enter the width: "))
print()

#height
height = eval(input("Enter the height: "))
print()

#surface area
surfaceArea = 2*(length*width) + 2*(height*length) + 2*(height*width)


#area
area = (length*width*height)


#solution
print(f"Your {length} X {width} X {height} has a volume of {area} and a surface area of {surfaceArea}")