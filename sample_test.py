# Something to be tested

class SodaFountain:
    def __init__(self):
        self.syrup = 10

    def pour(self, quantity):
        self.syrup -= quantity

    def shutdown(self):
        pass

# Our tests

from expectorant import describe, context, it, before, after

@describe("SodaFountain")
def _():
    soda_fountain = "X"

    @context("pour()")
    def _():

        @before
        def _(expect):
            nonlocal soda_fountain
            soda_fountain = SodaFountain()

        @after
        def _(expect):
            soda_fountain.shutdown()

        def subject(val):
            soda_fountain.pour(val)

        @context("when fresh")
        def _():

            @it("has 10 units of syrup")
            def _(expect):
                expect.is_equal(soda_fountain.syrup, 10)

            @it("has 0 syrup when pouring 99")
            def _(expect):
                expect.is_equal(soda_fountain.syrup, 0)


        @context("when one is already poured")
        def _():

            @before
            def _(expect):
                soda_fountain.pour(1)

            @it("pouring another leaves 8 left")
            def _(expect):
                subject(1)
                expect.is_equal(soda_fountain.syrup, 8)

            @it("pouring 5 leaves 4 left")
            def _(expect):
                subject(5)
                expect.is_equal(soda_fountain.syrup, 4)
