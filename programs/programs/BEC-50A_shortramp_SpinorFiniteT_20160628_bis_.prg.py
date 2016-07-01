prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(8000, "Pulse uw OFF")
    prg.add(11000, "TTL3-11 ON")
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(110000000, "Melassa Na.sub")
    prg.add(110001000, "Melassa Na amp.sub")
    prg.add(110001500, "Config Field OFF.sub")
    prg.add(110049500, "MOT lights Off.sub")
    prg.add(110053500, "Delta 1 Current", 200.000)
    prg.add(110053510, "Delta 2 Voltage", 30.0000)
    prg.add(110053520, "Config MT compr.sub")
    prg.add(112057540, "All Shutter Close.sub")
    prg.add(115059540, "Mirrors Imaging")
    prg.add(115559540, "IGBT B comp x ON")
    prg.add(116059540, "All AOM On.sub")
    prg.add(119059900, "B comp x", 1000.0)
    prg.add(120049500, "Evaporation Ramp.sub")
    prg.add(270049500, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(270050000, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(296052600, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(296059600, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(378364500, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(378369500, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(379369500, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(379369550, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(380799550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=100.0000)
    prg.add(380809550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=100.0000)
    prg.add(381009550, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(381019550, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(381219550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(381229550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(382829550, "LZ -1 to 0", enable=False)
    prg.add(387329550, "Rabi preparation 2", enable=False)
    prg.add(387329550, "MW repump preparation")
    prg.add(390379550, "spin cleaning pinch", enable=False)
    prg.add(393379550, "Bcomp y Sign Minus", enable=False)
    prg.add(394229600, "ReleConfigBackForGravityComp")
    prg.add(394229600, "ReleConfigBackForAntiGravityComp", enable=False)
    prg.add(394729600, "Rabi pulse New Antena", enable=False)
    prg.add(394729600, "Pulse uw ON", enable=False)
    prg.add(394729920, "Pulse uw OFF", enable=False)
    prg.add(395230420, "Dipole Trap y DAC V", -0.1000)
    prg.add(395230820, "Dipole Trap x DAC V", 0.0000)
    prg.add(395232820, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(395232820, "Picture -DipoleLoad-SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(395232820, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(395234820, "Picture NaK.sub")
    prg.add(395234820, "Picture NaK no Rep.sub", enable=False)
    prg.add(407108220, "Bias field initialization")
    prg.add(407858920, "Pulse uw OFF")
    prg.add(416093420, "Set MOT NaK.sub")
    prg.add(416593420, "Dark Spot MOT load.sub")
    prg.add(416693420, "Config MOT.sub")
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