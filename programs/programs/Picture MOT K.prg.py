prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(2000, "Initialize 0 TTL3")
    prg.add(4000, "Initialize 0 TTL0")
    prg.add(6000, "Synchronize.sub")
    prg.add(10000, "Set MOT K.sub")
    prg.add(51000, "Config MOT.sub")
    prg.add(100000, "Rele 5 Close")
    prg.add(29950100, "Melassa K amp.sub")
    prg.add(29950450, "Melassa K freq.sub")
    prg.add(29955000, "Config Field OFF.sub")
    prg.add(29999750, "Config Field OFF.sub")
    prg.add(30000000, "MOT lights Off K.sub")
    prg.add(30050000, "Picture close K.sub")
    prg.add(40000000, "Set MOT.sub", enable=False)
    prg.add(41000000, "Dark Spot MOT load.sub", enable=False)
    prg.add(45000000, "Config MOT.sub")
    prg.add(46000000, "Set MOT K.sub")
    prg.add(46500000, "Rele 5 Open")
    prg.add(47000000, "Shutter 2DMOT K Close")
    return prg
