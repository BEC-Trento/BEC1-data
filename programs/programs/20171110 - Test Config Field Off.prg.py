prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1090000, "Delta 1 Current", 50.000)
    prg.add(1190000, "Delta 1 Voltage", 15.0000)
    prg.add(1210000, "Config MOT.sub")
    prg.add(1211000, "TTL2-12 ON")
    prg.add(30000000, "Delta 1 Voltage", 0.0000, enable=False)
    prg.add(30089989, "TTL2-12 OFF")
    prg.add(30090000, "Config Field OFF.sub")
    return prg
