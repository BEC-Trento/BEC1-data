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
    prg.add(11411830, "Picture Quantum - 1 shot Trig1", enable=False)
    prg.add(12413530, "Picture NaK.sub", enable=False)
    prg.add(12413530, "Picture NaK short delay.sub", enable=False)
    prg.add(12413530, "Picture NaK 20ms delay.sub")
    prg.add(12413530, "Picture NaK no Rep 20ms delay.sub", enable=False)
    prg.add(12413540, "Picture NaK Ready.sub", enable=False)
    prg.add(12413940, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(12513940, "TTL Repumper MOT ON", enable=False)
    prg.add(12613940, "TTL2-12 OFF")
    prg.add(29000050, "startup.prg", enable=False)
    prg.add(29000050, "All AOM On.sub")
    return prg
