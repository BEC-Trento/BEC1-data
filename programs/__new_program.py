prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "RF sweep DAC V", 0.0000, functions=dict(value=lambda x: cmd.get_var('DAC_V')))
    return prg
