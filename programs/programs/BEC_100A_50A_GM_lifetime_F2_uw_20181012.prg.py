prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(242100000, "Synchronize.sub")
    prg.add(247000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(250000000, "B comp x", 675.0)
    prg.add(265000000, "Evaporation Ramp.sub")
    prg.add(702003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(702010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(851220000, "empty.sub")
    prg.add(851220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(851224300, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=675, stop_t=4500)
    prg.add(911224300, "empty.sub")
    prg.add(911224300, "Pulse uw ON")
    prg.add(911224340, "Pulse uw OFF")
    prg.add(911224340, "Picture NaK for Levit no Rep 2017.sub", functions=dict(time=lambda x: x + cmd.get_var('wait')))
    prg.add(911224340, "Picture NaK for Levit 2017.sub", functions=dict(time=lambda x: x + cmd.get_var('wait')), enable=False)
    prg.add(911254340, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('wait')))
    prg.add(911254350, "Config Levit 2017.sub", enable=False)
    prg.add(911256450, "Delta 1 Current", 13.400, enable=False)
    prg.add(911257450, "IGBT B comp x OFF", enable=False)
    prg.add(911317450, "Config Field OFF.sub", enable=False)
    prg.add(911327950, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(927098375, "Set MOT NaK.sub")
    prg.add(927598375, "Dark Spot MOT load.sub")
    prg.add(927698375, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.03, 1, 0.1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        wait1 = iters[j]
        cmd.set_var('wait', wait1)
        print('\n')
        print('Run #%d/%d, with variables:\nwait = %g\n'%(j+1, len(iters), wait1))
        cmd.run(wait_end=True, add_time=45000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
