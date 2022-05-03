def gcd(n, m):
    """
    Compute the greatest common divisor of two integers
    @param n the first integer under consideration (must be non-zero)
    @param m the second integer under consideration (must be non-zero)
    @return the greatest common divisor of the integers
    """

    d = min(n, m)

    if n != 0 and m !=0:
        while n % d != 0 or m % d != 0:
            d = d - 1

    return d


def reduce(num, den):
    """
    Reduce a fraction to lowest terms
    @param num the integer numerator of the fraction
    @param den the integer denominator of the fraction (must be non-zero)
    @return the numerator and denominator of the reduced fraction
    """

    if num == 0:
        return 0, den

    g = gcd(num, den)

    if num != 0 and den != 0:
        return num // g, den // g
    else:
        return num, den


class Fractie:
    """
    Class used for creating objects of type Fraction
    """

    def __init__(self, numarator: int, numitor: int):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self) -> str:

        reduced = False
        numarator_nou, numitor_nou = reduce(self.numarator, self.numitor)

        if numarator_nou != self.numarator or numitor_nou != self.numitor:
            reduced = True

        if numitor_nou != 0 and (not reduced):
            return "%s/%s" % (numarator_nou, numitor_nou)
        elif numitor_nou == 0 and (not reduced):
            return "%s/%s, numitorul este 0, fractie imposibila!" % (numarator_nou, numitor_nou)
        elif numitor_nou != 0 and reduced:
            return "%s/%s, redusa la %s/%s" % (self.numarator, self.numitor, numarator_nou, numitor_nou)
        elif numitor_nou == 0 and reduced:
            return "%s/%s, redusa la %s/%s, numitorul este 0, fractie imposibila!" % (self.numarator, self.numitor, numarator_nou, numitor_nou)

    def __add__(self, x, y):

        reduced = False
        numarator_nou = self.numarator* y + x * self.numitor
        numitor_nou = self.numitor * y
        numarator_nou_redus = numarator_nou
        numitor_nou_redus = numitor_nou
        numarator_nou_redus, numitor_nou_redus = reduce(numarator_nou, numitor_nou)

        if numarator_nou_redus != numarator_nou or numitor_nou_redus != numitor_nou:
            reduced = True

        if numitor_nou != 0 and (not reduced):
            return "%s/%s+%s/%s=%s/%s" % (self.numarator, self.numitor, x, y, numarator_nou, numitor_nou)
        elif numitor_nou == 0 and (not reduced):
            return "%s/%s+%s/%s=%s/%s, numitorul este 0, fractie imposibila!" % (self.numarator, self.numitor, x, y, numarator_nou, numitor_nou)
        elif numitor_nou != 0 and reduced:
            return "%s/%s+%s/%s=%s/%s, fractie redusa" % (self.numarator, self.numitor, x, y, numarator_nou_redus, numitor_nou_redus)
        elif numitor_nou == 0 and reduced:
            return "%s/%s+%s/%s=%s/%s, fractie redusa, numitorul este 0, fractie imposibila!" % (self.numarator, self.numitor, x, y, numarator_nou_redus, numitor_nou_redus)

    def __sub__(self, x, y):

        reduced = False
        numarator_nou, numitor_nou = reduce(self.numarator, self.numitor)
        numarator_nou = numarator_nou * y - x * numitor_nou
        numitor_nou = numitor_nou * y
        numarator_nou_redus = numarator_nou
        numitor_nou_redus = numitor_nou
        numarator_nou_redus, numitor_nou_redus = reduce(numarator_nou, numitor_nou)

        if numarator_nou_redus != numarator_nou or numitor_nou_redus != numitor_nou:
            reduced = True

        if numitor_nou != 0 and (not reduced):
            return "%s/%s-%s/%s=%s/%s" % (self.numarator, self.numitor, x, y, numarator_nou, numitor_nou)
        elif numitor_nou == 0 and (not reduced):
            return "%s/%s-%s/%s=%s/%s, numitorul este 0, fractie imposibila!" % (self.numarator, self.numitor, x, y, numarator_nou, numitor_nou)
        elif numitor_nou != 0 and reduced:
            return "%s/%s-%s/%s=%s/%s, fractie redusa" % (self.numarator, self.numitor, x, y, numarator_nou_redus, numitor_nou_redus)
        elif numitor_nou == 0 and reduced:
            return "%s/%s-%s/%s=%s/%s, fractie redusa, numitorul este 0, fractie imposibila!" % (self.numarator, self.numitor, x, y, numarator_nou_redus, numitor_nou_redus)

    def inverse(self) -> str:

        reduced = False
        numarator_nou, numitor_nou = reduce(self.numarator, self.numitor)

        if numarator_nou != self.numarator or numitor_nou != self.numitor:
            reduced = True

        if numarator_nou != 0 and (not reduced):
            return "%s/%s" % (self.numitor, self.numarator)
        elif numarator_nou == 0 and (not reduced):
            return "%s/%s, numitorul este 0, fractie imposibila!" % (self.numitor, self.numarator)
        elif numarator_nou != 0 and reduced:
            return "%s/%s, redusa la %s/%s" % (self.numitor, self.numarator, numitor_nou, numarator_nou)
        elif numarator_nou == 0 and reduced:
            return "%s/%s, redusa la %s/%s, numitorul este 0, fractie imposibila!" % (self.numitor, self.numarator, numitor_nou, numarator_nou)


fractie = Fractie(3, 2)
print(fractie.__str__())
print(fractie.inverse())
print(fractie.__add__(2, 2))
print(fractie.__add__(2, 0))
print(fractie.__sub__(3, 4))
print(fractie.__sub__(3, 0))

fractie2 = Fractie(6, 4)
print(fractie2.__str__())
print(fractie2.inverse())
print(fractie2.__add__(2, 2))
print(fractie2.__add__(2, 0))
print(fractie2.__sub__(3, 4))
print(fractie2.__sub__(3, 0))

fractie3 = Fractie(0, 2)
print(fractie3.__str__())
print(fractie3.inverse())
