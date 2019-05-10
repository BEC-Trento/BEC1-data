prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(20000, "Set MOT NaK.sub")
    prg.add(509000, "Dark Spot MOT load.sub")
    prg.add(609000, "Config MOT.sub")
    prg.add(60605000, "Config Field OFF.sub")
    prg.add(60609000, "MOT lights Off TTL short.sub")
    prg.add(60609800, "TTL2-12 ON")
    prg.add(60610800, "GrayMolassesPulse", enable=False)
    prg.add(60610900, "Gray Molasses 2017")
    prg.add(60620000, "TTL12 OFF")
    prg.add(60710900, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 6066.0900+cmd.get_var('tof')))
    prg.add(67000000, "Set MOT NaK.sub")
    prg.add(68170600, "Dark Spot MOT load.sub")
    prg.add(68270600, "Config MOT.sub")
    return prg
