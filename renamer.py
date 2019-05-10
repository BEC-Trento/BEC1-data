import importlib.util
from pprint import pprint

try:
    from pathlib import Path
except ImportError:  # @#$%#$ python2
    from pathlib2 import Path


class Renamer:
    def __init__(self, prg):
        self.program = prg
        self._folder = Path(prg).parent
        self.subroutines = []
        self.channels = []

    def add(self, _time, name, *args, **kwargs):
        """Overwrite add method from the program files to collect the
        names of the subprograms.
        """

        name = self._folder / f'subroutines/{name}.py'
        self.subroutines.append(name)

    def _load(self, prgfile):
        # m = importlib.import_module(self.prg)
        spec = importlib.util.spec_from_file_location('prg', prgfile)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)

        return m

    def collect(self):

        def _collect(program):
            m = self._load(program)
            m.program(self, None)

        # populate the list of subprogs from the top file
        _collect(self.program)

        # then recursively look for all subroutines
        for sub in self.subroutines:
            if sub.exists():
                _collect(sub)
            else:
                self.channels.append(sub.stem)

        # clean up the list removing actions to keep subroutines only
        for sub in self.subroutines:
            if not sub.exists():
                self.subroutines = list(
                    filter(lambda a: a != sub, self.subroutines))

        # keep only unique elements
        self.subroutines = set(self.subroutines)

    def rename(self, old, new):
        """Renames an action from <old> to <new> name in all subroutines
        that use it.
        """

        # get all subroutines
        self.collect()

        if new in self.channels:
            raise Exception(f'{new} already exists. Try another one.')

        print(f"Renaming '{old}' to '{new}' in:")
        # for sub in self.subroutines:
        #     print(f'- {sub.stem}')

        def _rename(_file):
            with open(_file) as f:
                # lines = [line.replace(old, new) for line in f]

                lines = []
                for idx, line in enumerate(f):
                    count = line.count(old)
                    if count:
                        line = line.replace(old, new)
                        print(f'\tline {idx + 1} --> {line}', end='')

                    lines.append(line)

            with open(_file, 'w') as f:
                for line in lines:
                    f.write(line)

        # first rename at the top file
        print(f'- {self.program.stem}')
        _rename(self.program)

        # then all others
        for sub in self.subroutines:
            print(f'- {sub.stem}')
            _rename(sub)


if __name__ == '__main__':
    program = Path.cwd() / 'programs/BEC_May_2019.prg.py'

    r = Renamer(program)
    r.rename('Na Repumper MOT Amp', 'TTL Repumper MOT OFF')

    # print()
    #
    # r = Renamer(program)
    # r.rename('banana', 'Shutter Probe Na Open')
