def mandelbrot_iterations(c: complex, max_iterations: int) -> int:
    """
    Calculate the number of iterations for a given complex number c to determine if it belongs to the Mandelbrot set.

    Parameters:
    c (complex): The complex number to test.
    max_iterations (int): The maximum number of iterations to perform.

    Returns:
    int: The number of iterations before the magnitude of z exceeds 2, or max_iterations if it does not exceed 2.
    """
    z = 0 + 0j
    for n in range(max_iterations):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iterations