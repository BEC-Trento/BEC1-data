import importlib.util
from pathlib import Path
from pprint import pprint


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

    def rename(self, old, new, dry_run=False):
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

        def _rename(_file, dry_run):
            with open(_file) as f:
                # lines = [line.replace(old, new) for line in f]

                lines = []
                for idx, line in enumerate(f):
                    count = line.count(old)
                    if count:
                        line = line.replace(old, new)
                        print(f'\tline {idx + 1} --> {line}', end='')

                    lines.append(line)

            if not dry_run:
                with open(_file, 'w') as f:
                    for line in lines:
                        f.write(line)

        # first rename at the top file
        print(f'- {self.program.stem}')
        _rename(self.program, dry_run)

        # then all others
        for sub in self.subroutines:
            print(f'- {sub.stem}')
            _rename(sub, dry_run)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', "--dry-run", action="store_true", default=False)
    args = parser.parse_args()

#    program = Path.cwd() / 'programs/BEC_May_2019_Ioffe_evaporation.prg.py'
#    program = Path.cwd() / 'programs/subroutines/BEC_imaging_ready.py'
    program = Path.cwd() / 'programs/test imaging.py'
#    program = Path.cwd() / 'programs/MOT_GM_May_2019.prg.py'
    
    actions = [
        # fuck exp-control yet another time
        ('Shutter Probe Na Close', 'Shutter Probe/Push Close'),
        ('Shutter Probe Na Open',  'Shutter Probe/Push Open'),
        ('Na Probe/Push (+) ON',   'TTL Push ON'),
        ('Na Probe/Push (+) OFF',  'TTL Push OFF'),
        ('Na Probe/Push (+) freq', 'Na Push (+) freq'),
        ('Na Probe/Push (+) Amp',  'Na Push (+) amp'),
        ('Na Probe/Push (-) Amp',  'Na Probe/Push (-) amp')
    ]
    
    if args.dry_run:
        print("--- DRY RUN ---")
    for old, new in actions:
        r = Renamer(program)
        r.rename(old, new, dry_run=args.dry_run)

    # print()
    #
    # r = Renamer(program)
    # r.rename('banana', 'Shutter Probe Na Open')
