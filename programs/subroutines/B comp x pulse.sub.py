prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1000, "IGBT 3 Close")
    prg.add(0, "IGBT 3 Open")
    return prg
