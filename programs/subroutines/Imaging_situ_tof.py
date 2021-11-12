prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "Setup_imaging")
    prg.add(0, "BEC_imaging_z_4_frames")
    prg.add(20000, "Dipole trap xy STANDBY")
    prg.add(21320, "Scope 2 Trigger ON")
    prg.add(22200, "Config Levitation dipole")
    prg.add(23010, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('tof2')-cmd.get_var('t_cfo')))
    prg.add(23010, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof2')+6))
    prg.add(35000, "B grad comp OFF")
    prg.add(53320, "Scope 2 Trigger OFF")
    prg.add(4579999, "IGBT B grad x OFF")
    return prg
