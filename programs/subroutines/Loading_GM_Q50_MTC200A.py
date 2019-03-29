prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(220, "Config MOT.sub")
    prg.add(24910, "Delta 1 Voltage", 15.0000)
    prg.add(2024910, "Config MOT to MT compr.sub")
    prg.add(2124910, "B comp x", 0.0, enable=False)
    prg.add(7834910, "Delta 1 Voltage", 30.0000)
    prg.add(7934910, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=1800, start_x=50.000, stop_t=900.0000)
    prg.add(7937410, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=450, start_x=0.000, stop_t=900.0000)
    return prg
