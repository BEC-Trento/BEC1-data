prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(232100000, "Synchronize.sub")
    prg.add(237000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(240000000, "B comp x", 665.0)
    prg.add(255000000, "Evaporation Ramp.sub")
    prg.add(512003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(512010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(534010000, "empty.sub")
    prg.add(539010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(539020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=4500)
    prg.add(594020000, "empty.sub")
    prg.add(596020000, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(596020000, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(596020000, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(596030000, "IGBT B comp x OFF", enable=False)
    prg.add(596035000, "Config Field OFF.sub", enable=False)
    prg.add(596045000, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(596045000, "Pulse uw ON")
    prg.add(596045100, "Pulse uw OFF")
    prg.add(596045134, "Picture NaK 20ms delay.sub", enable=False)
    prg.add(596045134, "Picture NaK no Rep 20ms delay.sub")
    prg.add(596075134, "Config Field OFF.sub")
    prg.add(611815559, "Set MOT NaK.sub")
    prg.add(612315559, "Dark Spot MOT load.sub")
    prg.add(612415559, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 14, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1 = iters[j]
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\n'%(j+1, len(iters), rep1))
        cmd.run(wait_end=True, add_time=21000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
