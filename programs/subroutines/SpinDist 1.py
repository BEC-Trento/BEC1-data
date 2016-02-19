prg_comment = "Spin distillation |1, /pm 1>"
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-700000, "Config Feshbach.sub")
    prg.add(-210000, "RFO", 0)
    prg.add(-200000, "Delta 1 Current ramp", start_t=0.0000, stop_x=11.600, n_points=50, start_x=0.000, stop_t=20.0000)
    prg.add(-150000, "B comp x", 0.0)
    prg.add(0, "Delta 1 Current ramp", start_t=0.0000, stop_x=11.800, n_points=70, start_x=11.600, stop_t=30.0000)
    prg.add(300000, "RFO2 Amp", 1)
    prg.add(310000, "B comp x", 1000.0)
    prg.add(320000, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=50, start_x=11.800, stop_t=30.0000)
    prg.add(790000, "RFO2 freq", 0.700)
    prg.add(800000, "RFO2 Amp", 1000)
    prg.add(803000, "RFO2 Amp", 1)
    return prg
