prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(200000, "Pulse TTL2-12", polarity=1, pulse_t=2.00000)
    prg.add(210000, "Pulse Freq sweep Probe Na", polarity=1, pulse_t=800.00000)
    prg.add(210500, "Pulse Probe Na", polarity=1, pulse_t=500.00000, enable=False)
    prg.add(210500, "Na Probe/Push (+) ON")
    prg.add(8310500, "empty.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.45, 5, 0.05)
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
