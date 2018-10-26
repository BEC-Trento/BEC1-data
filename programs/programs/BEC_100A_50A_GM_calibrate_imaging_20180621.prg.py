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
    prg.add(634010000, "empty.sub")
    prg.add(634010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(634014300, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=675, stop_t=4500)
    prg.add(694014300, "empty.sub")
    prg.add(694014300, "Config Levit 2017.sub", enable=False)
    prg.add(694016400, "Delta 1 Current", 10.000, enable=False)
    prg.add(694131400, "Pulse uw ON")
    prg.add(694131420, "Pulse uw OFF")
    prg.add(694131420, "IGBT B comp x OFF", enable=False)
    prg.add(694131420, "Config Field OFF.sub", enable=False)
    prg.add(694131420, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(694131770, "Picture NaK 20ms delay.sub", enable=False)
    prg.add(694131770, "Picture NaK no Rep 20ms delay.sub")
    prg.add(694161770, "Config Field OFF.sub")
    prg.add(709902195, "Set MOT NaK.sub")
    prg.add(710402195, "Dark Spot MOT load.sub")
    prg.add(710502195, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 5, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1 = iters[j]
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\n'%(j+1, len(iters), rep1))
        cmd.run(wait_end=True, add_time=20000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
