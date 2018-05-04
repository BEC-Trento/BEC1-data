prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(300000, "Mirrors Imaging")
    prg.add(20000000, "Picture NaK.sub", enable=False)
    prg.add(20000000, "Picture SetImaging")
    prg.add(20100213, "Picture SetRepumper")
    prg.add(20100213, "Picture Quantum - 1 shot Trig1")
    prg.add(21100213, "Picture Ramp Trig1", start_t=0.0000, stop_x=0.000, n_points=10, start_x=1.000, stop_t=180.0000)
    prg.add(23100213, "TTL2-12 ON")
    prg.add(23100213, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(23200213, "TTL Repumper MOT ON", enable=False)
    prg.add(23300213, "TTL2-12 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(188, 1000, 10)
    j = 0
    while(cmd.running):
        t1 = iters[j]
        cmd.set_var('t', t1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt = %g\n'%(j+1, len(iters), t1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
