# Mathematical Vectors Library

A Python library implementing a fully-featured mathematical vector class using Python's dunder (magic) methods. This library is designed for intuitive and Pythonic manipulation of vectors, supporting comparison, type conversion, and more.

## Features

- Vector creation from lists of numbers
- Magnitude and direction (unit vector) calculation
- Dimension property
- Equality and comparison operations (`==`, `<`, `>`, etc.)
- Type conversions (`int`, `float`, `complex`, `str`, `repr`)
- Truthiness checks
- Formatted string output

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
```

## Running the Example

Run the included `main.py` to see the vector class in action:

```bash
python main.py
```

## Future Plans

- Implement arithmetic operations (`+`, `-`, `*`, etc.)
- Add support for more vector operations (dot product, cross product)
- Provide a CLI interface for vector operations via command line
- Explore more class functionality to make this a proper class ie. custom exceptions.
