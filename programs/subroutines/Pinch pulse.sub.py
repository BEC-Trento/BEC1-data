prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2000, "IGBT 6 Close")
    prg.add(0, "IGBT 6 Open")
    return prg
