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
    prg.add(109950500, "Melassa Na.sub")
    prg.add(109951500, "Melassa Na amp.sub")
    prg.add(109952000, "Config Field OFF.sub")
    prg.add(110000000, "MOT lights Off.sub")
    prg.add(110004000, "Delta 1 Current", 200.000)
    prg.add(110004010, "Delta 2 Voltage", 30.0000)
    prg.add(110004020, "Config MT compr.sub")
    prg.add(112008040, "All Shutter Close.sub")
    prg.add(115010040, "Mirrors Imaging")
    prg.add(115510040, "IGBT B comp x ON")
    prg.add(116010040, "All AOM On.sub")
    prg.add(119010400, "B comp x", 1000.0)
    prg.add(120000000, "Evaporation Ramp.sub")
    prg.add(270000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(270000500, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(296003100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(296010100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(378315000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(378320000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(379320000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(379320050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(380750050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=100.0000)
    prg.add(380760050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=100.0000)
    prg.add(380960050, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(380970050, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(381170050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(381180050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(382780050, "LZ -1 to 0")
    prg.add(387280050, "Rabi preparation 2", enable=False)
    prg.add(387280050, "MW repump preparation")
    prg.add(390330050, "spin cleaning pinch")
    prg.add(393330050, "Bcomp y Sign Minus", enable=False)
    prg.add(394180100, "ReleConfigBackForGravityComp")
    prg.add(394180100, "ReleConfigBackForAntiGravityComp", enable=False)
    prg.add(394680100, "Rabi pulse New Antena", enable=False)
    prg.add(394680100, "Pulse uw ON")
    prg.add(394683100, "Pulse uw OFF")
    prg.add(394687400, "Dipole Trap y DAC V", -0.1000)
    prg.add(394687800, "Dipole Trap x DAC V", 0.0000)
    prg.add(394689800, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(394689800, "Picture -DipoleLoad-SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(394689800, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(394689800, "Picture NaK.sub", enable=False)
    prg.add(394689800, "Picture NaK no Rep.sub")
    prg.add(406563200, "Bias field initialization")
    prg.add(407313900, "Pulse uw OFF")
    prg.add(415548400, "Set MOT NaK.sub")
    prg.add(416048400, "Dark Spot MOT load.sub")
    prg.add(416148400, "Config MOT.sub")
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
