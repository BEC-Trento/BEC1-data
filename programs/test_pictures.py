prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(20000000, "Picture NaK.sub")
    prg.add(20000000, "Picture Stingray + Hamamatsu.sub", enable=False)
    prg.add(20000500, "TTL2-12 ON")
    prg.add(20000500, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(20100500, "TTL Repumper MOT ON", enable=False)
    prg.add(20200500, "TTL2-12 OFF")
    return prg
