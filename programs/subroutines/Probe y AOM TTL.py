prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-509, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-500, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(0, "Pulse Probe y", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_pulsetime')))
    prg.add(50, "Na Probe/Push (-) amp", 0, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_pulsetime')))
    prg.add(59, "Na Probe y (+) amp", 0, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_pulsetime')))
    return prg
