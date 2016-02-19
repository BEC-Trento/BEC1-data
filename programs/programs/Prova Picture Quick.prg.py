prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(1000000, "Set MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(10000000, "All Shutter Close.sub")
    prg.add(20000000, "Picture.sub", enable=False)
    prg.add(20000000, "Picture quick.sub")
    prg.add(20000500, "General Trigger ON")
    prg.add(30000000, "Set MOT.sub")
    return prg
