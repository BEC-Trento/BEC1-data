prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(20000, "Trig OFF Stingray 1")
    prg.add(10000000, "Trig ON Stingray 1")
    prg.add(10002000, "Trig OFF Stingray 1")
    prg.add(11000000, "Trig ON Stingray 1")
    prg.add(21002000, "Trig OFF Stingray 1")
    return prg
