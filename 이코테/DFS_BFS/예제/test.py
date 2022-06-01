class MyClass(str):
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def test(self, digits):
        print(digits)


a = MyClass(123)
print(type(a.digits))
a.test("123")