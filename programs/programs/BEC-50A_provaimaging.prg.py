prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(2000, "IGBT 6 Open")
    prg.add(3000, "Rele 5 Close")
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(109950500, "Melassa Na.sub")
    prg.add(109951500, "Melassa Na amp.sub")
    prg.add(109952000, "Config Field OFF.sub")
    prg.add(110000000, "MOT lights Off.sub")
    prg.add(110004020, "Config MT compr.sub")
    prg.add(110010000, "Picture NaK_2secondi.sub", enable=False)
    prg.add(110010000, "Picture NaK.sub")
    prg.add(130012200, "Set MOT NaK.sub")
    prg.add(130512200, "Dark Spot MOT load.sub")
    prg.add(130612200, "Config MOT.sub")
    return prg
def commands(cmd):
    from numpy import arange
    times=list(arange(0,20,1))
    times.reverse()
    while(cmd.running):
        print('actual: ', times[-1])
        print('real hold time : ', 1+times[-1])
        cmd.set_var("t", times.pop())
        print('Remaining: ',times)
        cmd.run()
        cmd.sleep(2000)
        if len(times) == 0:
         cmd.stop()
    return cmd