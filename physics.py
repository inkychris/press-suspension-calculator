import math
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


class System:
    # Diagram Dimensions (m)
    ab = 0.10
    ac = 0.25
    cd = 0.25

    # Angle of system arm without load
    CAB = 35

    spring = Spring()

    # Load at point D (kg)
    load = 0.5

    def CAB_rads(self):
        return math.radians(self.CAB)

    def af(self):
        return self.ac * math.cos(self.CAB_rads())

    def bc(self):
        return math.sqrt( (self.ab ** 2) + (self.ac ** 2) - (2 * self.ab * self.ac * math.cos(self.CAB_rads())) )

    def cos_ACB(self):
        return ( (self.ac ** 2) + (self.bc() ** 2) - (self.ab ** 2) ) / ( 2 * self.bc() * self.ac )

    def sin_ACB(self):
        return math.sqrt( 1 - (self.cos_ACB() ** 2) )

    def load_moment(self):
        return self.load * 9.81 * math.cos( self.CAB_rads() ) * (self.ac + self.cd)

    def suspension_moment(self, spring_compression):
        return self.spring.force(spring_compression) * self.sin_ACB()

    def spring_compression(self):
        minimum_compression = 0
        maximum_compression = self.spring.free_length - self.spring.minimum_length

        while not math.isclose(minimum_compression, maximum_compression, rel_tol=1e-12):
            compression = (maximum_compression + minimum_compression) / 2
            moment = self.load_moment() - self.suspension_moment(compression)

            if moment < 0:
                maximum_compression = compression
            elif moment > 0:
                minimum_compression = compression

        return round(minimum_compression, 12)

    def ec(self):
        return self.bc() - self.spring.length( self.spring_compression() )

    def  be_minimum(self):
        return self.ac - (self.ab + self.ec())


if __name__ == '__main__':
    unittest.main(verbosity=2)