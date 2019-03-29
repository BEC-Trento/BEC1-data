prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-500, "General Trigger ON")
    prg.add(1500, "General Trigger OFF")
    prg.add(999500, "General Trigger ON")
    prg.add(1001500, "General Trigger OFF")
    prg.add(1999500, "General Trigger ON")
    prg.add(2001500, "General Trigger OFF")
    prg.add(2999500, "General Trigger ON")
    prg.add(3001500, "General Trigger OFF")
    return prg
