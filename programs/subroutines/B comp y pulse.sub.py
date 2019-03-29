prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-600000, "IGBT B comp y ON")
    prg.add(0, "IGBT B comp y OFF")
    return prg
