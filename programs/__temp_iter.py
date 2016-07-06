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
    prg.add(160000000, "Melassa Na.sub")
    prg.add(160001000, "Melassa Na amp.sub")
    prg.add(160001500, "Config Field OFF.sub")
    prg.add(160049500, "MOT lights Off.sub")
    prg.add(160053500, "Delta 1 Current", 200.000)
    prg.add(160053510, "Delta 2 Voltage", 30.0000)
    prg.add(160053520, "Config MT compr.sub")
    prg.add(162057540, "All Shutter Close.sub")
    prg.add(165059540, "Mirrors Imaging")
    prg.add(165559540, "IGBT B comp x ON")
    prg.add(166059540, "All AOM On.sub")
    prg.add(169059900, "B comp x", 1000.0)
    prg.add(170049500, "Evaporation Ramp.sub")
    prg.add(320049500, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(320050000, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(346052600, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(346059600, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(428364500, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(428369500, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(429369500, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(429369550, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(430799550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=100.0000)
    prg.add(430809550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=100.0000)
    prg.add(431009550, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(431019550, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(431219550, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(431229550, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(432829550, "LZ -1 to 0", enable=False)
    prg.add(437329550, "Rabi preparation 2")
    prg.add(440379550, "spin cleaning pinch", enable=False)
    prg.add(443379550, "Bcomp y Sign Minus", enable=False)
    prg.add(444229600, "ReleConfigBackForGravityComp")
    prg.add(444729600, "Rabi pulse New Antena", enable=False)
    prg.add(444733900, "Dipole Trap y DAC V", -0.1000)
    prg.add(444734300, "Dipole Trap x DAC V", 0.0000)
    prg.add(444736300, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms - Levit 20ms.sub")
    prg.add(444736300, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms -SternGerlach_ShortTom15ms.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(444736300, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(444738300, "Picture NaK.sub", enable=False)
    prg.add(444738300, "Picture NaK no Rep.sub", enable=False)
    prg.add(456611700, "Bias field initialization")
    prg.add(457362400, "Pulse uw OFF")
    prg.add(465596900, "Set MOT NaK.sub")
    prg.add(466096900, "Dark Spot MOT load.sub")
    prg.add(466196900, "Config MOT.sub")
    return prg
