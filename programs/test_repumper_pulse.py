prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter repump Na Open")
    prg.add(20000, "Na 3D MOT cool (-) OFF")
    prg.add(30000, "Shutter 3DMOT cool Na Open")
    prg.add(1999000, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(1999100, "Pulse Repumper MOT", polarity=1, pulse_t=0.16000)
    prg.add(22999100, "TTL Repumper MOT OFF", enable=False)
    return prg
