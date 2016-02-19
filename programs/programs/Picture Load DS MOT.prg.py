prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(10000, "Set MOT.sub")
    prg.add(500000, "Dark Spot MOT load.sub")
    prg.add(1000000, "Config MOT.sub")
    prg.add(1200000, "Delta 1 Current", 11.000000)
    prg.add(1210000, "Delta 2 Current", 200.000000)
    prg.add(1220000, "Delta 1 Voltage", 30.000000)
    prg.add(1230000, "Delta 2 Voltage", 0.000000)
    prg.add(5000000, "Synchronize.sub")
    prg.add(9940000, "Config Field OFF.sub")
    prg.add(9940500, "Melassa Na.sub")
    prg.add(9941500, "Melassa Na amp.sub")
    prg.add(10000000, "MOT lights Off.sub")
    prg.add(10001990, "General Trigger ON")
    prg.add(10002000, "Config Field OFF.sub")
    prg.add(10152000, "Picture.sub")
    prg.add(19000000, "Set MOT.sub")
    prg.add(19500000, "Dark Spot MOT load.sub")
    prg.add(20000000, "Config MOT.sub")
    return prg
