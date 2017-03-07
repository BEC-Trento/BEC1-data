prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "BREAKPOINT")
    prg.add(10000, "NOP")
    prg.add(5000000, "Mirrors Imaging")
    prg.add(15000000, "Mirrors MOT")
    return prg
