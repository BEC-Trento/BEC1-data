prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(2500, "Trig OFF Stingray 1")
    prg.add(200000, "Trig ON Stingray 2")
    prg.add(202500, "Trig OFF Stingray 2")
    return prg
