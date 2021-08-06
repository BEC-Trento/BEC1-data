prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-13150, "B grad comp OFF", functions=dict(time=lambda x: x+cmd.get_var('tof2')))
    prg.add(0, "Config Levitation dipole")
    prg.add(0, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('tof2')-cmd.get_var('t_cfo')))
    prg.add(0, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof2')))
    prg.add(0, "BEC_imaging_4_frames", functions=dict(time=lambda x: x+cmd.get_var('tof2')), enable=False)
    prg.add(5002201, "IGBT B grad x OFF", functions=dict(time=lambda x: x+cmd.get_var('tof2')+500))
    return prg
