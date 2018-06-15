prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter repump Na Close")
    prg.add(10, "Shutter Probe Na Close")
    prg.add(20, "Shutter EOM Na Close")
    prg.add(31, "Shutter 3DMOT cool Na Close")
    prg.add(40, "Shutter Push Na Close")
    prg.add(50, "Shutter Bragg Close")
    prg.add(60, "Shutter Repump2 Close")
    return prg
