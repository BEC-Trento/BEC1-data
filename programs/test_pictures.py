prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(15000000, "Picture SetImaging", enable=False)
    prg.add(15010000, "Picture SetRepumper", enable=False)
    prg.add(15010000, "Picture SetRepumper2", enable=False)
    prg.add(20110000, "TTL2-12 ON")
    prg.add(21110100, "Picture NaK.sub")
    prg.add(21110110, "Picture NaK Ready.sub", enable=False)
    prg.add(21110510, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(21210510, "TTL Repumper MOT ON", enable=False)
    prg.add(21310510, "TTL2-12 OFF")
    return prg
