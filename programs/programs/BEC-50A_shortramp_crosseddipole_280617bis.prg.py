prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(7000, "TTL2-10 OFF")
    prg.add(7500, "Bx Grad ON", enable=False)
    prg.add(8000, "Pulse uw OFF")
    prg.add(10000, "TTL2 5 ON")
    prg.add(11000, "TTL3-11 ON")
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(120000, "Bx Grad OFF")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(10010000, "Optical Levit ON")
    prg.add(11010000, "Synchronize.sub", enable=False)
    prg.add(191010000, "Melassa Na.sub")
    prg.add(191011000, "Melassa Na amp.sub")
    prg.add(191011500, "Config Field OFF.sub")
    prg.add(191059500, "MOT lights Off.sub")
    prg.add(191063500, "Delta 1 Current", 200.000)
    prg.add(191063510, "Delta 2 Voltage", 30.0000)
    prg.add(191063520, "Config MT compr.sub")
    prg.add(193067540, "All Shutter Close.sub")
    prg.add(196069540, "Mirrors Imaging")
    prg.add(196569540, "IGBT B comp x ON")
    prg.add(197069540, "All AOM On.sub")
    prg.add(200069900, "B comp x", 600.0, functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(201059500, "Evaporation Ramp.sub")
    prg.add(250000000, "Bx Grad ON", enable=False)
    prg.add(301059500, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(375910100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(375917100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(436000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.500, n_points=500, start_x=0.000, stop_t=2000.0000, enable=False)
    prg.add(459367100, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=600, stop_t=250)
    prg.add(467381100, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=700.0000)
    prg.add(474391100, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.500, n_points=300, start_x=1.000, stop_t=100.0000)
    prg.add(475401100, "heating dipole", enable=False)
    prg.add(475411100, "B comp y ramp", start_t=0, stop_x=3, n_points=200, start_x=0, stop_t=130)
    prg.add(475411150, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(478411150, "LZ -1 to 0", enable=False)
    prg.add(520411150, "spin cleaning pinch", enable=False)
    prg.add(520411150, "Rabi preparation 2")
    prg.add(523511200, "ReleConfigBackForGravityComp")
    prg.add(524011200, "Rabi pulse New Antena", enable=False)
    prg.add(524315500, "B compensation ramp", start_t=0, stop_x=0.582, n_points=300, start_x=0.575, stop_t=200, functions=dict(stop_x=lambda x: cmd.get_var('finB'), funct_enable=False), enable=False)
    prg.add(524315500, "Bx Grad Pulse", enable=False)
    prg.add(524315500, "excite pinch")
    prg.add(525315500, "Dipole Trap x DAC V", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('dt')))
    prg.add(525321699, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(525321699, "Picture - Field off at 0ms -SternGerlach_Levit xms.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(525323199, "Picture - Field off at 0ms -SternGerlach_Ele.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(525323598, "TTL2-11 OFF", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(525483598, "Picture NaK.sub", functions=dict(time=lambda x: x+cmd.get_var('dt')))
    prg.add(525485098, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(525485098, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(525485098, "Picture - Field off at 0ms -SternGerlach_ShortElena2017.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(525545098, "Picture NaK.sub", enable=False)
    prg.add(525545098, "Picture NaK no Rep.sub", enable=False)
    prg.add(535555098, "Bx Grad OFF", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(535555198, "TTL2 5 OFF", enable=False)
    prg.add(547328597, "Bias field initialization", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(548179295, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(556413796, "Set MOT NaK.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(556913796, "Dark Spot MOT load.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(557013796, "Config MOT.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 500, 15)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
