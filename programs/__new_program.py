prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(10000000, "Bx Grad OFF", enable=False)
    prg.add(10010000, "Bx Grad ON", enable=False)
    prg.add(10010010, "Bx Grad Pulse")
    prg.add(10050010, "Bx Grad OFF", enable=False)
    return prg
