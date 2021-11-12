prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1010000, "B comp x ramp", start_t=0, stop_x=5, n_points=50, start_x=cmd.get_var('Bx_dipole_trap'), stop_t=100)
    prg.add(-2050, "IGBT 4 Close")
    prg.add(-2040, "Delta 1 Voltage", 3.0000)
    prg.add(0, "IGBT 2 Open")
    prg.add(10, "IGBT 3 Close")
    prg.add(30, "IGBT 5 Open")
    prg.add(40, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=50, start_x=0.000, stop_t=200.0000, functions=dict(stop_x=lambda x: cmd.get_var('Gravity_current_comp')))
    return prg
