from expectorant import *
from expectorant import runner
import glob

@describe('runner')
def _():

    @describe('find_files()')
    def _():

        @it('returns *_spec.py files in current directory when args=[]')
        def _():
            args = []
            expect(runner.find_files(args)) == glob.glob('./**/*_spec.py', recursive=True)

        @it('passes args through when args are filenames')
        def _():
            args = ['specs/runner_spec.py']
            expect(runner.find_files(args)) == ['specs/runner_spec.py']

        @it('returns all spec filenames when args is directory')
        def _():
            args = ['specs']
            expect(runner.find_files(args)) == glob.glob('specs/*_spec.py')

        @it('raises error when args has filename that doesnt exist')
        def _():
            args = ['non_existent.file']
            expect(lambda: runner.find_files(args)).to(raise_error, FileNotFoundError)
