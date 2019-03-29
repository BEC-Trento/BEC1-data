prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000500, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(-1600, "TTL Repumper MOT ON")
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(-37, "Pulse Freq sweep Probe Na", polarity=1, pulse_t=0.05000, enable=False)
    prg.add(0, "Picture Set Probe Pulse.sub")
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(999500, "Trig ON Stingray 1")
    prg.add(999963, "Pulse Freq sweep Probe Na", polarity=1, pulse_t=0.05000, enable=False)
    prg.add(1000000, "Picture Set Probe Pulse.sub")
    prg.add(1002000, "Trig OFF Stingray 1")
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2001500, "Trig OFF Stingray 1")
    prg.add(2999500, "Trig ON Stingray 1")
    prg.add(3001500, "Trig OFF Stingray 1")
    return prg
