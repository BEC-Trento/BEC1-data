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
    prg.add(452003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(452010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(479010000, "empty.sub", enable=False)
    prg.add(484010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=4500.0000)
    prg.add(484020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=675, stop_t=4500)
    prg.add(554020000, "empty.sub", enable=False)
    prg.add(554021560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(554021617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(554021617, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(554021617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(554021617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(554021617, "Pulse uw ON")
    prg.add(554021617, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(554021651, "Picture NaK no Rep 20ms delay.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(554021651, "Picture NaK 20ms delay.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')), enable=False)
    prg.add(554051651, "Config Field OFF.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(569792076, "Set MOT NaK.sub")
    prg.add(570292076, "Dark Spot MOT load.sub")
    prg.add(570392076, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(20, 61, 10)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        t_uw1 = iters[j]
        cmd.set_var('t_uw', t_uw1)
        print('\n')
        print('Run #%d/%d, with variables:\nt_uw = %g\n'%(j+1, len(iters), t_uw1))
        cmd.run(wait_end=True, add_time=20000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
