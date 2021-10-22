prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-207209, "Pulse Trig Stingray z", comment="F1", polarity=1, pulse_t=0.10000, functions=dict(time=lambda x: x -20.1, funct_enable=False))
    prg.add(-5009, "Pulse uw with RF imaging extra", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')), enable=False)
    prg.add(-50, "Pulse uw with RF imaging m1", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(-50, "Pulse uw with RF imaging m1to0", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')), enable=False)
    prg.add(701, "Probe z AOM TTL")
    prg.add(3791, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.15445, functions=dict(time=lambda x: x- 1e-3*cmd.get_var('marconi1_pulsetime_p1')))
    prg.add(4991, "Pulse uw with RF imaging p1", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_p1')))
    prg.add(4991, "Pulse uw with RF imaging zero", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_p1')), enable=False)
    prg.add(4991, "Pulse uw with RF imaging p1to0", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_p1')), enable=False)
    prg.add(5701, "Probe z AOM TTL")
    prg.add(205798, "Pulse Trig Stingray z", comment="probe", polarity=1, pulse_t=0.35400, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(207300, "Probe z AOM TTL", functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(215889, "Na Probe/Push (-) amp", 0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(216890, "Na Probe z (+) amp", 0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(427823, "Shutter Probe/Push Close", functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ), enable=False)
    prg.add(592389, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    return prg
