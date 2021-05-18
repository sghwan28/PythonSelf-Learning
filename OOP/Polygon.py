from math import sin, cos, pi, isclose, sqrt


class Polygon(object):
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices')
        self.n = n
        self.R = R

    @property
    def count_vertices(self):
        return self.n

    @property
    def count_edges(self):
        return self.n

    @property
    def circumradius(self):
        return self.R

    @property
    def interior_angle(self):
        return (self.n - 2) * (180 / self.n)

    @property
    def edge_length(self):
        return sin(pi / self.n) * 2 * self.R

    @property
    def apothem(self):
        return cos(pi / self.n) * self.R

    @property
    def area(self):
        return 0.5 * self.n * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self.n * self.edge_length

    def __repr__(self):
        return f'Polygon(n={self.n}, R={self.R})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.count_edges == other.count_edges and self.circumradius == other.circumradius
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_edges > other.count_edges
        else:
            return NotImplemented


# Polygons is a sequence
class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]


# below is the unit test


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert isclose(p.area, 2, rel_tol=abs_tol, abs_tol=abs_tol), (f'actual: {p.area},'
                                                                  ' expected: 2.0')

    assert isclose(p.edge_length,  sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                           f' expected: { sqrt(2)}')

    assert isclose(p.perimeter, 4 *  sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 *  sqrt(2)}')

    assert isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = Polygon(6, 2)
    assert isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

test_polygon()