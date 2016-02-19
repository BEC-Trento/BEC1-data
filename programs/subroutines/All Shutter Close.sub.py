prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1800060, "Shutter repump Na Close")
    prg.add(-1800050, "Shutter Probe Na Close")
    prg.add(-1800040, "Shutter EOM Na Close")
    prg.add(-1800029, "Shutter 3DMOT cool Na Close")
    prg.add(-1800020, "Shutter Push Na Close")
    prg.add(-1800010, "Shutter Bragg Close")
    return prg
