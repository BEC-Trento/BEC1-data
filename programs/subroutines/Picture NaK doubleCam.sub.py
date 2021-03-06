prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4393000, "K probe Repumper (+) Amp", 1)
    prg.add(-4383000, "K Repumper 1p (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3033000, "Shutter Probe K Open")
    prg.add(-3023000, "Shutter RepumperMOT K Open")
    prg.add(-3013000, "Shutter repump Na Open")
    prg.add(-2493000, "K probe Cooler (-) Amp", 1)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-1200, "Na Probe/Push (+) freq", 116.25)
    prg.add(-800, "Na Probe/Push (-) freq", 103.75)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(302000, "Trig ON Stingray 2")
    prg.add(302500, "Na Probe/Push (-) Amp", 1000)
    prg.add(303500, "Na Probe/Push (-) Amp", 1)
    prg.add(304500, "Trig OFF Stingray 2")
    prg.add(1204500, "Trig ON Stingray 1")
    prg.add(1205000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1206000, "Na Probe/Push (-) Amp", 1)
    prg.add(1207000, "Trig OFF Stingray 1")
    prg.add(1330000, "RFO1 Amp", 800, enable=False)
    prg.add(1330000, "RFO FM amp", 1.0000)
    prg.add(1334500, "Trig ON Stingray 2")
    prg.add(1335000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1336000, "Na Probe/Push (-) Amp", 1)
    prg.add(1337000, "Trig OFF Stingray 2")
    prg.add(1464500, "Trig ON Stingray 1")
    prg.add(1465000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1466000, "Na Probe/Push (-) Amp", 1)
    prg.add(1467000, "Trig OFF Stingray 1")
    prg.add(1590000, "RFO1 Amp", 900, enable=False)
    prg.add(1590000, "RFO FM amp", 1.5000)
    prg.add(1594500, "Trig ON Stingray 2")
    prg.add(1595000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1596000, "Na Probe/Push (-) Amp", 1)
    prg.add(1597000, "Trig OFF Stingray 2")
    prg.add(1724500, "Trig ON Stingray 1")
    prg.add(1725000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1726000, "Na Probe/Push (-) Amp", 1)
    prg.add(1727000, "Trig OFF Stingray 1")
    prg.add(1850000, "RFO1 Amp", 1000, enable=False)
    prg.add(1850000, "RFO FM amp", 2.5000)
    prg.add(1854500, "Trig ON Stingray 2")
    prg.add(1855000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1856000, "Na Probe/Push (-) Amp", 1)
    prg.add(1857000, "Trig OFF Stingray 2")
    prg.add(1980000, "RFO FM amp", 3.0000)
    prg.add(1984500, "Trig ON Stingray 1")
    prg.add(1985000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1986000, "Na Probe/Push (-) Amp", 1)
    prg.add(1987000, "Trig OFF Stingray 1")
    prg.add(2114500, "Trig ON Stingray 2")
    prg.add(2115000, "Na Probe/Push (-) Amp", 1000)
    prg.add(2116000, "Na Probe/Push (-) Amp", 1)
    prg.add(2117000, "Trig OFF Stingray 2")
    return prg
