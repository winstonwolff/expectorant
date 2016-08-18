Experimenting with a new Unit Testing framework
===============================================

UnitTesting is great but I don't love python's unittest.TestCase. It
feels awkward compared to Ruby's rspec and it also feels like it was
grafted from Java. I know that in Nose, there is no need to write a
class if you don't need a setup() or teardown() which is a nice
simplification. But I have another thing I often need when testing:
running a test with a set of inputs. I don't know a good way to do
this with unittest. Nose has a way but it seems awkward again. So
here's an attempt to re-think unittesting.


## A more complicated example
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


Let me know your thoughts--is this insane, am I missing an important use-case, what would be a nicer way to write tests?

Also, if you or your child wants to learn electricity, try my game Electropocalyse at http://electropocalypse.com

