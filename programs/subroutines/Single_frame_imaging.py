prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-310, "Repumper AOM TTL", enable=False)
    prg.add(-300, "Trig ON Stingray 1", "'image0'")
    prg.add(-200, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.00416, enable=False)
    prg.add(0, "Probe y AOM TTL")
    prg.add(100, "Trig OFF Stingray 1")
    prg.add(1000000, "Shutter Probe/Push Close", enable=False)
    prg.add(1150000, "Pulse Trig Stingray 1", comment="dark", polarity=1, pulse_t=0.10000, enable=False)
    return prg
