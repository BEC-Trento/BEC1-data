prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-210000, "IGBT B comp y OFF")
    prg.add(-200000, "B comp y", 3.0000)
    prg.add(-5000, "IGBT B comp y ON")
    return prg
