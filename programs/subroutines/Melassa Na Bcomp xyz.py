prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT B comp x ON")
    prg.add(10, "IGBT B comp y ON")
    prg.add(20, "IGBT B comp z ON")
    prg.add(1000, "Bcomp y Sign Plus")
    prg.add(2000, "Bcomp z Sign Plus")
    return prg
