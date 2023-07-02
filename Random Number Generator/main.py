from random import randint

print("Random Number Generator by NRAS App\n")

def random_number_generator():
    random_number = randint(min, max)
    print("Random Number:", random_number)

while True:
    min = int(input("Min: "))
    max = int(input("Max: "))
    print("\nResults:\n")
    random_number_generator()
    ctn = input("\nDo you want to continue? (y/n): ")
    if ctn == "n" or ctn == "N":
        print("Thank you")
        break