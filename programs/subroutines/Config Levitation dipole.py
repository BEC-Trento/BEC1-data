prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2050, "IGBT 4 Close")
    prg.add(-2040, "Delta 1 Voltage", 1.6000)
    prg.add(0, "IGBT 2 Open")
    prg.add(10, "IGBT 3 Close")
    prg.add(30, "IGBT 5 Open")
    prg.add(40, "Delta 1 Current", 0.000, functions=dict(value=lambda x: cmd.get_var('Levitation_current')))
    prg.add(8139, "Ramp_bias_imaging_dipole", functions=dict(time=lambda x: x+cmd.get_var('tof2')-cmd.get_var('t_cfo')-2.014))
    return prg
