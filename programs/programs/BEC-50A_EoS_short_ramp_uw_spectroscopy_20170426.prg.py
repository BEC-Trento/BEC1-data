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
    prg.add(9948420, "Optical Levit ON")
    prg.add(169955000, "Melassa Na.sub")
    prg.add(169956000, "Melassa Na amp.sub")
    prg.add(169956500, "Config Field OFF.sub")
    prg.add(170004500, "MOT lights Off.sub")
    prg.add(170008500, "Delta 1 Current", 200.000)
    prg.add(170008510, "Delta 2 Voltage", 30.0000)
    prg.add(170008520, "Config MT compr.sub")
    prg.add(172012540, "All Shutter Close.sub")
    prg.add(175014540, "Mirrors Imaging")
    prg.add(175510040, "IGBT B comp x ON")
    prg.add(176010040, "All AOM On.sub")
    prg.add(179010040, "B comp x", 938.0)
    prg.add(180000000, "Evaporation Ramp.sub")
    prg.add(356003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(356010100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(438320000, "Picture - Field off at 0ms - Levit 60ms.sub", enable=False)
    prg.add(446320000, "Pulse uw ON")
    prg.add(446321000, "Pulse uw OFF")
    prg.add(446321500, "Config Field OFF.sub")
    prg.add(446421500, "Picture NaK.sub", enable=False)
    prg.add(446421500, "Picture NaK no Rep.sub")
    prg.add(456421500, "Config Field OFF.sub")
    prg.add(465531500, "Set MOT NaK.sub")
    prg.add(466031500, "Dark Spot MOT load.sub")
    prg.add(466131500, "Config MOT.sub")
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
