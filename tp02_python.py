class Polynome:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        res = ""
        i = len(self.coefficients) - 1
        while i >= 0:
            if self.coefficients[i] != 0:
                if i == 0:
                    res += "{}".format(self.coefficients[i])
                elif i == 1:
                    res += "{}*x".format(self.coefficients[i])
                else:
                    res += "{}*x^{}".format(self.coefficients[i], i)
                if i != 0:
                    if self.coefficients[i-1] >= 0:
                        res += " + "
                    else:
                        res += " "
            i -= 1
        return res