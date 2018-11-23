prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(11410080, "TTL2-12 ON")
    prg.add(12413530, "Picture NaK 20ms delay.sub", enable=False)
    prg.add(12613940, "TTL2-12 OFF")
    prg.add(13613940, "Picture NaK for Levit 2017 Trig2.sub", enable=False)
    prg.add(13613940, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(13613940, "Trig ON Stingray 1")
    prg.add(13623940, "Trig OFF Stingray 1")
    prg.add(30010050, "startup.prg", enable=False)
    prg.add(30010050, "All AOM On.sub")
    return prg
