prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1500, "Na Repumper2 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(-1000, "Na Repumper1 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(0, "TTL Repumper MOT ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(0, "TTL Repumper MOT OFF")
    prg.add(4, "Na Repumper2 (+) Amp", 0)
    prg.add(517, "Na Repumper1 (+) Amp", 0)
    return prg
