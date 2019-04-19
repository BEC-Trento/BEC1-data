prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(20000, "Set MOT NaK.sub")
    prg.add(509000, "Dark Spot MOT load.sub")
    prg.add(609000, "Config MOT.sub")
    prg.add(30605000, "Config Field OFF.sub")
    prg.add(30609000, "MOT lights Off TTL short.sub")
    prg.add(30609800, "TTL2-12 ON", enable=False)
    prg.add(30610800, "GrayMolassesPulse", enable=False)
    prg.add(30610900, "Gray Molasses 2017")
    prg.add(30710900, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 3066.0900+cmd.get_var('tof')))
    prg.add(37670600, "Set MOT NaK.sub")
    prg.add(38170600, "Dark Spot MOT load.sub")
    prg.add(38270600, "Config MOT.sub")
    prg.add(39565600, "Shutter Probe Na Open")
    return prg
