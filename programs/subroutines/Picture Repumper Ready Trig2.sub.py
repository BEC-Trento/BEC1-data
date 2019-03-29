prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100, "Trig ON Stingray 2", enable=False)
    prg.add(0, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000)
    prg.add(1000, "Trig ON Stingray 2")
    prg.add(2000, "Trig OFF Stingray 2")
    prg.add(999900, "Trig ON Stingray 2", enable=False)
    prg.add(1000000, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000)
    prg.add(1001000, "Trig ON Stingray 2")
    prg.add(1002000, "Trig OFF Stingray 2")
    prg.add(1999900, "Pulse Trig Stingray 2", polarity=1, pulse_t=0.26000)
    prg.add(2999900, "Pulse Trig Stingray 2", polarity=1, pulse_t=0.26000)
    return prg
