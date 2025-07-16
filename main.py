from vector import Vector

def main():
    """Main function to execute the script."""
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([0, 0, 0])
    v4 = Vector([7, 8])
    v5 = Vector([1, 2])

    print("=== Construction and Properties ===")
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v3 (zero): {v3}")
    print(f"v4 (2D): {v4}")
    print(f"v1 magnitude: {v1.magnitude}")
    print(f"v2 direction: {v2.direction}")
    print(f"v1 dimension: {v1.dimension}")

    print("\n=== Comparison Operations ===")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 != v2: {v1 != v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"v1 <= v2: {v1 <= v2}")
    print(f"v1 > v2: {v1 > v2}")
    print(f"v1 >= v2: {v1 >= v2}")

    print("\n=== Type Conversion Methods ===")
    print(f"repr(v1): {repr(v1)}")
    print(f"str(v2): {str(v2)}")
    print(f"bool(v1): {bool(v1)}")
    print(f"bool(v3): {bool(v3)}")
    print(f"int(v1): {int(v1)}")
    print(f"float(v2): {float(v2)}")
    print(f"v1 formatted (.2f): {v1:.2f}")
    try:
        print(f"complex(v4): {complex(v4)}")
    except Exception as e:
        print(f"complex(v4) error: {e}")

    print("\n=== Container Methods ===")
    print(f"len(v1): {len(v1)}")
    print(f"Iterating v1: {[x for x in v1]}")
    print(f"v1[0]: {v1[0]}")
    print(f"v1[10] (out of bounds): {v1[10]}")
    v1[1] = 10
    print(f"v1 after setting index 1 to 10: {v1}")

    print("\n=== Arithmetic Operations ===")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 2: {v1 * 2}")
    print(f"v1 ** v2 (dot product): {v1 ** v2}")
    print(f"v1 @ v2 (cross product): {v1 @ v2}")
    print(f"-v1: {-v1}")
    print(f"+v1: {+v1}")

    print("\n=== In-place Operations ===")
    v6 = Vector([1, 2, 3])
    v6 += Vector([1, 1, 1])
    print(f"v6 after += [1,1,1]: {v6}")
    v6 -= Vector([1, 0, 1])
    print(f"v6 after -= [1,0,1]: {v6}")
    v6 *= 2
    print(f"v6 after *= 2: {v6}")

    print("\n=== Error Handling ===")
    try:
        print(v1 / v2)
    except Exception as e:
        print(f"Division error: {e}")
    try:
        print(v1 // v2)
    except Exception as e:
        print(f"Floor division error: {e}")
    try:
        print(v1 % v2)
    except Exception as e:
        print(f"Modulus error: {e}")
    try:
        print(bytes(v1))
    except Exception as e:
        print(f"bytes error: {e}")

if __name__ == "__main__":
    main()