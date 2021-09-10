prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter repump Na Close", enable=False)
    prg.add(0, "Shutter 2DMOT Close", enable=False)
    prg.add(0, "Shutter 3DMOT cool Na Close", enable=False)
    prg.add(0, "Shutter EOM Na Close")
    prg.add(0, "Shutter Gray molasses Close", enable=False)
    prg.add(0, "Shutter Probe/Push Close", enable=False)
    prg.add(0, "Shutter Dark Spot Close", enable=False)
    prg.add(0, "Shutter repump Na Close", enable=False)
    prg.add(20000000, "Shutter repump Na Open", enable=False)
    prg.add(20000000, "Shutter Dark Spot Open", enable=False)
    prg.add(20000000, "Shutter Probe/Push Open", enable=False)
    prg.add(20000000, "Shutter Gray molasses Open", enable=False)
    prg.add(20000000, "Shutter EOM Na Open")
    prg.add(20000000, "Shutter 3DMOT cool Na Open", enable=False)
    prg.add(20000000, "Shutter 2DMOT Open", enable=False)
    prg.add(20000000, "Shutter repump Na Open", enable=False)
    prg.add(30000000, "EMPTY")
    return prg
