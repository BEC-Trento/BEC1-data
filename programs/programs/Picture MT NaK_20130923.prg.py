prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(10000, "Initialize 0 TTL3")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(12010000, "Delta 1 Current", 7.800000)
    prg.add(70000000, "Rele 5 Close")
    prg.add(72000000, "Na 3D MOT cool (-) Amp", 350.000000)
    prg.add(79000000, "Rele 5 Open")
    prg.add(79500000, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(79950000, "Melassa K amp.sub")
    prg.add(79950400, "Melassa K freq-short.sub")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off NaK.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(81000000, "All Shutter Close NaK.sub")
    prg.add(85000000, "Mirrors Imaging")
    prg.add(86000000, "All AOM On NaK.sub")
    prg.add(89000000, "B comp x", 248.000000)
    prg.add(90000000, "Evaporation Ramp.sub")
    prg.add(375000000, "Decompress Current MT.sub")
    prg.add(375010000, "Decompress Voltage MT.sub")
    prg.add(474350000, "Config Field OFF ramp.sub")
    prg.add(474600000, "Picture NaK.sub")
    prg.add(500000000, "Set MOT NaK.sub")
    prg.add(501000000, "Config MOT.sub")
    return prg
