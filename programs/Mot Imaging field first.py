prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1490000, "Trigger LZ ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22096000, "Config Field OFF.sub")
    prg.add(22100000, "MOT lights Off TTL short.sub")
    prg.add(22107000, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 2210.7000+cmd.get_var('tof')))
    prg.add(22110000, "empty.sub", enable=False)
    prg.add(27115000, "Set MOT NaK.sub")
    prg.add(27615000, "Dark Spot MOT load.sub")
    prg.add(27715000, "Config MOT.sub")
    prg.add(29010000, "Shutter Probe Na Open", enable=False)
    prg.add(29020000, "TTL2-12 OFF", enable=False)
    prg.add(29030000, "TTL2-12 ON", enable=False)
    prg.add(29040000, "TTL2-12 OFF", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 7, 0.5)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
