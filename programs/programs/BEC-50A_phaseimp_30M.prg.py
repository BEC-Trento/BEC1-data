prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(5000, "TTL3-11 ON")
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(89950500, "Melassa Na.sub")
    prg.add(89951500, "Melassa Na amp.sub")
    prg.add(89952000, "Config Field OFF.sub")
    prg.add(90000000, "MOT lights Off.sub")
    prg.add(90004000, "Delta 1 Current", 200.000)
    prg.add(90004010, "Delta 2 Voltage", 30.0000)
    prg.add(90004020, "Config MT compr.sub")
    prg.add(92008040, "All Shutter Close.sub")
    prg.add(95010040, "Mirrors Imaging")
    prg.add(95510040, "IGBT B comp x ON")
    prg.add(96010040, "All AOM On.sub")
    prg.add(99010040, "B comp x", 313.0)
    prg.add(100000000, "Evaporation Ramp.sub")
    prg.add(276003100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(276010100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(358320000, "Pulse uw ON")
    prg.add(358330100, "Phase Imprint Pulse.sub")
    prg.add(358335000, "RFO FM amp", 0.7000)
    prg.add(358340000, "Bottom Evaporation ON")
    prg.add(358540000, "Picture NaK no Rep.sub")
    prg.add(358640000, "Bottom Evaporation OFF")
    prg.add(358650000, "Pulse uw OFF")
    prg.add(358670100, "Picture - Field off at 0ms - Levit 50ms.sub", functions=dict(time=lambda x: x + cmd.get_var("t"), funct_enable=False), enable=False)
    prg.add(358670200, "Picture - Field off at 0ms - Levit 100ms.sub", functions=dict(time=lambda x: x +  + cmd.get_var("t"), funct_enable=False), enable=False)
    prg.add(370330200, "Set MOT NaK.sub")
    prg.add(370830200, "Dark Spot MOT load.sub")
    prg.add(370930200, "Config MOT.sub")
    prg.add(378790200, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(382120200, "Test imaging phase imprint 180ms", enable=False)
    prg.add(382120200, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(382120200, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(382170200, "Config Field OFF.sub", enable=False)
    prg.add(382180200, "Picture NaK.sub", enable=False)
    prg.add(382605162, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
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
