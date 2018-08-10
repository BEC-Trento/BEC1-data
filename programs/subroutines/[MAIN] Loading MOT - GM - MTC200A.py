prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "All Shutter Close 2017.sub")
    prg.add(1490, "Pulse TTL2-12", polarity=1, pulse_t=0.54000)
    prg.add(1500, "Config Field OFF.sub")
    prg.add(1800, "MOT lights Off close.sub")
    prg.add(2300, "Mirrors Imaging")
    prg.add(4035, "Gray Molasses 2017")
    prg.add(64035, "empty.sub")
    prg.add(64035, "Loading_GM_Q50_MTC200A")
    prg.add(67300, "TTL0-13 broken ON", enable=False)
    prg.add(2188945, "B comp x", 665.0)
    prg.add(4997300, "All AOM On.sub")
    return prg
