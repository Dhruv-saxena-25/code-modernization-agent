# main.py

from math_utils import add, subtract, multiply, divide

def main():
    x = 10
    y = 5

    print(f"Adding {x} and {y}: {add(x, y)}")
    print(f"Subtracting {y} from {x}: {subtract(x, y)}")
    print(f"Multiplying {x} and {y}: {multiply(x, y)}")
    try:
        print(f"Dividing {x} by {y}: {divide(x, y)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
