prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(100000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(209000000, "Synchronize.sub", enable=False)
    prg.add(209943111, "MOT lights Off TTL.sub")
    prg.add(209947301, "Config Field OFF.sub")
    prg.add(209949001, "Gray Molasses 2017", enable=False)
    prg.add(209949001, "Optical pumping", enable=False)
    prg.add(209949011, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(220000000, "empty.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(200, 1001, 200)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        push_amp = iters[j]
        cmd.set_var('push_amp', push_amp)
        print('\n')
        print('Run #%d/%d, with variables:\npush_amp = %g\n'%(j+1, len(iters), push_amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
