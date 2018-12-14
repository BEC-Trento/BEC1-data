prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(12210080, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(12210110, "Picture FastStingray")
    prg.add(12210110, "Picture close.sub", enable=False)
    prg.add(12210110, "Picture NaK - new Stingray", enable=False)
    prg.add(30806630, "All AOM On.sub")
    return prg
def commands(cmd):
    import numpy as np
    probe_det_arr = np.arange(-20, 20, 2)
    probe_amp_arr = np.arange(0, 100, 1)
    iters = list(zip(probe_det_arr, probe_amp_arr))
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_det1, probe_amp1 = iters[j]
        cmd.set_var('probe_det', probe_det1)
        cmd.set_var('probe_amp', probe_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_det = %g\nprobe_amp = %g\n'%(j+1, len(iters), probe_det1, probe_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
