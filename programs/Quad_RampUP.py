prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "Delta 2 Current", 200.000, enable=False)
    prg.add(-500, "Delta 1 Voltage", 6.0000, enable=False)
    prg.add(-100, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=151, start_x=50.000, stop_t=2023.0000, functions=dict(start_x=lambda x: cmd.get_var('Quad_current')))
    prg.add(0, "Delta 1 Voltage ramp", start_t=0.0000, stop_x=28.000, n_points=151, start_x=20.000, stop_t=2023.0000)
    prg.add(5550000, "Delta 1 Voltage", 30.0000, enable=False)
    return prg
