prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(5000, "Initialize 0 TTL3", enable=False)
    prg.add(10000, "Initialize 0 TTL0")
    prg.add(100000, "Set MOT.sub")
    prg.add(1000000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(14000000, "Config Field OFF.sub")
    prg.add(15000000, "Shutter Probe Na Open")
    prg.add(18000000, "Config MOT.sub")
    prg.add(20000000, "MOT lights Off.sub")
    prg.add(20002500, "Config Field OFF.sub")
    prg.add(20010000, "Picture close.sub")
    prg.add(26000000, "Set MOT.sub")
    prg.add(27000000, "Config MOT.sub")
    return prg
