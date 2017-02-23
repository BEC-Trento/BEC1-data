prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(1000, "Trig OFF Stingray 1")
    prg.add(1000000, "Trig ON Stingray 1")
    prg.add(1001000, "Trig OFF Stingray 1")
    prg.add(2000000, "Trig ON Stingray 1")
    prg.add(2001000, "Trig OFF Stingray 1")
    prg.add(3000000, "Trig ON Stingray 1")
    prg.add(3001000, "Trig OFF Stingray 1")
    return prg
