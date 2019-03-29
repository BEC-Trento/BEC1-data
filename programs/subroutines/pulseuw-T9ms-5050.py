prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Pulse uw ON")
    prg.add(37500, "Pulse uw OFF")
    prg.add(75000, "Pulse uw ON")
    prg.add(112500, "Pulse uw OFF")
    prg.add(150000, "Pulse uw ON")
    prg.add(187500, "Pulse uw OFF")
    return prg
