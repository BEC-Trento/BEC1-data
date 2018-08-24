prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3520000, "Na Probe/Push (+) OFF")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3020000, "TTL Repumper MOT OFF")
    prg.add(-3013000, "Shutter repump Na Open")
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2010000, "Shutter 3DMOT cool Na Open")
    prg.add(-1000500, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(-199500, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-199000, "Na Repumper1 (+) Amp", 1000)
    prg.add(-101000, "Na Probe/Push (+) Amp", 1000)
    prg.add(-100500, "Na Probe/Push (-) Amp", 1000)
    prg.add(-91199, "Na Probe/Push (+) freq", 111.00)
    prg.add(-90800, "Na Probe/Push (-) freq", 109.25)
    prg.add(-1600, "TTL Repumper MOT ON")
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(-37, "Pulse Freq sweep Probe Na", polarity=1, pulse_t=0.05000)
    prg.add(0, "Pulse Probe Na", polarity=1, pulse_t=0.01000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(99500, "Trig ON Stingray 1")
    prg.add(99963, "Pulse Freq sweep Probe Na", polarity=1, pulse_t=0.05000)
    prg.add(100000, "Pulse Probe Na", polarity=1, pulse_t=0.01000)
    prg.add(102000, "Trig OFF Stingray 1")
    prg.add(110000, "Shutter Probe Na Close")
    prg.add(120000, "Na Repumper1 (+) Amp", 1)
    prg.add(199500, "Trig ON Stingray 1")
    prg.add(202000, "Trig OFF Stingray 1")
    prg.add(299500, "Trig ON Stingray 1")
    prg.add(302000, "Trig OFF Stingray 1")
    return prg
