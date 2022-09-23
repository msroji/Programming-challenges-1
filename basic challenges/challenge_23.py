def userinput():
    length = float(input("Enter the length of the garden in metres: "))
    width = float(input("Enter the width of the garden in metres: "))
    radius = float(input("Enter the radius of the circular flower bed in meters: "))
    return length,width,radius

def flower_bed(radius):
    return (radius**2)*3.14

def garden(length,width):
    return length * width

if __name__ == "__main__":
    length,width,radius = userinput()
    circle_area = flower_bed(radius)
    garden_area = garden()
    turf_needed = garden_area-circle_area
    print(f"{turf_needed} metres")
