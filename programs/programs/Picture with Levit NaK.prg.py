prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2200000, "Rele 5 Close")
    prg.add(5000000, "Synchronize.sub")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79954000, "Melassa K freq.sub")
    prg.add(79954450, "Melassa K amp.sub")
    prg.add(79955000, "Config Field OFF.sub")
    prg.add(79960000, "Rele 5 Open")
    prg.add(80000000, "MOT lights Off NaK.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(82003000, "All Shutter Close NaK.sub")
    prg.add(85000000, "Mirrors Imaging")
    prg.add(86000000, "All AOM On.sub")
    prg.add(89000000, "B comp x", 655.000000)
    prg.add(90000200, "Evaporation Ramp.sub")
    prg.add(375000300, "Decompress Current MT.sub")
    prg.add(375010000, "Decompress Voltage MT.sub")
    prg.add(480010000, "Picture - Field off at 0ms - Levit 50ms NaK.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(480010000, "Picture - Field off at 0ms - Levit 10ms NaK.sub")
    prg.add(521500000, "Set MOT NaK.sub")
    prg.add(522000000, "Dark Spot MOT load.sub")
    prg.add(522100000, "Config MOT.sub")
    prg.add(523000000, "Rele 5 Open")
    return prg