prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(500000, "Bcomp y Sign Plus", enable=False)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(119950500, "Melassa Na.sub")
    prg.add(119951500, "Melassa Na amp.sub")
    prg.add(119952000, "Config Field OFF.sub")
    prg.add(120000000, "MOT lights Off.sub")
    prg.add(120004000, "Delta 1 Current", 200.000)
    prg.add(120004010, "Delta 2 Voltage", 30.0000)
    prg.add(120004020, "Config MT compr.sub")
    prg.add(122008040, "All Shutter Close.sub")
    prg.add(125010040, "Mirrors Imaging")
    prg.add(125510040, "IGBT B comp x ON")
    prg.add(126010040, "All AOM On.sub")
    prg.add(129010040, "B comp x", 340.0)
    prg.add(130000000, "Evaporation Ramp.sub")
    prg.add(567003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(567010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(585010000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(644290000, "RFO FM amp", 0.2000, enable=False)
    prg.add(644300000, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(644300000, "Bottom Evaporation ON", enable=False)
    prg.add(644300000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(644300000, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(644790000, "Bottom Evaporation OFF", enable=False)
    prg.add(644810000, "RFO FM amp", 0.0000, enable=False)
    prg.add(676270000, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(677280000, "Config Field OFF.sub", enable=False)
    prg.add(677380000, "Picture NaK.sub", enable=False)
    prg.add(678270000, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(678270000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(678270000, "Picture - Field off at 0ms - Levit 80ms.sub")
    prg.add(682050000, "Set MOT NaK.sub")
    prg.add(682550000, "Dark Spot MOT load.sub")
    prg.add(682650000, "Config MOT.sub")
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
