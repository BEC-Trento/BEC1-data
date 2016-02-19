prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-40, "Pulse uw ON")
    prg.add(0, "Pulse uw OFF")
    prg.add(1000, "Optical Levit OFF")
    prg.add(77590, "Optical Levit ON")
    return prg
