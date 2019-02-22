prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Trig OFF Stingray 1")
    prg.add(10000, "Trig ON Stingray 1")
    prg.add(15000, "Trig OFF Stingray 1")
    prg.add(17000, "Shutter Gray molasses Close")
    prg.add(22000, "Shutter Gray molasses Open")
    prg.add(27000, "Shutter Gray molasses Close")
    prg.add(47000, "BREAKPOINT")
    prg.add(57000, "Trig ON Stingray 1")
    prg.add(60000, "Trig OFF Stingray 1")
    prg.add(62000, "Shutter Gray molasses Open")
    prg.add(65000, "Shutter Gray molasses Close")
    return prg
