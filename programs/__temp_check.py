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
    prg.add(197601490, "TTL2-12 ON")
    prg.add(197601500, "Config Field OFF.sub")
    prg.add(197604500, "MOT lights Off close.sub")
    prg.add(197605000, "Mirrors Imaging")
    prg.add(197606735, "Gray Molasses 2017")
    prg.add(197666735, "empty.sub")
    prg.add(197666735, "Loading_GM_Q50_MTC200A")
    prg.add(199790000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(199791645, "B comp x", 915.0)
    prg.add(202600000, "All AOM On.sub")
    prg.add(217600000, "Evaporation Ramp.sub")
    prg.add(654603000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(654610000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(761900000, "empty.sub")
    prg.add(766900000, "TTL2-12 ON")
    prg.add(766910000, "Bx Grad ON")
    prg.add(767010000, "Bx Grad OFF")
    prg.add(767310000, "Pulse uw ON")
    prg.add(767310050, "Pulse uw OFF")
    prg.add(767351050, "Picture NaK.sub")
    prg.add(767653510, "Config Field OFF.sub")
    prg.add(772653510, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(772653510, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(772653510, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(772653510, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(772653510, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(774452510, "TTL2-12 ON", enable=False)
    prg.add(783672050, "TTL2-12 OFF")
    prg.add(783772050, "Pulse uw OFF")
    prg.add(783773310, "Set MOT NaK.sub")
    prg.add(784272050, "Dark Spot MOT load.sub")
    prg.add(784372050, "Config MOT.sub")
    return prg
