prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(77000000, "Shutter Probe Na Open")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off.sub")
    prg.add(80012500, "Picture.sub", enable=False)
    prg.add(80182500, "Picture close.sub")
    prg.add(89000000, "Set MOT.sub")
    prg.add(89500000, "Dark Spot MOT load.sub")
    prg.add(89600000, "Config MOT.sub")
    return prg
