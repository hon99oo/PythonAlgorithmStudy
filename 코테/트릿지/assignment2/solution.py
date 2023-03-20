class Transformer(object):
    """Convert numbers from base 10 integers to base N strings and back again.
    Sample usage:
    base20 = Transformer('0123456789abcdefghij')
    base20.from_decimal(1234)
    '31e'
    base20.to_decimal('31e')
    1234
    """
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        # return early if from_decimal is zero
        if number == 0:
            return todigits[0]

        fromdigits_length = len(fromdigits)
        todigits_length = len(todigits)

        # N -> decimal
        decimal = 0
        for idx, val in enumerate(str(number)[::-1]):
            decimal += (fromdigits_length ** idx) * int(fromdigits.index(val))

        # return early if to_decimal is zero
        if decimal == 0:
            return 0

        # decimal -> N
        result = ''
        while decimal:
            result += todigits[decimal % todigits_length]
            decimal //= todigits_length

        return result[::-1]




binary_transformer = Transformer('01')
hex_transformer = Transformer('0123456789ABCDEF')
base62_transformer = Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
test = Transformer('0123456789abcdefghij')

print(base62_transformer.from_decimal(0))