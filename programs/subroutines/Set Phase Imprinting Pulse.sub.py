prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter Phase Imprinting Close")
    prg.add(100, "Phase Imprinting (-) ON")
    prg.add(200, "Phase Imprinting (+) ON")
    prg.add(300, "Phase imprinting (-) Amp", 1000.000000)
    prg.add(700, "Phase imprinting (+) Amp", 1000.000000)
    prg.add(1100, "Phase imprinting (-) freq", 80.000000)
    prg.add(1500, "Phase imprinting (+) freq", 80.000000)
    return prg
