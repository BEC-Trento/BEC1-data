prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(30000, "Na Push OFF")
    prg.add(30000000, "Na Probe x (+) freq", 120.00)
    prg.add(50000000, "Na Probe x (+) freq", 100.00)
    prg.add(70000000, "Na Probe x (+) freq", 120.00)
    prg.add(90000000, "Na Probe x (+) freq", 100.00)
    prg.add(110000000, "Na Probe x (+) freq", 110.00)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 500, 20)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_amp1 = iters[j]
        cmd.set_var('probe_amp', probe_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_amp = %g\n'%(j+1, len(iters), probe_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
