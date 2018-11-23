prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(202100000, "Synchronize.sub", enable=False)
    prg.add(207000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(210000000, "B comp x", 775.0)
    prg.add(225000000, "Evaporation Ramp.sub")
    prg.add(662003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(662010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(802010000, "empty.sub", enable=False)
    prg.add(807010000, "Config Field OFF.sub", enable=False)
    prg.add(807010000, "Picture Levit 2017 - 50ms")
    prg.add(822750425, "Set MOT NaK.sub")
    prg.add(823250425, "Dark Spot MOT load.sub")
    prg.add(823350425, "Config MOT.sub")
    return prg
