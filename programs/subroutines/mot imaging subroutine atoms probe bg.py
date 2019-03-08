prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5000900, "Shutter Probe Na Open")
    prg.add(-2700, "Na Probe/Push (+) OFF")
    prg.add(-2600, "TTL Repumper MOT ON")
    prg.add(-1600, "TTL Repumper MOT OFF")
    prg.add(-1500, "Trig ON Stingray 1")
    prg.add(-500, "Trig OFF Stingray 1")
    prg.add(0, "Na Probe/Push (+) ON")
    prg.add(100, "Na Probe/Push (+) OFF")
    prg.add(1000000, "Trig ON Stingray 1")
    prg.add(1001000, "Trig OFF Stingray 1")
    prg.add(1001500, "Na Probe/Push (+) ON")
    prg.add(1001600, "Na Probe/Push (+) OFF")
    prg.add(1002000, "Shutter Probe Na Close")
    prg.add(2016100, "Trig ON Stingray 1")
    prg.add(2017100, "Trig OFF Stingray 1")
    prg.add(3816100, "Na Probe/Push (+) ON")
    return prg
