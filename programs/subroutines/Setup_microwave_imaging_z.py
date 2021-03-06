prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-320000, "TTL Probe y OFF")
    prg.add(-310000, "TTL Probe z OFF")
    prg.add(-300000, "TTL Push OFF")
    prg.add(-290000, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp'), funct_enable=False))
    prg.add(-289500, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp'), funct_enable=False))
    prg.add(-289000, "Na Probe z (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp'), funct_enable=False))
    prg.add(-288000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_z_det')/2))
    prg.add(-287000, "Na Probe z (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_z_det')/2))
    prg.add(-280000, "Na Push (+) amp", 0)
    prg.add(-275000, "Na Push (+) freq", 60.00)
    prg.add(-150000, "Shutter Probe/Push Open")
    return prg
