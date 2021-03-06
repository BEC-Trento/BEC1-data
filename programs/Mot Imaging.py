prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(32100000, "MOT lights Off TTL short.sub")
    prg.add(32101000, "Config Field OFF.sub")
    prg.add(32105000, "mot imaging subroutine atoms probe bg")
    prg.add(37105000, "Set MOT NaK.sub")
    prg.add(37605000, "Dark Spot MOT load.sub")
    prg.add(37705000, "Config MOT.sub")
    return prg
