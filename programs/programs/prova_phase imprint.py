prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(8000000, "phase imprint AOM warmup")
    prg.add(18000000, "phase imprint 2016 manual time", enable=False)
    prg.add(18000000, "phase imprint pulse_2016")
    return prg
def commands(cmd):
    a=[4,5,6]
    cmd.set_var("hhh", 4)
    cmd.run()
    while(cmd.running):
        a.pop()
        if len(a) == 0:
         cmd.stop()
    return cmd
