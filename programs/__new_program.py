prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter Gray molasses Open")
    prg.add(10000000, "Shutter Gray molasses Close")
    prg.add(20000000, "Shutter Gray molasses Open")
    return prg
