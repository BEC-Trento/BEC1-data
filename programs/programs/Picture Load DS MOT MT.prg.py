prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(500000, "Set MOT.sub")
    prg.add(1000000, "Dark Spot MOT load.sub")
    prg.add(1100000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(59940000, "Config Field OFF.sub")
    prg.add(59940500, "Melassa Na.sub")
    prg.add(59941500, "Melassa Na amp.sub")
    prg.add(60000000, "MOT lights Off.sub")
    prg.add(60003000, "All Shutter Close.sub")
    prg.add(60003990, "General Trigger ON")
    prg.add(60004000, "Delta 1 Current", 200.000000)
    prg.add(60004010, "Delta 2 Voltage", 30.000000)
    prg.add(60004020, "Config MT compr.sub")
    prg.add(70000000, "Config Field OFF.sub")
    prg.add(70010000, "Picture.sub")
    prg.add(75000000, "Set MOT.sub")
    prg.add(76000000, "Dark Spot MOT load.sub")
    prg.add(77000000, "Config MOT.sub")
    return prg
