prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500, "Na Probe/Push (-) freq", 0.00, functions=dict(frequency=lambda x: 110 - cmd.get_var('probe_det_movies')/2))
    prg.add(0, "Na Probe y (+) freq", 0.00, functions=dict(frequency=lambda x: 110 + cmd.get_var('probe_det_movies')/2))
    return prg
