prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter Phase Imprint Close")
    prg.add(10000000, "Phase Imprint Pulse.sub")
    return prg
