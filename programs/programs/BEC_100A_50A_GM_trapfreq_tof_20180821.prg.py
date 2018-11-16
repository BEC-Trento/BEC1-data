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
    prg.add(60000000, "B comp x", 665.0)
    prg.add(75000000, "Evaporation Ramp.sub")
    prg.add(512003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(512010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(652010000, "empty.sub", enable=False)
    prg.add(657010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=2500.0000)
    prg.add(657020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=2500)
    prg.add(692020000, "empty.sub", enable=False)
    prg.add(692021000, "Pulse TTL2-12", polarity=1, pulse_t=0.10000)
    prg.add(692121000, "B comp z ramp", start_t=0.0000, stop_x=1.500, n_points=50, start_x=1.005, stop_t=200.0000, enable=False)
    prg.add(692121000, "B comp y ramp", start_t=0, stop_x=0.5, n_points=50, start_x=0.07, stop_t=200, enable=False)
    prg.add(694621000, "B comp z", 1.0050, enable=False)
    prg.add(694621000, "B comp y", 0.0700, enable=False)
    prg.add(695121000, "empty.sub")
    prg.add(695122617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 20ms", functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(695122617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 80ms", functions=dict(time=lambda x: x + cmd.get_var('delay')), enable=False)
    prg.add(695122617, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(695122617, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(695122617, "Picture NaK short delay.sub", enable=False)
    prg.add(695152617, "Config Field OFF.sub", enable=False)
    prg.add(695157617, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(695187617, "Config Field OFF.sub", enable=False)
    prg.add(710928042, "Set MOT NaK.sub")
    prg.add(711428042, "Dark Spot MOT load.sub")
    prg.add(711528042, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 20, 1)
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
