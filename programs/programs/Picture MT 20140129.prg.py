prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(82003000, "All Shutter Close.sub")
    prg.add(85000000, "Mirrors Imaging")
    prg.add(85500000, "IGBT B comp x ON")
    prg.add(86000000, "All AOM On.sub")
    prg.add(89000000, "B comp x", 349.000000, enable=False)
    prg.add(90000200, "Evaporation Ramp.sub", enable=False)
    prg.add(130000000, "Config Field OFF.sub")
    prg.add(130050000, "Picture NaK.sub")
    prg.add(151500000, "Set MOT NaK.sub")
    prg.add(152000000, "Dark Spot MOT load.sub")
    prg.add(152100000, "Config MOT.sub")
    prg.add(153000000, "Shutter Probe Na Open", enable=False)
    prg.add(154000000, "Shutter Bragg Open", enable=False)
    prg.add(155000000, "Pulse MOT Na ON", enable=False)
    return prg
