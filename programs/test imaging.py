prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Na 3D MOT cool (-) OFF", enable=False)
    prg.add(100000, "MOT lights Off TTL.sub")
    prg.add(1000000, "Mirrors Imaging")
    prg.add(8000000, "EMPTY")
    prg.add(9000000, "Trig ON Stingray 1", "'ciao'", enable=False)
    prg.add(9001000, "Trig OFF Stingray 1", enable=False)
    prg.add(9990000, "Synchronize.sub", enable=False)
    prg.add(10000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01448, functions=dict(time=lambda x: x-0.00154))
    prg.add(10000000, "Setup_imaging")
    prg.add(10000000, "BEC_fast_imaging_uw_z", enable=False)
    prg.add(10000000, "BEC_imaging_z", enable=False)
    prg.add(10000000, "Imaging_uw_movie", enable=False)
    prg.add(10000000, "Single_frame_imaging", enable=False)
    prg.add(10000000, "Single_frame_imaging_z", enable=False)
    prg.add(10000000, "BEC_imaging")
    prg.add(10200001, "Setup_tof_imaging", enable=False)
    prg.add(11000000, "BEC_imaging", enable=False)
    prg.add(35200001, "open_probe")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(10, 50, 10)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_z_amp = iters[j]
        cmd.set_var('probe_z_amp', probe_z_amp)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_z_amp = %g\n'%(j+1, len(iters), probe_z_amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
