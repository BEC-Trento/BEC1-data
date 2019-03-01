prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(29995000, "MOT lights Off TTL short.sub")
    prg.add(29996000, "Config Field OFF.sub")
    prg.add(29999000, "mot imaging subroutine atoms probe bg")
    prg.add(35000000, "Set MOT NaK.sub")
    prg.add(35500000, "Dark Spot MOT load.sub")
    prg.add(35600000, "Config MOT.sub")
    prg.add(40000000, "Shutter Probe Na Open")
    return prg
