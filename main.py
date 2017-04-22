import math

class Spring:
    constant = 1630
    free_length = 0.135

    def force(self, compression):
        return self.constant * compression


class System:
    # Diagram Dimensions (metres)
    ac = 0.25
    ad = 0.5
    ab = 0.08
    ec = 0.06

    spring = Spring()

    # Load at point D (kg)
    load = 0.5

    def bc(self, spring_compression):
        return self.ec + self.spring.free_length - spring_compression

    def cos_a(self, spring_compression):
        return (pow(self.ab, 2) + pow(self.ac, 2) - pow(self.bc(spring_compression), 2))/(2 * self.ab * self.ac)

    def angle(self, spring_compression):
        return math.degrees(math.acos(self.cos_a(spring_compression)))

    def load_moment(self, spring_compression):
        return self.load * 9.81 * self.ad * self.cos_a(spring_compression)

    def suspension_moment(self, spring_compression):
        return self.spring.force(spring_compression) * self.ac * pow((1 - pow(self.cos_a(spring_compression), 2)), 0.5)

    def moment(self, spring_compression):
        return self.load_moment(spring_compression) - self.suspension_moment(spring_compression)


press = System()
x = 0.005
print("Angle: {angle}".format(angle=press.angle(x)))
print("BC: {bc}".format(bc=press.bc(x)))