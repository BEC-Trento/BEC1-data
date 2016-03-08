prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(7000000, "Phase Imprint Pulse.sub")
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
