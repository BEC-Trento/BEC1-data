prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "K probe Cooler (-) Amp", 1.000000)
    prg.add(500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(1000, "K Cooler 1p (-) Amp", 1.000000)
    prg.add(1500, "K Repumper 1p (+) Amp", 1.000000)
    return prg
