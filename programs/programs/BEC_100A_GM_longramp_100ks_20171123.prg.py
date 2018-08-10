prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(3100000, "Synchronize.sub")
    prg.add(8000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(26000000, "Evaporation Ramp.sub")
    prg.add(403003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(403010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(429540000, "empty.sub", enable=False)
    prg.add(434540000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(434550000, "B comp x ramp", start_t=0, stop_x=750, n_points=200, start_x=665, stop_t=1200)
    prg.add(454550000, "empty.sub", enable=False)
    prg.add(454551560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(454551560, "TTL0-13 broken OFF", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(454551617, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(454551617, "Picture NaK short delay.sub")
    prg.add(454581617, "Config Field OFF.sub")
    prg.add(454586617, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(454616617, "Config Field OFF.sub", enable=False)
    prg.add(470357042, "Set MOT NaK.sub")
    prg.add(470857042, "Dark Spot MOT load.sub")
    prg.add(470957042, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.2, 3, 0.2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
