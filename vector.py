"""A full implementation of a Vector class with operations."""
from typing import Self

class Vector:
    def __init__(
            self,
            val_list : list[float | int] = [0]
    ):
        self._vector = [float(v) for v in val_list]

    # Vector instance properties
    @property
    def magnitude(self) -> float:
        """Calculate the magnitude of the vector."""
        return sum(x ** 2 for x in self._vector) ** 0.5
    
    @property
    def direction(self) -> Self:
        """Return the direction of the vector as a unit vector."""
        mag = self.magnitude
        if mag == 0:
            return Vector([0] * self.size)
        return Vector([x / mag for x in self._vector])
    
    @property
    def dimension(self) -> int:
        """Return the dimension of the vector. Also accessible as len(v)."""
        return len(self._vector)
    
    # Comparison operations + adjacent methods
    def __eq__(self, other: object) -> bool:
        """Check if two vectors are equal."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self._vector == other._vector
    
    def __ne__(self, other: object) -> bool:
        """Check if two vectors are not equal."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self._vector != other._vector
    
    __hash__ = None  # Vectors are mutable, so they are not hashable.

    def __lt__(self, other: object) -> bool:
        """Check if this vector's magnitude is less than another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude < other.magnitude
    
    def __le__(self, other: object) -> bool:
        """Check if this vector's magnitude is less than or equal to another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude <= other.magnitude
    
    def __gt__(self, other: object) -> bool:
        """Check if this vector's magnitude is greater than another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude > other.magnitude
    
    def __ge__(self, other: object) -> bool:
        """Check if this vector's magnitude is greater than or equal to another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude >= other.magnitude
    
    # Type conversion methods
    def __repr__(self) -> str:
        """Return a string representation of the vector."""
        return f"Vector([{", ".join(str(x) for x in self._vector)}])"
    
    def __str__(self) -> str:
        """Return a string representation of the vector for printing."""
        return f"<{', '.join(str(x) for x in self._vector)}>"
    
    def __bool__(self) -> bool:
        """Return True if the vector is non-zero, False otherwise."""
        return any(x != 0 for x in self._vector)
    
    def __int__(self) -> int:
        """Return the integer representation of the vector's magnitude."""
        return int(self.magnitude)
    
    def __float__(self) -> float:
        """Return the float representation of the vector's magnitude."""
        return self.magnitude
    
    __bytes__ = None  # Vectors do not have a byte representation.

    def __complex__(self) -> complex:
        """Return the complex representation of the vector if 2d."""
        if self.dimension != 2:
            raise ValueError("Complex representation is only valid for 2D vectors.")
        return complex(self[0], self[1])
    
    def __format__(self, format_spec: str) -> str:
        """Return a formatted string representation of the vector."""
        return f"<{', '.join(f'{x:{format_spec}}' for x in self._vector)}>"
    
    # Container methods
    def __len__(self) -> int:
        """Return the number of dimensions in the vector."""
        return self.dimension
    
    def __iter__(self) -> iter:
        """Return an iterator over the vector's components."""
        return iter(self._vector)
    
    def __getitem__(self, index: int) -> float:
        """Return the component at the specified index."""
        if index < 0:
            raise IndexError("Index out of vector range.")
        if index >= self.dimension:
            return 0.0
        return self._vector[index]
    
    def __setitem__(self, index: int, value: float | int) -> None:
        """Set the component at the specified index to a new value."""
        if index < 0:
            raise IndexError("Index out of vector range.")
        if index >= self.dimension:
            for i in range(self.dimension, index + 1):
                self._vector.append(0.0)
        self._vector[index] = float(value)

    # Arithmetic operations
    def __add__(self, other: object) -> Self:
        """Add two vectors."""
        if not isinstance(other, Vector):
            return NotImplemented
        result = Vector(self._vector if self.dimension >= other.dimension else other._vector)
        for i in range(max(self.dimension, other.dimension)):
            result[i] = self[i] + other[i]
        return result
    
    def __mul__(self, other: object) -> float:
        """Dot product the vector by a scalar or vector."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vector([x * other for x in self._vector])
        
    def __pow__(self, other: object) -> float:
        """Dot product the vector by a vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return sum([self[i] * other[i] for i in range(
            min(self.dimension, other.dimension)
        )])
    
    def __matmul__(self, other: object) -> Self:
        """Cross product with another vector (only for 3D vectors)."""
        if not isinstance(other, Vector):
            return NotImplemented
        max_dim = max(self.dimension, other.dimension)
        dim = 3 if max_dim <= 3 else None  # Only supports 3D cross product.
        if not dim:
            return NotImplemented
        return Vector([
            self[1] * other[2] - self[2] * other[1],
            self[2] * other[0] - self[0] * other[2],
            self[0] * other[1] - self[1] * other[0]
        ])
    
    def __sub__(self, other: object) -> Self:
        """Subtract two vectors."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self + (-other)
    
    def __div__(self, other: object) -> Self:
        """Division of the vector by a scalar."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Vector([x / other for x in self._vector])
    
    def __truediv__(self, other: object) -> Self:
        """True division of the vector by a scalar."""
        return self.__div__(other)

    def __neg__(self) -> Self:
        """Return the negation of the vector."""
        return self * -1.0
    
    def __pos__(self) -> Self: return self  # Unary plus does not change the vector.

    __truediv__ = None  # Division is not defined for vectors.
    __floordiv__ = None  # Floor division is not defined for vectors.
    __mod__ = None  # Modulus is not defined for vectors.

    # In-place operations
    def __iadd__(self, other: object) -> Self:
        """In-place addition of two vectors."""
        if not isinstance(other, Vector):
            return NotImplemented
        for i in range(max(self.dimension, other.dimension)):
            self[i] += other[i]
        return self
    
    def __isub__(self, other: object) -> Self:
        """In-place subtraction of two vectors."""
        if not isinstance(other, Vector):
            return NotImplemented
        for i in range(max(self.dimension, other.dimension)):
            self[i] -= other[i]
        return self
    
    def __imul__(self, other: object) -> Self:
        """In-place multiplication of the vector by a scalar."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        for i in range(self.dimension):
            self[i] *= other
        return self
    
    def __idiv__(self, other: object) -> Self:
        """In-place division of the vector by a scalar."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        for i in range(self.dimension):
            self[i] /= other
        return self
    
    def __itruediv__(self, other: object) -> Self:
        """In-place true division of the vector by a scalar."""
        return self.__idiv__(other)



