prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(510, "Mirrors Imaging")
    prg.add(1000, "Config Field OFF.sub", enable=False)
    prg.add(11500, "TTL3-11 ON")
    prg.add(48920, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(98920, "B comp y", 0.0000)
    prg.add(108920, "IGBT B comp y ON")
    prg.add(498920, "Bcomp y Sign Plus", enable=False)
    prg.add(1498920, "Set MOT NaK.sub", enable=False)
    prg.add(1998920, "Dark Spot MOT load.sub", enable=False)
    prg.add(2098920, "Config MOT.sub", enable=False)
    prg.add(9998920, "Melassa Na.sub", enable=False)
    prg.add(9999920, "Melassa Na amp.sub", enable=False)
    prg.add(10000420, "Config Field OFF.sub")
    prg.add(10048420, "MOT lights Off.sub")
    prg.add(15054440, "Mirrors Imaging")
    prg.add(16054440, "All AOM On.sub")
    prg.add(21054440, "Picture NaK.sub", enable=False)
    prg.add(21054440, "Picture NaK Repump Off.sub")
    prg.add(21054440, "Picture NaK Hamamatsu.sub", enable=False)
    prg.add(21057860, "Picture - Field off at 0ms - Levit 50ms - Hamamatsu.sub", enable=False)
    prg.add(28826280, "Set MOT NaK.sub", enable=False)
    prg.add(29326280, "Dark Spot MOT load.sub", enable=False)
    prg.add(29426280, "Config MOT.sub", enable=False)
    return prg
def commands(cmd):
    from numpy import arange
    times=list(arange(0,20,1))
    times.reverse()
    while(cmd.running):
        print('actual: ', times[-1])
        print('real hold time : ', 1+times[-1])
        cmd.set_var("t", times.pop())
        print('Remaining: ',times)
        cmd.run()
        cmd.sleep(2000)
        if len(times) == 0:
         cmd.stop()
    return cmd
