prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Mirrors Imaging")
    prg.add(20000, "Na Probe/Push (+) ON")
    prg.add(100000, "Shutter Probe Na Open")
    return prg
