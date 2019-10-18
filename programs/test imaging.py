prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Na 3D MOT cool (-) OFF", enable=False)
    prg.add(1000000, "Mirrors Imaging")
    prg.add(9000000, "Trig ON Stingray 1", enable=False)
    prg.add(9001000, "Trig OFF Stingray 1", enable=False)
    prg.add(9990000, "Synchronize.sub", enable=False)
    prg.add(10000000, "BEC_imaging")
    prg.add(10000000, "BEC_fast_imaging_uw_z", enable=False)
    prg.add(10000512, "Scope 1 Trigger ON", enable=False)
    prg.add(10000562, "Scope 1 Trigger OFF", enable=False)
    prg.add(10010000, "Scope 2 Trigger ON")
    prg.add(10011000, "Scope 2 Trigger OFF")
    prg.add(30000000, "TTL Probe y ON")
    prg.add(30010000, "Shutter Probe/Push Open")
    prg.add(30020000, "Na Probe/Push (-) amp", 1000)
    prg.add(30030000, "Na Probe y (+) amp", 1000)
    prg.add(70000000, "TTL Probe y ON", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    gain = [10, 12, 16, 20, 24]
    amp = np.arange(120, 500, 20)
    cam4_Gain_arr, probe_amp_arr = np.meshgrid(gain, amp)
    iters = list(zip(cam4_Gain_arr.ravel(), probe_amp_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        cam4_Gain1, probe_amp1 = iters[j]
        cmd.set_var('cam4_Gain', cam4_Gain1)
        cmd.set_var('probe_amp', probe_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\ncam4_Gain = %g\nprobe_amp = %g\n'%(j+1, len(iters), cam4_Gain1, probe_amp1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
