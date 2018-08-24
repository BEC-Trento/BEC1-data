prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(197100000, "Synchronize.sub", enable=False)
    prg.add(202000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(205000000, "B comp x", 665.0)
    prg.add(220000000, "Evaporation Ramp.sub")
    prg.add(657003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(657010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(786220000, "empty.sub", enable=False)
    prg.add(791220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=2500.0000)
    prg.add(791230000, "B comp x ramp", start_t=0, stop_x=750, n_points=400, start_x=665, stop_t=2500)
    prg.add(826230000, "empty.sub")
    prg.add(826230000, "B comp x", 0.0, enable=False)
    prg.add(826230100, "IGBT B comp x OFF", enable=False)
    prg.add(826231660, "Pulse TTL2-12", polarity=1, pulse_t=0.10000)
    prg.add(826231660, "TTL0-13 broken OFF", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 30ms")
    prg.add(826231717, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(826231717, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(826231717, "Picture NaK short delay.sub", enable=False)
    prg.add(826261717, "Config Field OFF.sub", enable=False)
    prg.add(826266717, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(826296717, "Config Field OFF.sub", enable=False)
    prg.add(842037142, "Set MOT NaK.sub")
    prg.add(842537142, "Dark Spot MOT load.sub")
    prg.add(842637142, "Config MOT.sub")
    return prg
