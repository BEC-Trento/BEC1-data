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
    prg.add(129948920, "Melassa Na.sub")
    prg.add(129949920, "Melassa Na amp.sub")
    prg.add(129950420, "Config Field OFF.sub")
    prg.add(129998420, "MOT lights Off.sub")
    prg.add(130002420, "Delta 1 Current", 200.000)
    prg.add(130002430, "Delta 2 Voltage", 30.0000)
    prg.add(130002440, "Config MT compr.sub")
    prg.add(132006460, "All Shutter Close.sub")
    prg.add(135008460, "Mirrors Imaging")
    prg.add(135508460, "IGBT B comp x ON")
    prg.add(136008460, "All AOM On.sub")
    prg.add(139008460, "B comp x", 1000.0)
    prg.add(139998420, "Evaporation Ramp.sub")
    prg.add(577001420, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(577008420, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(595008420, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(653438420, "Config Field OFF.sub", enable=False)
    prg.add(653448420, "Picture NaK.sub", enable=False)
    prg.add(654288420, "RFO FM amp", 0.2000, enable=False)
    prg.add(654298420, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(654298420, "Bottom Evaporation ON", enable=False)
    prg.add(654298420, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(654788420, "Bottom Evaporation OFF", enable=False)
    prg.add(654808420, "RFO FM amp", 0.0000, enable=False)
    prg.add(684298420, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(684298420, "Picture - Field off at 0ms - Levit 180ms.sub")
    prg.add(686268420, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(688268420, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(688268420, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(692048420, "Set MOT NaK.sub")
    prg.add(692548420, "Dark Spot MOT load.sub")
    prg.add(692648420, "Config MOT.sub")
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
