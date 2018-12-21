prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(10000, "open Probe")
    prg.add(1010000, "Na Probe/Push (+) OFF", enable=False)
    prg.add(2010000, "Na Probe/Push (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(2110000, "Na Probe/Push (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    return prg
def commands(cmd):
    import numpy as np
    probe_amp_arr = [1000, 500, 300, 200, 150, 600, 800]
    probe_amp_arr = np.repeat(probe_amp_arr, 4)
    probe_tau_arr = [4, 5, 5, 10, 20, 4, 4]
    probe_tau_arr = np.repeat(probe_tau_arr, 4)
    iters = list(zip(probe_amp_arr, probe_tau_arr))
    np.random.shuffle(iters)
    print(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_amp1, probe_tau1 = iters[j]
        cmd.set_var('probe_amp', probe_amp1)
        cmd.set_var('probe_tau', probe_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_amp = %g\nprobe_tau = %g\n'%(j+1, len(iters), probe_amp1, probe_tau1))
        cmd.run(wait_end=True, add_time=3000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
