prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2050, "IGBT 4 Close")
    prg.add(-2040, "Delta 1 Voltage", 1.6000)
    prg.add(0, "IGBT 2 Open")
    prg.add(10, "IGBT 3 Close")
    prg.add(30, "IGBT 5 Open")
    prg.add(40, "Delta 1 Current", 12.000, functions=dict(value=lambda x: 2.232315e-6*cmd.get_var('tof')**3 - 1.164726e-3*cmd.get_var('tof')**2 + 1.986549e-1*cmd.get_var('tof') + 2.931988))
    prg.add(40, "Delta 1 Current", 0.000, functions=dict(value=lambda x: cmd.get_var('Levitation_current')), enable=False)
    prg.add(7940, "Ramp_bias_imaging")
    prg.add(8139, "Ramp_bias_imaging_dipole", functions=dict(time=lambda x: x+cmd.get_var('tof2')-cmd.get_var('t_cfo')-2.014), enable=False)
    return prg
