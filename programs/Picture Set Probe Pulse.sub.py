prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Probe/Push (+) ON")
    prg.add(1000, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: cmd.get_var('tau'), funct_enable=False))
    return prg
