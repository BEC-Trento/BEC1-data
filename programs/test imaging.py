prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL Probe y ON")
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Na 3D MOT cool (-) OFF", enable=False)
    prg.add(100000, "MOT lights Off TTL.sub")
    prg.add(1000000, "Mirrors Imaging")
    prg.add(8000000, "EMPTY")
    prg.add(9000000, "Trig ON Stingray 1", "'ciao'", enable=False)
    prg.add(9001000, "Trig OFF Stingray 1", enable=False)
    prg.add(9990000, "Synchronize.sub", enable=False)
    prg.add(10000000, "Setup_imaging")
    prg.add(10000000, "Imaging_uw_movie", enable=False)
    prg.add(10000000, "Single_frame_imaging", enable=False)
    prg.add(10000000, "Single_frame_imaging_z", enable=False)
    prg.add(10000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=100.44800, functions=dict(time=lambda x: x-0.04154), enable=False)
    prg.add(10200000, "BEC_imaging_field_lock", enable=False)
    prg.add(10200000, "BEC_imaging_z", enable=False)
    prg.add(10200000, "BEC_imaging_x", enable=False)
    prg.add(10200000, "BEC_imaging_xz", enable=False)
    prg.add(10200000, "BEC_imaging_xy")
    prg.add(10200000, "BEC_imaging_xyz", enable=False)
    prg.add(10200000, "BEC_imaging_fast", enable=False)
    prg.add(10200000, "multiple_RF_sweep_movie", enable=False)
    prg.add(10402349, "BEC_imaging", enable=False)
    prg.add(11400001, "Setup_tof_imaging", enable=False)
    prg.add(12200000, "BEC_imaging", enable=False)
    prg.add(36400001, "open_probe")
    prg.add(36419001, "Shutter EOM Na Open", enable=False)
    prg.add(40000000, "EMPTY")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 90, 10)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        dmd1_alpha = iters[j]
        cmd.set_var('dmd1_alpha', dmd1_alpha)
        print('\n')
        print('Run #%d/%d, with variables:\ndmd1_alpha = %g\n'%(j+1, len(iters), dmd1_alpha))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
