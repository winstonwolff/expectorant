# Something to be tested

class SodaFountain:
    def __init__(self):
#         print("!!! SodaFountain: created.")
        self.syrup = 10

    def pour(self, quantity):
#         print("!!! SodaFounding: pouring", quantity)
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
#             print("!!! when-adding-before called")
            soda_fountain.pour(1)

        def subject(val):
#             print("!!! subject called with", val)
            soda_fountain.pour(val)

        @it("pouring another leaves 8 left")
        def _(expect):
            subject(1)
            expect.is_equal(soda_fountain.syrup, 8)
#             print("!!! it 1 called. sum=", soda_fountain.syrup)

        @it("pouring 5 leaves 4 left")
        def _(expect):
            subject(5)
            expect.is_equal(soda_fountain.syrup, 4)
#             print("!!! it 5 called. sum=", soda_fountain.syrup)
#             expect(adder.sum, equals(0))

#             @it("changes score")
#             def _():
#                 expect(subject, changes(lambda: bowling.score, from=0, to=1))

#             @it("is not over")
#             def _():
#                 expect(bowling.is_game_over(), truthy)

