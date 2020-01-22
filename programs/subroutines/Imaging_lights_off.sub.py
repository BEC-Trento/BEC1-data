prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter repump Na Close")
    prg.add(2000, "Shutter Probe/Push Close")
    prg.add(5000, "Na Push (+) amp", 0)
    prg.add(5200, "Na Probe y (+) amp", 0)
    prg.add(5400, "Na Probe z (+) amp", 0)
    prg.add(5500, "Na Probe/Push (-) amp", 0)
    prg.add(5850, "TTL Probe y OFF")
    prg.add(5900, "TTL Probe z OFF")
    prg.add(6000, "TTL Push OFF")
    prg.add(7000, "TTL Repumper MOT OFF")
    prg.add(11200, "Na Repumper2 (+) Amp", 0)
    prg.add(11600, "Na Repumper1 (+) Amp", 0)
    return prg
