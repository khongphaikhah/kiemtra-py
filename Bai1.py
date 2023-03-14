import random

def generate_input_file(filename, num_shapes):
    shapes = ["#Rect", "#Circle", "#Triangle"]
    with open(filename,"w" ) as file:
        for i in range(num_shapes):
            shape = random.choice(shapes)
            file.write(shape + "\n")
            if shape == "#Rect":
                rong = random.randint(1, 10)
                dai = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(rong) + " " + str(dai) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Circle":
                bankinh = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(bankinh) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Triangle":
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(a) + " " + str(b) + " " + str(c) + "\n")
                file.write(str(x) + " " + str(y) + "\n")

generate_input_file("D:\\Python\\Kiemtra\input.txt",10)    
