prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter RepumperMOT K Open")
    prg.add(10, "Shutter Probe Na Open")
    prg.add(20, "Shutter Push Na Open")
    prg.add(30, "Shutter 3DMOT cool Na Open")
    prg.add(40, "Shutter EOM Na Open")
    prg.add(50, "Shutter repump Na Open")
    prg.add(60, "Shutter RepumperMOT K Open")
    prg.add(70, "Shutter Probe K Open")
    prg.add(80, "Shutter CoolerMOT K Open")
    prg.add(90, "Shutter Push K Open")
    return prg
