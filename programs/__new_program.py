prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Scope 1 Trigger ON")
    prg.add(10, "Pulse uw ON")
    prg.add(50, "Pulse uw OFF")
    prg.add(500, "Scope 1 Trigger OFF")
    return prg
