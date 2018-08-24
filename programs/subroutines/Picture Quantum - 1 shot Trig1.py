prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(0, "Picture Set Probe Pulse.sub")
    prg.add(2000, "Trig OFF Stingray 1")
    return prg
