prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(119950500, "Melassa Na.sub")
    prg.add(119951500, "Melassa Na amp.sub")
    prg.add(119952000, "Config Field OFF.sub")
    prg.add(120000000, "MOT lights Off.sub")
    prg.add(120004000, "Delta 1 Current", 200.000)
    prg.add(120004010, "Delta 2 Voltage", 30.0000)
    prg.add(120004020, "Config MT compr.sub")
    prg.add(122008040, "All Shutter Close.sub")
    prg.add(125010040, "Mirrors Imaging")
    prg.add(125510040, "IGBT B comp x ON")
    prg.add(126010040, "All AOM On.sub")
    prg.add(129010040, "B comp x", 250.0)
    prg.add(130000000, "Evaporation Ramp.sub")
    prg.add(565003000, "Decompress Current MT.sub")
    prg.add(565010000, "Decompress Voltage MT.sub")
    prg.add(681360000, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(681369900, "Config Field OFF.sub")
    prg.add(681375000, "Bragg Pulse Single.sub")
    prg.add(681539900, "Picture NaK.sub")
    prg.add(692662100, "Set MOT NaK.sub")
    prg.add(693162100, "Dark Spot MOT load.sub")
    prg.add(693262100, "Config MOT.sub")
    return prg
