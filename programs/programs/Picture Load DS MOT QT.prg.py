prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(10000, "Set MOT.sub")
    prg.add(500000, "Dark Spot MOT load.sub")
    prg.add(1000000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(29940000, "Config Field OFF.sub")
    prg.add(29940500, "Melassa Na.sub")
    prg.add(29941500, "Melassa Na amp.sub")
    prg.add(30000000, "MOT lights Off.sub")
    prg.add(30003000, "All Shutter Close.sub")
    prg.add(30003990, "General Trigger ON")
    prg.add(30004000, "Delta 1 Current", 200.000000)
    prg.add(30004010, "Delta 2 Voltage", 30.000000)
    prg.add(30004020, "Config MOT.sub")
    prg.add(40000000, "Config Field OFF.sub")
    prg.add(40010000, "Picture.sub")
    prg.add(299000000, "Set MOT.sub", enable=False)
    prg.add(299500000, "Dark Spot MOT load.sub", enable=False)
    prg.add(300000000, "Config MOT.sub", enable=False)
    return prg
