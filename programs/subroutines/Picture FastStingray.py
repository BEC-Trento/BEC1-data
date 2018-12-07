prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1012300, "Picture SetRepumper")
    prg.add(-1002300, "Picture SetImaging")
    prg.add(-702300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-2800, "Na Probe/Push (+) ON")
    prg.add(-2600, "Na Probe/Push (+) OFF")
    prg.add(-1600, "TTL Repumper MOT ON")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(0, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1000, "Na Probe/Push (+) ON")
    prg.add(1200, "Na Probe/Push (+) OFF")
    prg.add(798600, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1598300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000, enable=False)
    return prg
