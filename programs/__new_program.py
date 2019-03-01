prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(20000, "MOT lights Off TTL.sub")
    prg.add(10000000, "mot imaging subroutine atoms probe bg")
    return prg
