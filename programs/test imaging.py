prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Na 3D MOT cool (-) OFF")
    prg.add(1000000, "Mirrors Imaging")
    prg.add(9000000, "Trig ON Stingray 1", enable=False)
    prg.add(9001000, "Trig OFF Stingray 1", enable=False)
    prg.add(10000000, "BEC_imaging", enable=False)
    prg.add(10000000, "DMD_imaging")
    prg.add(10000512, "Scope 1 Trigger ON", enable=False)
    prg.add(10000562, "Scope 1 Trigger OFF", enable=False)
    prg.add(20000000, "Na Probe/Push (+) ON")
    prg.add(20010000, "Shutter Probe Na Open")
    prg.add(20020000, "Na Probe/Push (+) Amp", 1000)
    prg.add(20030000, "Na Probe/Push (-) Amp", 1000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(500, 1050, 50)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Rep_amp1 = iters[j]
        cmd.set_var('Rep_amp', Rep_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\nRep_amp = %g\n'%(j+1, len(iters), Rep_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
