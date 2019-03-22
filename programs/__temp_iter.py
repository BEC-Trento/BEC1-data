prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1490000, "Trigger LZ ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22096000, "Config Field OFF.sub")
    prg.add(22100000, "MOT lights Off TTL short.sub")
    prg.add(22107000, "mot imaging subroutine atoms probe bg")
    prg.add(27105000, "Set MOT NaK.sub")
    prg.add(27605000, "Dark Spot MOT load.sub")
    prg.add(27705000, "Config MOT.sub")
    prg.add(29000000, "Shutter Probe Na Open")
    prg.add(29010000, "TTL2-12 OFF", enable=False)
    prg.add(29020000, "TTL2-12 ON", enable=False)
    prg.add(29030000, "TTL2-12 OFF", enable=False)
    return prg
