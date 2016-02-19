prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(1000, "Initialize 0 TTL2")
    prg.add(2000, "Initialize 0 TTL3")
    prg.add(3000, "Initialize 0 TTL4")
    prg.add(20000, "Config Field OFF.sub")
    prg.add(100000, "Synchronize.sub")
    prg.add(1500000, "Set MOT Na.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(40000000, "MOT lights Off.sub")
    prg.add(40005000, "Config MOT.sub")
    prg.add(70000000, "Shutter Probe Na Open")
    prg.add(79999900, "Config Field OFF.sub", enable=False)
    prg.add(80000000, "MOT lights Off close NaK.sub")
    prg.add(80013000, "Picture close NaK.sub")
    prg.add(105000000, "Set MOT NaK.sub")
    prg.add(105500000, "Dark Spot MOT load.sub")
    prg.add(110000000, "All Shutter Open Na.sub")
    prg.add(110020000, "All AOM On.sub")
    return prg
