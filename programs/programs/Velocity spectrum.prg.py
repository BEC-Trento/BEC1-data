prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "Na Repumper (+)", 500.000000)
    prg.add(110, "Na Repumper (+)", 1000.000000)
    prg.add(130, "Na Probe/Push", 500.000000)
    prg.add(10000, "Na Probe/Push", 400.000000)
    prg.add(70000, "Na Repumper (+)", 400.000000)
    prg.add(70010, "Na Repumper (+)", 900.000000)
    prg.add(80000, "Strobe load MOT 3D.sub")
    prg.add(320000, "Na Repumper (+)", 500.000000)
    prg.add(320010, "Na Repumper (+)", 1000.000000)
    prg.add(340000, "Na Repumper (+)", 1000.000000)
    prg.add(340010, "Na Repumper (+)", 500.000000)
    return prg
