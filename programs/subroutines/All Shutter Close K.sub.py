prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1800010, "Shutter RepumperMOT K Close")
    prg.add(-1800000, "Shutter Probe K Close")
    prg.add(-1799990, "Shutter CoolerMOT K Close")
    prg.add(-1799980, "Shutter Push K Close")
    return prg
