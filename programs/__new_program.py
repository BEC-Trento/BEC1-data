prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter Bragg D1 Open")
    prg.add(10000, "Bragg ON", enable=False)
    prg.add(10000, "Picture NaK.sub")
    return prg
