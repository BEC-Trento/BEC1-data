prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Set MOT NaK.sub")
    prg.add(500000, "Dark Spot MOT load.sub")
    prg.add(600000, "Config MOT.sub")
    return prg
