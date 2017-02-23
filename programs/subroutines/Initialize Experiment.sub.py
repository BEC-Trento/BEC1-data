prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL0", enable=False)
    prg.add(0, "Initialize Test IGBT")
    prg.add(100, "Initialize 0 TTL2")
    prg.add(200, "Initialize 0 TTL3")
    prg.add(300, "Initialize 0 TTL4")
    prg.add(350, "Na 3D MOT cool (-) ON")
    prg.add(400, "Na Probe/Push (+) ON")
    prg.add(450, "Pulse MOT Na OFF")
    prg.add(8000, "Bcomp z Sign Plus")
    prg.add(9000, "Bcomp y Sign Plus")
    prg.add(10000, "Analog71", 0.3250)
    prg.add(10100, "B comp x", 1369.0)
    prg.add(15000, "Bx Grad OFF")
    return prg
