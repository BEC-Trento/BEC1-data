prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3011000, "IGBT B comp y OFF", enable=False)
    prg.add(-201000, "B comp y", 0.0500, enable=False)
    prg.add(-40000, "IGBT B comp y ON", enable=False)
    prg.add(-500, "Trig ON Stingray 2")
    prg.add(0, "Pulse MOT beams", polarity=1, pulse_t=0.00500)
    prg.add(1050, "Trig OFF Stingray 2")
    prg.add(999500, "Trig ON Stingray 2")
    prg.add(1000000, "Pulse MOT beams", polarity=1, pulse_t=0.00500)
    prg.add(1001050, "Trig OFF Stingray 2")
    prg.add(1999500, "Trig ON Stingray 2")
    prg.add(2001050, "Trig OFF Stingray 2")
    prg.add(2999500, "Trig ON Stingray 2")
    prg.add(3001050, "Trig OFF Stingray 2")
    prg.add(3999550, "B comp y", 0.0000, enable=False)
    prg.add(4009550, "IGBT B comp y OFF", enable=False)
    return prg
