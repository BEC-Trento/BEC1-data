prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "K Cooler 2p (+) freq", 97.500000)
    prg.add(20000, "K Cooler 2p (+) Amp", 1000.000000)
    prg.add(30000, "K Repumper 2p (+) freq", 96.000000)
    prg.add(40000, "K Repumper 2p (+) Amp", 1000.000000)
    prg.add(50000, "K probe Repumper (+) freq", 126.000000)
    prg.add(60000, "K probe Repumper (+) Amp", 780.000000)
    prg.add(70000, "K probe Cooler (-) freq", 99.500000)
    prg.add(80000, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(90000, "K Cooler 1p (-) freq", 115.000000)
    prg.add(100000, "K Cooler 1p (-) Amp", 1000.000000)
    prg.add(110000, "K Repumper 1p (+) freq", 115.000000)
    prg.add(120000, "K Repumper 1p (+) Amp", 1000.000000)
    return prg
