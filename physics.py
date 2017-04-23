import unittest

class Spring:
    # Spring constant (Nm^-1)
    constant = 1630

    # Length of spring without load (m)
    free_length = 0.135

    # Specified minimum length (m)
    minimum_length = 0.0388

    # Returns length of spring after given compression
    def length(self, compression):
        if compression < 0:
            raise AttributeError("Compression value must be a positive number")

        length = self.free_length - compression

        if length < self.minimum_length:
            raise AttributeError(
                "Compression value {comp}m exceeds spring minimum length {len}m".format(
                    comp=compression, len=self.minimum_length))

        return length

    # Returns the force for a given compression distance
    def force(self, compression):
        return round(self.constant * (self.free_length - self.length(compression)), 12)

    # Returns the force of the spring at a given length
    def force_at_length(self, length):
        return self.force(self.free_length - length)


class TestSpring(unittest.TestCase):
    def setUp(self):
        self.spring = Spring()
        self.spring.constant = 1000
        self.spring.free_length = 0.1
        self.spring.minimum_length = 0.01

    def test_length(self):
        self.assertEqual(self.spring.length(0.05), 0.05)
        with self.assertRaises(AttributeError):
            self.spring.length(0.095)

    def test_force(self):
        self.assertEqual(self.spring.force(0.01), 10)

    def test_force_at_length(self):
        self.assertEqual(self.spring.force_at_length(0.09), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)