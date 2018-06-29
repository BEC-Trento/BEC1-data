prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(15000000, "Picture SetImaging")
    prg.add(15010000, "Picture SetRepumper")
    prg.add(15010000, "Picture SetRepumper2", enable=False)
    prg.add(20110000, "TTL2-12 ON")
    prg.add(20110100, "Picture NaK.sub", enable=False)
    prg.add(20110110, "Picture NaK Ready.sub")
    prg.add(20110510, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(20210510, "TTL Repumper MOT ON", enable=False)
    prg.add(20310510, "TTL2-12 OFF")
    return prg
