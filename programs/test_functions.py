prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL2-12 ON")
    prg.add(10000, "Dipole y Func", start_t=0.0000, func_args="amp=5, freq=100", n_points=100, func="amp*sin(2*pi*freq*t)**2", stop_t=100.0000)
    prg.add(10000, "Pulse uw Func", start_t=0.0000, func_args="fr = 200, a=2", n_points=25, func="a*sin(2*pi*fr*t)**2 + 1", stop_t=100.0000, enable=False)
    prg.add(10050000, "TTL2-12 OFF")
    prg.add(30100000, "Dipole Trap y DAC V", 0.0000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 1, 0.05)
    j = 0
    while(cmd.running):
        x1 = iters[j]
        cmd.set_var('x', x1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
