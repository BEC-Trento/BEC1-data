prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Config Field OFF.sub")
    prg.add(3000, "TTL Fluo Lock OFF")
    prg.add(13000, "Initialize 0 TTL0", enable=False)
    prg.add(13100, "Initialize Test IGBT", enable=False)
    prg.add(13200, "Initialize 0 TTL2", enable=False)
    prg.add(13300, "Initialize 0 TTL3", enable=False)
    prg.add(13400, "Initialize 0 TTL4", enable=False)
    prg.add(18450, "Na 3D MOT cool (-) ON", enable=False)
    prg.add(18500, "TTL Push ON", enable=False)
    prg.add(18550, "Pulse MOT Na OFF", enable=False)
    prg.add(44700, "Synchronize.sub")
    return prg
