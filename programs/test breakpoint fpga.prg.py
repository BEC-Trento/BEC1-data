prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(1000, "Trig OFF Stingray 1")
    prg.add(2000, "TTL Repumper MOT OFF")
    prg.add(10000, "Trig ON Stingray 1")
    prg.add(15000, "Trig OFF Stingray 1")
    prg.add(17000, "TTL Repumper MOT ON")
    prg.add(22000, "TTL Repumper MOT OFF")
    prg.add(47000, "BREAKPOINT", enable=False)
    prg.add(48000, "NOP", enable=False)
    prg.add(57000, "Trig ON Stingray 1")
    prg.add(60000, "Trig OFF Stingray 1")
    prg.add(62000, "TTL Repumper MOT ON")
    prg.add(65000, "TTL Repumper MOT OFF")
    return prg
