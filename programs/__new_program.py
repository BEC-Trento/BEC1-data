prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Set MOT NaK.sub")
    prg.add(2100000, "Dark Spot MOT load.sub")
    prg.add(5000000, "Config MOT.sub")
    prg.add(6000000, "Pulse MOT Na ON")
    return prg
