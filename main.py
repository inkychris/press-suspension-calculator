import math
import physics

class System:
    # Diagram Dimensions (m)
    ac = 0.25
    ad = 0.5
    ab = 0.08
    ec = 0.06

    spring = physics.Spring()

    # Load at point D (kg)
    load = 0.5

    def bc(self, spring_compression):
        return float(self.ec + self.spring.length(spring_compression))

    def cos_a(self, spring_compression):
        return float((pow(self.ab, 2) + pow(self.ac, 2) - pow(self.bc(spring_compression), 2))/(2 * self.ab * self.ac))

    def angle(self, spring_compression):
        return float(math.degrees(math.acos(self.cos_a(spring_compression))))

    def load_moment(self, spring_compression):
        return float(self.load * 9.81 * self.ad * self.cos_a(spring_compression))

    def suspension_moment(self, spring_compression):
        return float(self.spring.force(spring_compression) * self.ac * math.sqrt((1 - pow(self.cos_a(spring_compression), 2))))

    def moment(self, spring_compression):
        return float(self.load_moment(spring_compression) - self.suspension_moment(spring_compression))

    def spring_compression(self):
        min_comp = 0
        max_comp = self.spring.minimum_length

        while True:
            compression = (max_comp + min_comp)/2
            if 0.0 < self.moment(compression):
                max_comp = compression
            elif 0.0 > self.moment(compression):
                min_comp = compression
            else:
                return compression


press = System()
x = 0.005
print("Angle: {angle}".format(angle=press.angle(x)))
print("BC: {bc}".format(bc=press.bc(x)))
print("Moment: {moment}".format(moment=press.moment(x)))

print(press.spring_compression())