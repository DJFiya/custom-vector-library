"""Unit tests for the Vector class."""

import pytest
from copy import deepcopy
from vector import Vector

V1 = Vector([1, 2, 3])
V2 = Vector([4, 5, 6])
V3 = Vector([0, 0, 0])
V4 = Vector([7, 8])
V5 = Vector([1, 2])

def test_properties():
    assert V1.magnitude == pytest.approx(3.7417, rel=1e-4)
    for val1, val2 in zip(V1, V1.direction * V1.magnitude):
        assert val1 == pytest.approx(val2, rel=1e-3)
    assert V1.dimension == 3
    assert V4.dimension == 2

def test_comparison_operations():
    assert V1 == Vector([1, 2, 3])
    assert V1 != V2
    assert V1 < V2
    assert V1 <= V2
    assert V4 > V5
    assert V4 >= V5

def test_type_conversion():
    assert repr(V1) == "Vector([1.0, 2.0, 3.0])"
    assert str(V2) == "<4.0, 5.0, 6.0>"
    assert bool(V1) is True
    assert bool(V3) is False
    assert int(V1) == int(V1.magnitude)
    assert float(V2) == V2.magnitude
    assert f"{V1:.2f}" == "<1.00, 2.00, 3.00>"
    assert complex(V4) == complex(7, 8)
    with pytest.raises(ValueError):
        complex(V1)

def test_container_methods():
    assert len(V1) == 3
    assert list(V1) == [1.0, 2.0, 3.0]
    assert V1[0] == 1
    vector = deepcopy(V1)
    assert vector[10] == 0
    with pytest.raises(IndexError):
        V1[-1]
    vector[1] = 10
    assert vector[1] == 10

def test_arithmetic_operations():
    assert V1 + V2 == Vector([5.0, 7.0, 9.0])
    assert V1 - V2 == Vector([-3.0, -3.0, -3.0])
    assert V1 * 2 == Vector([2.0, 4.0, 6.0])
    assert V1 ** V2 == 32.0
    assert V1 @ V2 == Vector([-3.0, 6.0, -3.0])
    assert -V1 == Vector([-1.0, -2.0, -3.0])
    assert +V1 == V1

def test_inplace_operations():
    v6 = Vector([1, 2, 3])
    v6 += Vector([1, 1, 1])
    assert v6 == Vector([2.0, 3.0, 4.0])
    v6 -= Vector([1, 0, 1])
    assert v6 == Vector([1.0, 3.0, 3.0])
    v6 *= 2
    assert v6 == Vector([2.0, 6.0, 6.0])
    v6 /= 2
    assert v6 == Vector([1.0, 3.0, 3.0])
    with pytest.raises(ZeroDivisionError):
        v6 /= 0

def test_error_handling():
    v1 = Vector([1, 2, 3])
    v2 = Vector([0, 0, 0])
    with pytest.raises(TypeError):
        v1 / v2
    with pytest.raises(TypeError):
        v1 // v2
    with pytest.raises(TypeError):
        v1 % v2
    with pytest.raises(TypeError):
        bytes(v1)