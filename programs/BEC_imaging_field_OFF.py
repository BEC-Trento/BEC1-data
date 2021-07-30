prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2201, "B grad comp OFF", functions=dict(time=lambda x: x+0.7))
    prg.add(-2201, "IGBT B grad x OFF", functions=dict(time=lambda x: x+0.115))
    prg.add(-1200, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('tof2')-cmd.get_var('t_cfo')))
    prg.add(-1200, "Config Levitation dipole", functions=dict(time=lambda x: x+0.092))
    prg.add(0, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof2')), enable=False)
    prg.add(0, "BEC_imaging_4_frames", functions=dict(time=lambda x: x+cmd.get_var('tof2')))
    return prg
