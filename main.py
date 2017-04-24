import math
import physics

class System:
    # Diagram Dimensions (m)
    ab = 0.10
    ac = 0.25
    cd = 0.25
    ec = 0.05

    # Angle of system arm without load
    angle_cab_free_deg = 30

    spring = physics.Spring()

    # Load at point D (kg)
    load = 0.2

    # Floating point precision
    float_precision = 12

    def angle_cab_free_rads(self):
        return math.radians(self.angle_cab_free_deg)

    def af(self):
        return self.ac * math.cos(self.angle_cab_free_rads())

    def bc(self):
        return math.sqrt( (self.ab ** 2) + (self.ac ** 2) - (2 * self.ab * self.ac * math.cos(self.angle_cab_free_rads())) )

    def bf(self):
        pass

    def cf(self):
        pass

    def angle_cbf(self):
        pass

test = System()
print(test.bc())