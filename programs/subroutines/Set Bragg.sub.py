prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Na Probe/Push (+) OFF")
    prg.add(10, "Na 3D MOT cool (-) OFF")
    prg.add(10000, "Shutter Bragg Open")
    return prg
