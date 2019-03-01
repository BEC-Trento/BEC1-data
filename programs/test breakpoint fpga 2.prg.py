prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(17000, "Trig ON Stingray 1")
    prg.add(22000, "Trig OFF Stingray 1")
    prg.add(47000, "BREAKPOINT")
    prg.add(48000, "NOP")
    prg.add(62000, "Trig ON Stingray 1")
    prg.add(65000, "Trig OFF Stingray 1")
    return prg
