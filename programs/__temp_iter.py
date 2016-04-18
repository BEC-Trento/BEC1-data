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
    prg.add(119010400, "B comp x", 1025.0)
    prg.add(120000000, "Evaporation Ramp.sub")
    prg.add(270000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=7.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(270000500, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.800, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(296003100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(296010100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(378315000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1028, stop_t=250)
    prg.add(378320000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(379320000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(379320050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(380750050, "LZ -1 to 0")
    prg.add(385250050, "Rabi preparation 2")
    prg.add(388300050, "spin cleaning pinch")
    prg.add(391300050, "Bcomp y Sign Minus", enable=False)
    prg.add(392150100, "ReleConfigBackForGravityComp")
    prg.add(392150100, "ReleConfigBackForAntiGravityComp", enable=False)
    prg.add(392650100, "Rabi pulse New Antena")
    prg.add(392654399, "Dipole Trap y DAC V", -0.1000)
    prg.add(392654799, "Dipole Trap x DAC V", 0.0000)
    prg.add(392659799, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(392659799, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(392659799, "Picture -DipoleLoad-SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(392659799, "Picture - Field off at 0ms - Levit 30ms.sub")
    prg.add(392659799, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(392659799, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(392659799, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(392759799, "Picture NaK.sub", enable=False)
    prg.add(404633199, "Bias field initialization")
    prg.add(405383899, "Pulse uw OFF")
    prg.add(413618399, "Set MOT NaK.sub")
    prg.add(414118399, "Dark Spot MOT load.sub")
    prg.add(414218399, "Config MOT.sub")
    return prg
