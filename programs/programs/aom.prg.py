prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000000, "Synchronize.sub")
    prg.add(49900000, "Na Probe/Push (+) freq", 150.000000)
    prg.add(49901000, "Na Probe/Push (-) freq", 150.000000)
    prg.add(49952000, "Pulsed uw.sub")
    prg.add(50001000, "Na Probe/Push (-) freq", 110.000000)
    prg.add(50002000, "Na Probe/Push (+) freq", 110.000000)
    prg.add(50020000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(50021000, "Na Probe/Push (+) Amp", 1.000000)
    return prg
