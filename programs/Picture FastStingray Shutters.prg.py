prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(0, "B comp y", 0.0000, enable=False)
    prg.add(142579, "B comp x", 0.0, enable=False)
    prg.add(179999, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(239999, "IGBT B comp y ON", enable=False)
    prg.add(1629999, "Set MOT NaK.sub", enable=False)
    prg.add(2129999, "Dark Spot MOT load.sub", enable=False)
    prg.add(2229999, "Config MOT.sub", enable=False)
    prg.add(3000000, "Na Probe/Push (+) ON")
    prg.add(3500000, "Shutter Probe Na Open")
    prg.add(18229999, "Na Probe/Push (+) OFF")
    prg.add(19700000, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.10000)
    prg.add(20329999, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau'), funct_enable=False))
    prg.add(20330199, "Na Probe/Push (+) OFF")
    prg.add(25330199, "TTL Repumper MOT ON")
    prg.add(25331699, "TTL Repumper MOT OFF")
    prg.add(25332199, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.31000)
    prg.add(25334199, "Na Probe/Push (+) ON")
    prg.add(25334499, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau'), funct_enable=False))
    prg.add(30334499, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.31000)
    prg.add(30344499, "Shutter Probe Na Close")
    prg.add(41344499, "Na Probe/Push (+) ON")
    return prg
