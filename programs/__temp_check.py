prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(52100000, "Synchronize.sub")
    prg.add(57000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(60000000, "B comp x", 675.0)
    prg.add(75000000, "Evaporation Ramp.sub")
    prg.add(512003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(512010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(652010000, "empty.sub", enable=False)
    prg.add(657010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=6000.0000)
    prg.add(657020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=675, stop_t=6000)
    prg.add(727020000, "empty.sub", enable=False)
    prg.add(727021560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000)
    prg.add(727021660, "IGBT 1 pinch", 10.0000)
    prg.add(727021670, "IGBT 4 Close")
    prg.add(727021690, "Delta 1 Voltage", 5.0000)
    prg.add(727023690, "Config Levitation zero current.sub")
    prg.add(727024690, "B comp x", 3600.0)
    prg.add(727025790, "Delta 1 Current", 14.130)
    prg.add(728215790, "Pulse uw ON")
    prg.add(728215890, "Pulse uw OFF")
    prg.add(728215924, "Config Field OFF.sub")
    prg.add(728225924, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(728225924, "Picture NaK for Levit no Rep 2017.sub")
    prg.add(728225925, "empty.sub", enable=False)
    prg.add(728225925, "IGBT B comp x OFF", enable=False)
    prg.add(728256038, "Config Field OFF.sub")
    prg.add(743996463, "Set MOT NaK.sub")
    prg.add(744496463, "Dark Spot MOT load.sub")
    prg.add(744596463, "Config MOT.sub")
    return prg
