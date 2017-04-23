import math
import physics

class System:
    # Diagram Dimensions (m)
    ac = 0.25
    ad = 0.5
    ab = 0.2
    ec = 0.06

    spring = physics.Spring()

    # Load at point D (kg)
    load = 0.2

    # Floating point precision
    float_precision = 12

    def max_spring_compression(self):
        return round(self.spring.free_length - (self.ac - self.ab - self.ec), self.float_precision)

    def validate_spring_compression(self, spring_compression):
        spring_comp = round(spring_compression, self.float_precision)
        if spring_compression <= self.max_spring_compression():
            return spring_comp
        else:
            raise AttributeError("Compression value {} results in invalid triangle dimensions".format(spring_comp))

    def bc(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        return round(self.ec + self.spring.length(spring_comp), self.float_precision)

    def cos_a(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        result = (pow(self.ab, 2) + pow(self.ac, 2) - pow(self.bc(spring_comp), 2))/(2 * self.ab * self.ac)
        if result <= 1 and result >= -1:
            return round(result, self.float_precision)
        else:
            raise ValueError("Result is not within bounds -1.0 to 1.0")

    def angle(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        return round(math.degrees(math.acos(self.cos_a(spring_comp))), self.float_precision)

    def load_moment(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        return round(self.load * 9.81 * self.ad * self.cos_a(spring_comp), self.float_precision)

    def suspension_moment(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        return round(self.spring.force(spring_comp) * self.ac * math.sqrt(1 - pow(self.cos_a(spring_comp), 2)), self.float_precision)

    def moment(self, spring_compression):
        spring_comp = self.validate_spring_compression(spring_compression)
        load_moment = self.load_moment(spring_comp)
        suspension_moment = self.suspension_moment(spring_comp)
        return round(load_moment - suspension_moment, self.float_precision)

    def spring_compression_at_rest(self):
        min_comp = 0
        max_comp = press.max_spring_compression()

        while True:
            min_comp = round(min_comp, self.float_precision)
            max_comp = round(max_comp, self.float_precision)
            if max_comp - min_comp < 10 ** -(self.float_precision - 1):
                return round(min_comp, self.float_precision)

            compression = (max_comp + min_comp) / 2
            moment = self.moment(compression)
            if moment > 0:
                max_comp = compression
            elif moment < 0:
                min_comp = compression

    def print_all(self):
        print("Max Spring Compression: {}".format(self.max_spring_compression()))
        compression = self.spring_compression_at_rest()
        print("BC: {} (m)".format(self.bc(compression)))

        print("Load Moment: {}".format(self.load_moment(compression)))
        print("Suspension Moment: {}".format(self.suspension_moment(compression)))
        print("Spring Compression: {} (m)".format(compression))

        print("Rest Angle: {} (deg)".format(self.angle(compression)))
        print("Spring Force: {} (N)".format(self.spring.force(compression)))




press = System()
press.print_all()