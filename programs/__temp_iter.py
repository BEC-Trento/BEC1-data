prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(100104000, "MOT lights Off TTL.sub")
    prg.add(100104200, "Config Field OFF.sub")
    prg.add(100105300, "Scope 2 Trigger ON")
    prg.add(100105900, "Gray Molasses 2017")
    prg.add(100156899, "Load_Quad")
    prg.add(100166899, "Quad_RampUP")
    prg.add(105170399, "Quad_RampDOWN", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime')))
    prg.add(105170499, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False), enable=False)
    prg.add(125170399, "Config Field OFF.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime')+2000.5))
    prg.add(125220399, "BEC_imaging", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime')+2000.5+cmd.get_var('tof')))
    prg.add(165734399, "Scope 2 Trigger OFF")
    prg.add(174744399, "Scope 1 Trigger OFF")
    prg.add(175744399, "DarkSpotMOT_19.sub", enable=False)
    return prg
