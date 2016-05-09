prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Mirrors Imaging Bragg")
    prg.add(5000, "Shutter Bragg Open")
    prg.add(6000, "Shutter Probe Na Open", enable=False)
    prg.add(23000000, "Bragg Pulse Single2015.sub", enable=False)
    prg.add(23000000, "Bragg Pulse Single New_20160509.sub")
    prg.add(23060000, "Picture NaK Bragg New_20160509.sub")
    prg.add(23060000, "Picture NaK Bragg Tom.sub", enable=False)
    prg.add(23060000, "Picture NaK.sub", enable=False)
    return prg
