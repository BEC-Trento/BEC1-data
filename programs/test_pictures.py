prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(20000000, "Picture NaK.sub")
    prg.add(20000500, "TTL2-12 ON")
    prg.add(20000500, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(20100500, "TTL Repumper MOT ON", enable=False)
    prg.add(20200500, "TTL2-12 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(5, 20, 2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
