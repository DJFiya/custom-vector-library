from vector import Vector

def main():
    """Main function to execute the script."""
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Are they equal? {v1 == v2}")
    print(f"Vector 1 magnitude: {v1.magnitude}")
    print(f"Vector 2 direction: {v2.direction}")
    print(f"Vector 1 dimension: {v1.dimension}")
    print(f"Vector 1 < Vector 2: {v1 < v2}")
    print(f"Vector 1 > Vector 2: {v1 > v2}")
    print(f"<1, 2> is truthy: {bool(Vector([1, 2]))}")
    print(f"<0, 0> is truthy: {bool(Vector([0, 0]))}")
    print(f"Vector 1 as string: {str(v1)}")
    print(f"Vector 2 as repr: {repr(v2)}")
    print(f"Vector 1 format 2f: {v1:.2f}")

if __name__ == "__main__":
    main()