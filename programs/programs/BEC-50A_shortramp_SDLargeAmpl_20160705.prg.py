prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(8000, "Pulse uw OFF")
    prg.add(11000, "TTL3-11 ON")
    prg.add(12000, "Bx Grad OFF")
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(150000000, "Melassa Na.sub")
    prg.add(150001000, "Melassa Na amp.sub")
    prg.add(150001500, "Config Field OFF.sub")
    prg.add(150049500, "MOT lights Off.sub")
    prg.add(150053500, "Delta 1 Current", 200.000)
    prg.add(150053510, "Delta 2 Voltage", 30.0000)
    prg.add(150053520, "Config MT compr.sub")
    prg.add(152057540, "All Shutter Close.sub")
    prg.add(155059540, "Mirrors Imaging")
    prg.add(155559540, "IGBT B comp x ON")
    prg.add(156059540, "All AOM On.sub")
    prg.add(159059900, "B comp x", 1000.0)
    prg.add(160049500, "Evaporation Ramp.sub")
    prg.add(310049500, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(310050000, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(336052600, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(336059600, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(418364500, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(418369500, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(419369500, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(419369550, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(420799550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=100.0000)
    prg.add(420809550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=100.0000)
    prg.add(421009550, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(421019550, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(421219550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(421229550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(422829550, "LZ -1 to 0")
    prg.add(427329550, "Rabi preparation 2")
    prg.add(430379550, "spin cleaning pinch")
    prg.add(433379550, "Bcomp y Sign Minus", enable=False)
    prg.add(434229600, "ReleConfigBackForGravityComp")
    prg.add(434729600, "Rabi pulse New Antena")
    prg.add(434733895, "Dipole Trap y DAC V", -0.1000)
    prg.add(434734295, "Dipole Trap x DAC V", 0.0000)
    prg.add(434736295, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub")
    prg.add(434736295, "Picture - Field off at 0ms -SternGerlach_ShortTom15ms.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(434736295, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(434738295, "Picture NaK.sub", enable=False)
    prg.add(434738295, "Picture NaK no Rep.sub", enable=False)
    prg.add(446611695, "Bias field initialization")
    prg.add(447362395, "Pulse uw OFF")
    prg.add(447372395, "Bx Grad OFF")
    prg.add(455606895, "Set MOT NaK.sub")
    prg.add(456106895, "Dark Spot MOT load.sub")
    prg.add(456206895, "Config MOT.sub")
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