prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(102579, "B comp x", 0.0)
    prg.add(139999, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(189999, "B comp y", 0.0000)
    prg.add(199999, "IGBT B comp y ON")
    prg.add(1589999, "Set MOT NaK.sub")
    prg.add(2089999, "Dark Spot MOT load.sub")
    prg.add(2189999, "Config MOT.sub")
    prg.add(2689999, "Na Probe/Push (+) ON")
    prg.add(3189999, "Shutter Probe Na Open")
    prg.add(18189999, "Na Probe/Push (+) OFF")
    prg.add(18289999, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.31000)
    prg.add(20289999, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau'), funct_enable=False))
    prg.add(20290199, "Na Probe/Push (+) OFF")
    prg.add(25290199, "TTL Repumper MOT ON")
    prg.add(25291699, "TTL Repumper MOT OFF")
    prg.add(25292199, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.31000)
    prg.add(25294199, "Na Probe/Push (+) ON")
    prg.add(25294499, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau'), funct_enable=False))
    prg.add(30294499, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.31000)
    prg.add(30304499, "Shutter Probe Na Close", enable=False)
    prg.add(41304499, "Na Probe/Push (+) ON")
    return prg
