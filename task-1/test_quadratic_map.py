from mandelbrot import quadratic_map


def test_quadratic_map():
    """
    Test the quadratic map f: z -> z^2 + c
    """

    # Case 1
    f = quadratic_map(c=0, z0=0)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 0  # 0
    assert z1 == 0  # 0^2 + 0
    assert z2 == 0  # (0^2 + 0)^2 + 0

    # Case 2
    f = quadratic_map(c=0, z0=1)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 1  # 1
    assert z1 == 1  # 1^2 + 0
    assert z1 == 1  # (1^2 + 0)^2 + 0

    # Case 3
    f = quadratic_map(c=1, z0=0)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 0  # 0
    assert z1 == 1  # 0^2 + 1
    assert z2 == 2  # (0^2 + 1)^2 + 1

    # Case 4
    f = quadratic_map(c=1, z0=1)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 1  # 1
    assert z1 == 2  # 1^2 + 1
    assert z2 == 5  # (1^2 + 1)^2 + 1

