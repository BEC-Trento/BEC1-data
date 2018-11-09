prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(62100000, "Synchronize.sub")
    prg.add(67000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(70000000, "B comp x", 675.0)
    prg.add(85000000, "Evaporation Ramp.sub")
    prg.add(522003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(522010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(662010000, "empty.sub")
    prg.add(662010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(662014300, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=675, stop_t=4500)
    prg.add(722014300, "empty.sub")
    prg.add(722129300, "Pulse uw ON", enable=False)
    prg.add(722129320, "Pulse uw OFF", enable=False)
    prg.add(722129354, "Picture NaK no Rep 20ms delay.sub", enable=False)
    prg.add(722159354, "Config Field OFF.sub", enable=False)
    prg.add(722159354, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(722169354, "B comp x", 2.0, enable=False)
    prg.add(722179354, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(722179354, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(722179354, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(722179354, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(722179354, "Picture Levit 2017 - 80ms")
    prg.add(722179354, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(737919779, "Set MOT NaK.sub")
    prg.add(738419779, "Dark Spot MOT load.sub")
    prg.add(738519779, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 6, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1 = iters[j]
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\n'%(j+1, len(iters), rep1))
        cmd.run(wait_end=True, add_time=12000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
