prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(5300000, "Picture SetImaging", enable=False)
    prg.add(5310000, "Picture SetRepumper", enable=False)
    prg.add(5310000, "Picture SetRepumper2", enable=False)
    prg.add(11410080, "TTL2-12 ON")
    prg.add(11411780, "Picture Quantum - 1 shot Trig1", enable=False)
    prg.add(12411780, "Picture Quantum - 1 shot Trig1", enable=False)
    prg.add(13413480, "Picture NaK.sub", enable=False)
    prg.add(13413480, "Picture NaK short delay.sub")
    prg.add(13413490, "Picture NaK Ready.sub", enable=False)
    prg.add(13413890, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(13513890, "TTL Repumper MOT ON", enable=False)
    prg.add(13613890, "TTL2-12 OFF")
    return prg
