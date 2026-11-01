
import unittest

from mandelbrot import mandelbrot_iterations


class TestMandelbrotIterations(unittest.TestCase):

    def test_origin_does_not_escape(self):
        result = mandelbrot_iterations(0j, 100)
        self.assertEqual(result, 100)

    def test_negative_one_does_not_escape(self):
        result = mandelbrot_iterations(-1 + 0j, 100)
        self.assertEqual(result, 100)

    def test_immediate_escape(self):
        result = mandelbrot_iterations(2 + 2j, 100)
        self.assertEqual(result, 1)

    def test_escape_after_three_iterations(self):
        result = mandelbrot_iterations(1 + 0j, 100)
        self.assertEqual(result, 3)

    def test_boundary_point(self):
        result = mandelbrot_iterations(-2 + 0j, 100)
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
