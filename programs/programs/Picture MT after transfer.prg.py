prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(1500000, "Set MOT.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(3000000, "Dark Spot MOT load.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(82003000, "All Shutter Close.sub")
    prg.add(86000000, "All AOM On.sub", enable=False)
    prg.add(90000200, "Evaporation Ramp.sub")
    prg.add(370005000, "Picture - Field off at 0ms - Levit 3ms.sub", enable=False)
    prg.add(370005000, "Picture - Field off at 0ms - Levit 30ms.sub")
    prg.add(370005000, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(401500000, "Set MOT.sub")
    prg.add(402000000, "Dark Spot MOT load.sub")
    prg.add(402100000, "Config MOT.sub")
    prg.add(467960000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 200ms.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 250ms.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 120ms.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    return prg
