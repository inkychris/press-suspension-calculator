import math
import physics

class System:
    # Diagram Dimensions (m)
    ab = 0.10
    ac = 0.25
    cd = 0.25

    # Angle of system arm without load
    CAB = 35

    spring = physics.Spring()

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

    def ec(self, spring_compression):
        return self.bc() - self.spring.length(spring_compression)

    def spring_compression(self):
        minimum_compression = 0
        maximum_compression = self.spring.free_length - self.spring.minimum_length

        while not math.isclose(minimum_compression, maximum_compression, rel_tol=1e-12):
            compression = ( maximum_compression + minimum_compression ) / 2
            moment = self.load_moment() - self.suspension_moment(compression)

            if moment < 0:
                maximum_compression = compression
            elif moment > 0:
                minimum_compression = compression

        return round(minimum_compression, 12)


test = System()
print(test.ec(test.spring_compression()))