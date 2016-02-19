prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(10000, "Initialize 0 TTL3")
    prg.add(100000, "Synchronize.sub")
    prg.add(1500000, "Set MOT.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(15000000, "Shutter Probe Na Open")
    prg.add(19950500, "Melassa Na.sub")
    prg.add(19951500, "Melassa Na amp.sub")
    prg.add(19952000, "Config Field OFF.sub")
    prg.add(20000000, "MOT lights Off.sub")
    prg.add(20080000, "Picture close.sub")
    prg.add(29000000, "Set MOT.sub")
    prg.add(29500000, "Dark Spot MOT load.sub")
    prg.add(29600000, "Config MOT.sub")
    return prg
