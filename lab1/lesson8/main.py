class Snow:
    def __init__(self, snowflake):
        self.snowflake = snowflake

    def __add__(self, n):
        return Snow(self.snowflake + n)

    def __sub__(self, n):
        return Snow(self.snowflake - n)

    def __mul__(self, n):
        return Snow(self.snowflake * n)

    def __truediv__(self, n):
        return Snow(round(self.snowflake / n))

    def __call__(self, new_snowflake):
        self.snowflake = new_snowflake

    def make_snow(self, row):
        rows = self.snowflake // row
        ost = self.snowflake % row
        return ('*' * row + '\n') * rows + ('*' * ost if ost else '')

snow = Snow(15)
snow + 5
print(snow.make_snow(5))