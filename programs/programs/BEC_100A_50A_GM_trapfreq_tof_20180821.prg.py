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
    prg.add(791230000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=2500)
    prg.add(826230000, "empty.sub", enable=False)
    prg.add(826231000, "Pulse TTL2-12", polarity=1, pulse_t=0.10000)
    prg.add(826331000, "B comp z ramp", start_t=0.0000, stop_x=1.500, n_points=50, start_x=1.005, stop_t=200.0000, enable=False)
    prg.add(826331000, "B comp y ramp", start_t=0, stop_x=0.5, n_points=50, start_x=0.07, stop_t=200)
    prg.add(828831000, "B comp z", 1.0050, enable=False)
    prg.add(828831000, "B comp y", 0.0700)
    prg.add(829331000, "empty.sub")
    prg.add(829332617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 20ms", functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(829332617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(829332617, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(829332617, "Picture NaK short delay.sub", enable=False)
    prg.add(829362617, "Config Field OFF.sub", enable=False)
    prg.add(829367617, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(829397617, "Config Field OFF.sub", enable=False)
    prg.add(845138042, "Set MOT NaK.sub")
    prg.add(845638042, "Dark Spot MOT load.sub")
    prg.add(845738042, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 170, 5)
    cmd.set_var('series', 4)
    j = 0
    while(cmd.running):
        delay1 = iters[j]
        cmd.set_var('delay', delay1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndelay = %g\n'%(j+1, len(iters), delay1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
