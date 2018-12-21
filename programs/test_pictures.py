prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(12210080, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(12210110, "Picture FastStingray", enable=False)
    prg.add(12210110, "Picture FastStingray uw rep")
    prg.add(12210110, "Picture close.sub", enable=False)
    prg.add(12210110, "Picture NaK - new Stingray", enable=False)
    prg.add(30806630, "All AOM On.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(25, 50, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_tau1 = iters[j]
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_tau = %g\n'%(j+1, len(iters), uw_tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
