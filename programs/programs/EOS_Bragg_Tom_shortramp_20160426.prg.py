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
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(109950500, "Melassa Na.sub")
    prg.add(109951500, "Melassa Na amp.sub")
    prg.add(109952000, "Config Field OFF.sub")
    prg.add(110000000, "MOT lights Off.sub")
    prg.add(110004000, "Delta 1 Current", 200.000)
    prg.add(110004010, "Delta 2 Voltage", 30.0000)
    prg.add(110004020, "Config MT compr.sub")
    prg.add(112008040, "All Shutter Close.sub")
    prg.add(115010040, "Mirrors Imaging", enable=False)
    prg.add(115010040, "Mirrors Imaging Bragg")
    prg.add(115510040, "IGBT B comp x ON")
    prg.add(116010040, "All AOM On.sub")
    prg.add(119010040, "B comp x", 1005.0)
    prg.add(120000000, "Evaporation Ramp.sub")
    prg.add(267620000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(267628230, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(378320000, "Picture - Field off at 0ms - Levit 50ms.sub")
    prg.add(378320220, "Pulse uw ON", enable=False)
    prg.add(378320220, "Pulse uw OFF", enable=False)
    prg.add(378322200, "Config Field OFF.sub", enable=False)
    prg.add(378332200, "Picture NaK.sub", enable=False)
    prg.add(378332200, "Na Repumper1 (+) Amp", 600, enable=False)
    prg.add(378410000, "Bragg Pulse Single2015.sub", enable=False)
    prg.add(378410000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(378462200, "Picture NaK Bragg Tom.sub", enable=False)
    prg.add(383962200, "Set MOT NaK.sub")
    prg.add(384462200, "Dark Spot MOT load.sub")
    prg.add(384562200, "Config MOT.sub")
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
