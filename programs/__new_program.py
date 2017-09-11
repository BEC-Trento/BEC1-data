prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub")
    prg.add(200000, "All AOM On.sub", enable=False)
    prg.add(200000, "Set MOT NaK.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(30000000, "Picture NaK.sub")
    return prg
