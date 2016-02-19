prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "B comp x", 2.000000)
    prg.add(20000, "B comp y", 2.000000)
    prg.add(30000000, "B comp x", 1.000000)
    prg.add(30020000, "B comp y", 1.000000)
    prg.add(60000000, "B comp x", 0.500000)
    prg.add(60010000, "B comp y", 0.500000)
    prg.add(90000000, "B comp x", 0.000000)
    prg.add(90010000, "B comp y", 0.000000)
    return prg
