prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-310, "Repumper AOM TTL", enable=False)
    prg.add(-300, "Trig ON Stingray z", 'image0')
    prg.add(0, "Probe z AOM TTL")
    prg.add(151, "Trig OFF Stingray z")
    prg.add(1000000, "Shutter Probe/Push Close")
    prg.add(1150000, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000, enable=False)
    return prg
