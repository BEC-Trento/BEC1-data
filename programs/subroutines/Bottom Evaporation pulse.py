prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Bottom Evaporation ON")
    prg.add(5000, "Bottom Evaporation OFF")
    return prg
