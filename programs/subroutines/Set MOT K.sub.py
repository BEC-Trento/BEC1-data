prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000, "Delta 1 Current", 7.000000)
    prg.add(1100, "Delta 2 Current", 200.000000)
    prg.add(1200, "Delta 1 Voltage", 30.000000)
    prg.add(1300, "Delta 2 Voltage", 0.000000)
    prg.add(5000, "Mirrors MOT")
    prg.add(5400, "Shutter RepumperMOT K Open")
    prg.add(5800, "Shutter Probe K Open")
    prg.add(6200, "Shutter CoolerMOT K Open")
    prg.add(6600, "Shutter Push K Open")
    prg.add(20000, "K Cooler 2p (+) freq", 97.500000)
    prg.add(20500, "K Repumper 2p (+) freq", 96.000000)
    prg.add(22000, "K Cooler 1p (-) freq", 115.000000)
    prg.add(22500, "K Repumper 1p (+) freq", 115.000000)
    prg.add(23000, "K Cooler 1p (-) Amp", 1000.000000)
    prg.add(23500, "K Repumper 1p (+) Amp", 1000.000000)
    prg.add(24000, "K probe Cooler (-) freq", 99.500000)
    prg.add(24500, "K probe Repumper (+) freq", 126.000000)
    prg.add(25000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(25500, "K probe Repumper (+) Amp", 750.000000)
    prg.add(40000, "B comp y", 0.000000)
    prg.add(50000, "B comp x", 0.000000)
    return prg