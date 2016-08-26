from expectorant import *
from expectorant import runner
import glob

@describe('runner')
def _():

    @describe('find_files()')
    def _():

        @it('returns fileenames in spec/ when args=[]')
        def _(scope, expect):
            args = []
            expect(runner.find_files(args)) == glob.glob('specs/*_spec.py')

        @it('passes args through when args are filenames')
        def _(scope, expect):
            args = ['specs/runner_spec.py']
            expect(runner.find_files(args)) == ['specs/runner_spec.py']

        @it('returns all spec filenames when args is directory')
        def _(scope, expect):
            args = ['specs']
            expect(runner.find_files(args)) == glob.glob('specs/*_spec.py')

        @it('throws error when args has filename that doesnt exist')
        def _(scope, expect):
            args = ['non_existent.file']
            expect(lambda: runner.find_files(args)).to(raise_error, FileNotFoundError)
