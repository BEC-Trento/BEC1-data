prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22100000, "Synchronize.sub")
    prg.add(27000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(30000000, "B comp x", 675.0)
    prg.add(45000000, "Evaporation Ramp.sub")
    prg.add(482003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(482010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(622010000, "empty.sub", enable=False)
    prg.add(627010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=4500.0000)
    prg.add(627020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=675, stop_t=4500)
    prg.add(702020000, "empty.sub", enable=False)
    prg.add(702020000, "Picture SetImaging")
    prg.add(702030000, "Picture SetRepumper", enable=False)
    prg.add(702031560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(702031617, "Pulse uw ON")
    prg.add(702031617, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(702031651, "Picture Quantum - 1 shot Trig1", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(703031651, "Config Field OFF.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')), enable=False)
    prg.add(703031651, "Picture Levit 2017 - 30ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')), enable=False)
    prg.add(703031651, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')), enable=False)
    prg.add(703031651, "Picture Levit 2017 - 80ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(718772076, "Set MOT NaK.sub")
    prg.add(719272076, "Dark Spot MOT load.sub")
    prg.add(719372076, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 30, 1)
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
