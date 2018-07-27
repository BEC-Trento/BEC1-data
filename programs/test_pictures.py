prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(5300000, "Picture SetImaging", enable=False)
    prg.add(5310000, "Picture SetRepumper", enable=False)
    prg.add(5310000, "Picture SetRepumper2", enable=False)
    prg.add(11410080, "TTL2-12 ON")
    prg.add(11410100, "Picture NaK.sub")
    prg.add(11410110, "Picture NaK Ready.sub", enable=False)
    prg.add(11410510, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(11510510, "TTL Repumper MOT ON", enable=False)
    prg.add(11610510, "TTL2-12 OFF")
    return prg
