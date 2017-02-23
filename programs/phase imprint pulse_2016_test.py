prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5000000, "Shutter Bragg D1 Open")
    prg.add(-10000, "Bragg OFF")
    prg.add(0, "Bragg burst ON")
    prg.add(100000, "Bragg burst OFF")
    prg.add(110000, "Shutter Bragg D1 Close")
    return prg
