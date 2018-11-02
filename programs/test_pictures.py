prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(11410080, "TTL2-12 ON")
    prg.add(12413530, "Picture NaK 20ms delay.sub")
    prg.add(12613940, "TTL2-12 OFF")
    prg.add(13613940, "Picture NaK for Levit 2017 Trig2.sub")
    prg.add(30000050, "startup.prg", enable=False)
    prg.add(30000050, "All AOM On.sub")
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
        cmd.run(wait_end=True, add_time=20000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
