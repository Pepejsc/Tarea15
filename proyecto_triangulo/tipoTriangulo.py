class tipoTriangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo(self):
        if self.a == self.b and self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"