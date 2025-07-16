# Mathematical Vectors Library

A Python library implementing a fully-featured mathematical vector class using Python's dunder (magic) methods. This library is designed for intuitive and Pythonic manipulation of vectors, supporting comparison, arithmetic, type conversion, and more.

## Features

- Vector creation from lists of numbers
- Magnitude and direction (unit vector) calculation
- Dimension property
- Equality and comparison operations (`==`, `<`, `>`, etc.)
- Arithmetic operations (`+`, `-`, `*`, unary `-`, unary `+`)
- Dot product (`**`) and cross product (`@`)
- In-place arithmetic (`+=`, `-=`, `*=`)
- Type conversions (`int`, `float`, `complex`, `str`, `repr`)
- Truthiness checks
- Formatted string output
- Container methods (`len`, iteration, indexing, assignment)
- Error handling for unsupported operations

## Example Usage

```python
from vector import Vector

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(f"Vector 1: {v1}")                  # <1.0, 2.0, 3.0>
print(f"Vector 2: {v2}")                  # <4.0, 5.0, 6.0>
print(f"Are they equal? {v1 == v2}")      # False
print(f"Vector 1 magnitude: {v1.magnitude}")  # 3.7416573867739413
print(f"Vector 2 direction: {v2.direction}")  # <0.455..., 0.569..., 0.683...>
print(f"Vector 1 dimension: {v1.dimension}")  # 3
print(f"Vector 1 < Vector 2: {v1 < v2}")      # True
print(f"Vector 1 > Vector 2: {v1 > v2}")      # False
print(f"<1, 2> is truthy: {bool(Vector([1, 2]))}")  # True
print(f"<0, 0> is truthy: {bool(Vector([0, 0]))}")  # False
print(f"Vector 1 as string: {str(v1)}")       # <1.0, 2.0, 3.0>
print(f"Vector 2 as repr: {repr(v2)}")        # Vector(4.0, 5.0, 6.0)
print(f"Vector 1 format 2f: {v1:.2f}")        # <1.00, 2.00, 3.00>
print(f"v1 + v2: {v1 + v2}")                  # <5.0, 7.0, 9.0>
print(f"v1 - v2: {v1 - v2}")                  # <-3.0, -3.0, -3.0>
print(f"v1 * 2: {v1 * 2}")                    # <2.0, 4.0, 6.0>
print(f"v1 ** v2 (dot product): {v1 ** v2}")  # 32.0
print(f"v1 @ v2 (cross product): {v1 @ v2}")  # <-3.0, 6.0, -3.0>
print(f"-v1: {-v1}")                          # <-1.0, -2.0, -3.0>
print(f"+v1: {+v1}")                          # <1.0, 2.0, 3.0>
```

## Running the Example

Run the included `main.py` to see the vector class in action and test all features:

```bash
python main.py
```

## Future Plans

- Provide a CLI interface for vector operations via command line
- Explore more class functionality to make this a proper class ie. custom exceptions.
