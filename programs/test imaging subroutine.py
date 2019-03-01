prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5640000, "Shutter Probe Na Open")
    prg.add(-2639900, "TTL Repumper MOT OFF", enable=False)
    prg.add(-2639000, "TTL Repumper MOT ON", enable=False)
    prg.add(-2638000, "TTL Repumper MOT OFF", enable=False)
    prg.add(-840000, "Na Probe/Push (+) OFF")
    prg.add(-820000, "Trig ON Stingray 1")
    prg.add(-819000, "Trig OFF Stingray 1")
    prg.add(-170000, "Na Probe/Push (+) ON")
    prg.add(-169900, "Na Probe/Push (+) OFF")
    prg.add(-20000, "TTL Repumper MOT ON")
    prg.add(-19900, "TTL Repumper MOT OFF")
    prg.add(-10000, "Trig ON Stingray 1")
    prg.add(-9000, "Trig OFF Stingray 1")
    prg.add(0, "Na Probe/Push (+) ON")
    prg.add(100, "Na Probe/Push (+) OFF")
    prg.add(10000, "Shutter Probe Na Close")
    prg.add(1180000, "Trig ON Stingray 1")
    prg.add(1181000, "Trig OFF Stingray 1")
    prg.add(2980000, "Na Probe/Push (+) ON")
    return prg
