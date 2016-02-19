prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000, "Set MOT.sub")
    prg.add(1000000, "Deplete Na MOT.sub")
    prg.add(1200000, "Dipole Trap On.sub")
    prg.add(50650000, "Dark Spot MOT.sub")
    prg.add(50960000, "Melassa Na.sub")
    prg.add(51000000, "MOT Off.sub")
    prg.add(51183100, "Picture.sub")
    prg.add(60000000, "Set MOT.sub")
    prg.add(61200000, "Dipole Trap Off.sub", enable=False)
    return prg
