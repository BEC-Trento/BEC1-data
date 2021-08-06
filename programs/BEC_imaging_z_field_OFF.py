prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_imaging_z")
    prg.add(3000000, "B grad comp OFF")
    prg.add(3030000, "IGBT B grad x OFF")
    return prg
