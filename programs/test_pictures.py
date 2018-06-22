prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(15000000, "Picture SetImaging")
    prg.add(15010000, "Picture SetRepumper")
    prg.add(15010000, "Picture SetRepumper2", enable=False)
    prg.add(20010000, "TTL2-12 ON")
    prg.add(20010100, "Picture NaK.sub", enable=False)
    prg.add(20010100, "Picture NaK Ready.sub")
    prg.add(20010500, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(20110500, "TTL Repumper MOT ON", enable=False)
    prg.add(20210500, "TTL2-12 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 200, 7)
    j = 0
    while(cmd.running):
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
