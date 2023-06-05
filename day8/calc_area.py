import math
def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil((height*width)/cover)} cans of paint.")
# math.ceil is used to round up a number!
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

