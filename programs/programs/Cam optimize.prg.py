prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(20, "Initialize 0 TTL2")
    prg.add(30, "Initialize 0 TTL4")
    prg.add(500, "Config Field OFF.sub")
    prg.add(10000, "Initialize 0 TTL3")
    prg.add(30000, "Shutter OT x Close")
    prg.add(50000, "All Shutter Open.sub")
    prg.add(100000, "Synchronize.sub")
    prg.add(1000000, "Bragg ON")
    prg.add(2000000, "Shutter Probe Na Open")
    prg.add(10030000, "Picture close NaK.sub")
    prg.add(15000000, "All AOM On.sub", enable=False)
    prg.add(16000000, "Shutter Probe Na Open", enable=False)
    prg.add(16500000, "Bragg ON", enable=False)
    return prg
