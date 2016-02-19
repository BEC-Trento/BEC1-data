prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(20000, "Mirrors Imaging")
    prg.add(30000, "Shutter Optical Levit ON", enable=False)
    prg.add(30000, "Shutter Optical Levit Open")
    prg.add(40000, "Optical Levit ON")
    prg.add(4500000, "Optical Levit (-) Amp", 1.000000)
    prg.add(4800000, "Optical Levit OFF", enable=False)
    prg.add(5000000, "Picture NaK.sub")
    prg.add(5150000, "Optical Levit (-) Amp", 1000.000000)
    prg.add(5800000, "Optical Levit ON", enable=False)
    prg.add(6001200, "Optical Levit OFF")
    prg.add(6500000, "Shutter Optical Levit OFF", enable=False)
    prg.add(9011000, "Shutter Optical Levit OFF", enable=False)
    prg.add(9011000, "Shutter Optical Levit Close")
    prg.add(12000000, "Optical Levit ON")
    return prg
