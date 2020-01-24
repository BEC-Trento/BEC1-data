prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-509, "Na Probe z (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp')))
    prg.add(-500, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(0, "Pulse Probe z", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_z_pulsetime')))
    prg.add(500, "Na Probe/Push (-) amp", 0, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_z_pulsetime')))
    prg.add(509, "Na Probe z (+) amp", 0, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_z_pulsetime')))
    return prg