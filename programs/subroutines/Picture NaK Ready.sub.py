prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL Repumper MOT ON")
    prg.add(1100, "Trig ON Stingray 1")
    prg.add(1500, "TTL Repumper MOT OFF")
    prg.add(1600, "Na Probe/Push (+) ON")
    prg.add(2600, "Na Probe/Push (+) OFF")
    prg.add(3600, "Trig OFF Stingray 1")
    prg.add(1001100, "Trig ON Stingray 1")
    prg.add(1001600, "Na Probe/Push (+) ON")
    prg.add(1002600, "Na Probe/Push (+) OFF")
    prg.add(1003600, "Trig OFF Stingray 1")
    prg.add(2001100, "Trig ON Stingray 1")
    prg.add(2003100, "Trig OFF Stingray 1")
    prg.add(3001100, "Trig ON Stingray 1")
    prg.add(3003100, "Trig OFF Stingray 1")
    prg.add(4001600, "B comp y", 0.0000, enable=False)
    prg.add(4011600, "IGBT B comp y OFF", enable=False)
    prg.add(4101600, "TTL2-12 OFF", enable=False)
    return prg
