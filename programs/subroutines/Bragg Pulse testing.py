prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Mirrors Imaging Bragg")
    prg.add(5000, "Shutter Bragg Open")
    prg.add(6000, "Shutter Probe Na Open", enable=False)
    prg.add(23000000, "Bragg Pulse Single2015.sub", enable=False)
    prg.add(23000000, "Bragg Pulse Single New_20160509.sub")
    prg.add(23020000, "Picture NaK Bragg New_20160509.sub")
    prg.add(23020000, "Picture NaK Bragg Tom.sub", enable=False)
    prg.add(23020000, "Picture NaK.sub", enable=False)
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
