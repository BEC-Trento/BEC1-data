prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10, "IGBT 4 Close")
    prg.add(20, "Delta 1 Voltage", 5.0000)
    prg.add(2000, "Config Levitation zero current.sub")
    return prg
