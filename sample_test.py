# Something to be tested

class Adder:
    def __init__(self):
        print("!!! Adder: created.")
        self.sum = 0

    def add(self, val):
        print("!!! Adder: adding", val)
        self.sum += val
        return self

# Our tests

from expectorant import describe, context, it, before

@describe("add")
def _():
    adder = "X"

    @before
    def _():
        nonlocal adder
        print("!!! add-before called. adder=", adder)
        adder = Adder()

    @context("when adding")
    def _():

        @before
        def _():
            print("!!! when-adding-before called")
            adder.add(1)

        def subject(val):
            print("!!! subject called with", val)
            adder.add(val)

        @it("sums 1")
        def _():
            subject(1)
            print("!!! it 1 called. sum=", adder.sum)

        @it("sums 5")
        def _():
            subject(5)
            print("!!! it 5 called. sum=", adder.sum)
#             expect(adder.sum, equals(0))

#             @it("changes score")
#             def _():
#                 expect(subject, changes(lambda: bowling.score, from=0, to=1))

#             @it("is not over")
#             def _():
#                 expect(bowling.is_game_over(), truthy)

