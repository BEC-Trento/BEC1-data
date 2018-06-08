prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(48420, "Optical Levit (-) Amp", 1000)
    prg.add(98420, "B comp y", 0.0000)
    prg.add(108420, "IGBT B comp y ON")
    prg.add(498420, "Bcomp y Sign Plus", enable=False)
    prg.add(1498420, "Set MOT NaK.sub")
    prg.add(1998420, "Dark Spot MOT load.sub")
    prg.add(2098420, "Config MOT.sub")
    prg.add(9998420, "Optical Levit ON")
    prg.add(169998920, "Melassa Na.sub")
    prg.add(169999920, "Melassa Na amp.sub")
    prg.add(170000420, "Config Field OFF.sub")
    prg.add(170048420, "MOT lights Off.sub", enable=False)
    prg.add(170052420, "Delta 1 Current", 200.000, enable=False)
    prg.add(170052430, "Delta 2 Voltage", 30.0000, enable=False)
    prg.add(170052440, "Config MT compr.sub", enable=False)
    prg.add(172056460, "All Shutter Close.sub", enable=False)
    prg.add(175058460, "Mirrors Imaging", enable=False)
    prg.add(175558460, "IGBT B comp x ON")
    prg.add(176058460, "All AOM On.sub")
    prg.add(179058460, "B comp x", 1052.0)
    prg.add(180000000, "Evaporation Ramp.sub", enable=False)
    prg.add(223703000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(223710000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(334798000, "Set MOT NaK.sub")
    prg.add(335298000, "Dark Spot MOT load.sub")
    prg.add(335398000, "Config MOT.sub")
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