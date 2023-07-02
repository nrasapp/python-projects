from math import sqrt

print("Rectangle Calculator by NRAS App\n")

def diagonal():
    diagonal = sqrt(side_length_a ** 2 + side_length_b ** 2)
    print("Diagonal:", diagonal)

def perimeter():
    perimeter = side_length_a * 2 + side_length_b * 2
    print("Perimeter:", perimeter)

def area():
    area = side_length_a * side_length_b
    print("Area:", area)

while True:
    side_length_a = int(input("Side length A: "))
    side_length_b = int(input("Side length B: "))
    print("\nResults:\n")
    diagonal()
    perimeter()
    area()
    ctn = input("\nDo you want to continue? (y/n): ")
    if ctn == "n" or ctn == "N":
        print("Thank you")
        break