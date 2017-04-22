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
        return self.constant * (self.free_length - self.length(compression))

    # Returns the force of the spring at a given length
    def force_at_length(self, length):
        return self.force(self.free_length - length)