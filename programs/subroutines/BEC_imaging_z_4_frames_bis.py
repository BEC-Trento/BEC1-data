prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.10000, functions=dict(time=lambda x: x - 1e-3*cmd.get_var('cam_z1_ExposureTime') - 1e-3*cmd.get_var('marconi1_pulsetime_m1')+0.15))
    prg.add(0, "Pulse uw with RF imaging m1", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')-0.13))
    prg.add(0, "Probe z AOM TTL", functions=dict(time=lambda x: x- 1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(1100, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.15445, functions=dict(time=lambda x: x- 1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(1200, "Pulse uw with RF imaging p1", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(1250, "Probe z AOM TTL", functions=dict(time=lambda x: x- 1e-3*cmd.get_var('marconi1_pulsetime_m1') + 1e-3*cmd.get_var('marconi1_pulsetime_p1')))
    prg.add(10008, "Pulse Trig Stingray z", comment="probe", polarity=1, pulse_t=0.35400, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(11510, "Probe z AOM TTL", functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(20099, "Na Probe/Push (-) amp", 0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(21100, "Na Probe z (+) amp", 0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(232033, "Shutter Probe/Push Close", functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    prg.add(396599, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000, functions=dict(time=lambda x: x+1e-3*cmd.get_var('cam_z1_ExposureTime') ))
    return prg
