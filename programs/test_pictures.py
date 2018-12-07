prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(12410080, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(12420444, "Picture NaK 20ms delay.sub", enable=False)
    prg.add(12420444, "Picture FastStingray")
    prg.add(12420444, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(12420444, "Picture NaK.sub", enable=False)
    prg.add(13620854, "Picture NaK for Levit 2017 Trig2.sub", enable=False)
    prg.add(13620854, "Trig ON Stingray 1", enable=False)
    prg.add(13630854, "Trig OFF Stingray 1", enable=False)
    prg.add(30016964, "startup.prg", enable=False)
    prg.add(31016964, "All AOM On.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 3, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1 = iters[j]
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\n'%(j+1, len(iters), rep1))
        cmd.run(wait_end=True, add_time=600)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
