prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-500000, "K probe Repumper (+) Amp", 1.000000)
    prg.add(-19000, "B comp y", 0.500000)
    prg.add(-4000, "K probe Cooler (-) freq", 99.500000)
    prg.add(-3500, "K probe Repumper (+) freq", 126.000000)
    prg.add(-3000, "K Cooler 2p (+) freq", 97.500000)
    prg.add(-2600, "K Repumper 1p (+) Amp", 1000.000000)
    prg.add(-2200, "K Repumper 1p (+) freq", 115.000000)
    prg.add(-1700, "K Repumper 2p (+) freq", 96.000000)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(0, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(1000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(1500, "Trig OFF Stingray 1")
    prg.add(999500, "Trig ON Stingray 1")
    prg.add(1000000, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(1001000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(1001500, "Trig OFF Stingray 1")
    prg.add(1010000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(1020000, "K probe Repumper (+) Amp", 1.000000)
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2001500, "Trig OFF Stingray 1")
    prg.add(2999500, "Trig ON Stingray 1")
    prg.add(3001500, "Trig OFF Stingray 1")
    prg.add(4000000, "B comp y", 0.000000)
    return prg
