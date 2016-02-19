prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(20000, "B comp y", 0.000000)
    prg.add(19000000, "B comp y", 1.000000)
    prg.add(20000000, "B comp x", 360.000000)
    prg.add(20500000, "IGBT B comp y ON")
    prg.add(21000000, "IGBT B comp x ON")
    prg.add(30000000, "Picture - Field off at 0ms - Levit 50ms.sub")
    prg.add(50000000, "Initialize 0 TTL and Synchronize.sub", enable=False)
    return prg
