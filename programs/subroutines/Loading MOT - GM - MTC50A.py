prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "All Shutter Close 2017.sub")
    prg.add(490, "Pulse TTL2-12", polarity=1, pulse_t=0.54000)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1200, "MOT lights Off close.sub")
    prg.add(2700, "Mirrors Imaging")
    prg.add(6207, "Gray Molasses 2017")
    prg.add(66207, "empty.sub")
    prg.add(66207, "Loading_GM_Q50_MTC200A", enable=False)
    prg.add(66207, "Delta 1 Current", 50.000)
    prg.add(66427, "Config MOT.sub")
    prg.add(91117, "Delta 1 Voltage", 15.0000)
    prg.add(2091117, "Config MOT to MT compr.sub")
    prg.add(2861570, "Delta 1 Voltage", 30.0000)
    prg.add(4999472, "All AOM On.sub")
    return prg
