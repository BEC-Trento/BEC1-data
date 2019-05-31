prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(100010000, "Scope 2 Trigger ON")
    prg.add(100015000, "Scope 2 Trigger OFF")
    prg.add(100050000, "MOT lights Off TTL short.sub", functions=dict(time=lambda x: cmd.get_var('MOT_Load_time')*1000))
    prg.add(100054190, "Config Field OFF.sub", functions=dict(time=lambda x: cmd.get_var('MOT_Load_time')*1000 + 0.419))
    prg.add(100055890, "Gray Molasses 2017", functions=dict(time=lambda x: cmd.get_var('MOT_Load_time')*1000 + 0.589))
    prg.add(200111780, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: cmd.get_var('MOT_Load_time')*1000 + 5.589 + cmd.get_var('tof')))
    prg.add(210111780, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: cmd.get_var('MOT_Load_time')*1000 +1000), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 15, 1)
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
