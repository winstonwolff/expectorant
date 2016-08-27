# --- Something to be tested

class SodaFountain:
    def __init__(self):
        self.syrup = 10

    def pour(self, quantity):
        self.syrup -= quantity

    def shutdown(self):
        pass

# --- Our tests


from expectorant import *

@describe("SodaFountain")
def _():

    @context("pour()")
    def _():

        @before
        def _(scope, expect):
            scope.soda_fountain = SodaFountain()

        @after
        def _(scope, expect):
            scope.soda_fountain.shutdown()

        def subject(soda_fountain, val):
            soda_fountain.pour(val)

        @context("when fresh")
        def _():

            @it("has 10 units of syrup")
            def _(scope, expect):
                expect(scope.soda_fountain.syrup) == 10

            @it("has 0 syrup when pouring 99 (this fails)")
            def _(scope, expect):
                subject(scope.soda_fountain, 99)
                expect(scope.soda_fountain.syrup).to(equal, 0)


        @context("when one is already poured")
        def _():

            @before
            def _(scope, expect):
                scope.soda_fountain.pour(1)

            @it("pouring another leaves 8 left")
            def _(scope, expect):
                subject(scope.soda_fountain, 1)
                expect(scope.soda_fountain.syrup).to(equal, 8)

            @it("pouring 5 leaves 4 left")
            def _(scope, expect):
                subject(scope.soda_fountain, 5)
                expect(scope.soda_fountain.syrup).to(equal, 4)

            @it("when pouring {} more, remaining is {}", repeat=[(0, 9), (3, 6), (9, 0)])
            def _(scope, expect, pour, remaining):
                subject(scope.soda_fountain, pour)
                expect(scope.soda_fountain.syrup) == remaining

