prg_comment = "gbho"
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5, "Pulse uw ON", enable=False)
    prg.add(0, "Pulse uw OFF", enable=False)
    return prg
