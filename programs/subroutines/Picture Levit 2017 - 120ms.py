prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", 10.0000)
    prg.add(10, "IGBT 4 Close")
    prg.add(20, "Delta 1 Voltage", 5.0000)
    prg.add(2000, "Config Levitation zero current.sub")
    prg.add(2100, "Delta 1 Current", 14.800)
    prg.add(1190000, "Config Field OFF.sub")
    prg.add(1200000, "Picture NaK for Levit 2017.sub")
    prg.add(1200000, "Picture NaK for Levit 2017 Trig2.sub", enable=False)
    return prg
