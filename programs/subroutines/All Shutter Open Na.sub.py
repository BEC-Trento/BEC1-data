prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Shutter Probe Na Open")
    prg.add(20, "Shutter Push Na Open")
    prg.add(30, "Shutter 3DMOT cool Na Open")
    prg.add(40, "Shutter EOM Na Open")
    prg.add(50, "Shutter repump Na Open")
    return prg
