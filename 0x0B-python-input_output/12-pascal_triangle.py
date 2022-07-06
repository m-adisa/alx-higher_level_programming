#!/usr/bin/python3
"""Module 12-pascal_triangle
1) pascal_triangle(n)
"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing a pascals triangle of n
    Args:
        - n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append[1]
        triangles.append(tmp)
    return triangles
