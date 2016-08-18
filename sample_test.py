# Something to be tested

class SodaFountain:
    def __init__(self):
        self.syrup = 10

    def pour(self, quantity):
        self.syrup -= quantity

# Our tests

from expectorant import describe, context, it, before

@describe("SodaFountain")
def _():
    soda_fountain = "X"

    @before
    def _():
        nonlocal soda_fountain
        soda_fountain = SodaFountain()

    @context("when one is already poured")
    def _():

        @before
        def _():
            soda_fountain.pour(1)

        def subject(val):
            soda_fountain.pour(val)

        @it("pouring another leaves 8 left")
        def _(expect):
            subject(1)
            expect.is_equal(soda_fountain.syrup, 8)

        @it("pouring 5 leaves 4 left")
        def _(expect):
            subject(5)
            expect.is_equal(soda_fountain.syrup, 4)
