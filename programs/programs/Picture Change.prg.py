prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-9500, "B comp y ramp 0-5 1ms.sub")
    prg.add(0, "Config Field OFF ramp.sub")
    prg.add(10300, "Config Levitation F1+1.sub")
    prg.add(10450, "B comp x", 0.000000)
    prg.add(10500, "B comp y ramp 5-0 1ms.sub")
    prg.add(1195000, "Config Field OFF.sub")
    prg.add(1201000, "Picture.sub")
    return prg
