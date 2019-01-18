prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(12210080, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(12211010, "Picture FastStingray")
    prg.add(12211010, "Picture FastStingray Trig2", enable=False)
    prg.add(12211010, "Picture FastStingray uw rep", enable=False)
    prg.add(12211010, "Picture FastStingray uw rep extra probe pic", enable=False)
    prg.add(13031010, "Picture FastStingray TOF Ready Trig2", enable=False)
    prg.add(13031010, "Picture close.sub", enable=False)
    prg.add(13031010, "Picture NaK - new Stingray", enable=False)
    prg.add(31627530, "All AOM On.sub")
    return prg
def commands(cmd):
    import numpy as np
    rep1 = np.arange(0,6,1)
    uw1 = [0.7, 1.8, 2.5]
    rep_arr, uw_tau_arr = np.meshgrid(rep1, uw1)
    iters = list(zip(rep_arr.ravel(), uw_tau_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1, uw_tau1 = iters[j]
        cmd.set_var('rep', rep1)
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\nuw_tau = %g\n'%(j+1, len(iters), rep1, uw_tau1))
        cmd.run(wait_end=True, add_time=35000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
