prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter 2DMOT Open")
    prg.add(10000, "Shutter 3DMOT cool Na Open")
    prg.add(20000, "Shutter Dark Spot Open")
    prg.add(30000, "Shutter EOM Na Open")
    prg.add(40000, "Shutter Probe/Push Open")
    prg.add(50000, "Shutter repump Na Open")
    prg.add(60000, "Shutter Gray molasses Open")
    return prg
