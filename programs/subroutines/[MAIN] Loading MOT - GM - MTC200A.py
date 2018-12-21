prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "All Shutter Close 2017.sub")
    prg.add(490, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1200, "MOT lights Off close.sub")
    prg.add(2700, "Mirrors Imaging")
    prg.add(6207, "Gray Molasses 2017")
    prg.add(66207, "empty.sub")
    prg.add(66207, "Loading_GM_Q50_MTC200A")
    prg.add(69472, "TTL0-13 broken ON", enable=False)
    prg.add(2191117, "B comp x", 665.0, enable=False)
    prg.add(4999472, "All AOM On.sub")
    return prg
