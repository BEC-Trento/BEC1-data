prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(192600000, "Synchronize.sub", enable=False)
    prg.add(197600000, "All Shutter Close 2017.sub")
    prg.add(197601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(197601500, "Config Field OFF.sub")
    prg.add(197604500, "MOT lights Off close.sub")
    prg.add(197610000, "Mirrors Imaging")
    prg.add(197611734, "Gray Molasses 2017")
    prg.add(197671734, "empty.sub")
    prg.add(197671734, "Loading_GM_Q50_MTC200A")
    prg.add(199796644, "B comp x", 665.0)
    prg.add(200004999, "Bcomp y Sign Minus", enable=False)
    prg.add(202604999, "All AOM On.sub")
    prg.add(217604999, "Evaporation Ramp.sub")
    prg.add(654607999, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(654614999, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(783824999, "empty.sub")
    prg.add(788824999, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(788829999, "B comp x ramp", start_t=0, stop_x=750, n_points=200, start_x=665, stop_t=1200)
    prg.add(808829999, "Picture SetImaging")
    prg.add(808839999, "Picture SetRepumper")
    prg.add(813340249, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(814339999, "TTL2-12 ON", enable=False)
    prg.add(814340149, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('tau'), funct_enable=False))
    prg.add(814340179, "Picture NaK Ready no Rep.sub", enable=False)
    prg.add(814340179, "Picture NaK Ready no Rep Trig2.sub")
    prg.add(814365179, "Picture NaK Ready.sub")
    prg.add(814375179, "Config Field OFF.sub")
    prg.add(822157479, "TTL2-12 OFF", enable=False)
    prg.add(822257479, "Pulse uw OFF")
    prg.add(822258739, "Set MOT NaK.sub")
    prg.add(822757479, "Dark Spot MOT load.sub")
    prg.add(822857479, "Config MOT.sub")
    return prg
