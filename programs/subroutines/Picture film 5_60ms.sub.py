prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-1200, "Na Probe/Push (+) freq", 110.000000)
    prg.add(-800, "Na Probe/Push (-) freq", 110.000000)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(254950, "TTL4-15 ON")
    prg.add(255000, "TTL4-15 OFF")
    prg.add(299500, "Trig ON Stingray 1")
    prg.add(300000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(301000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(302000, "Trig OFF Stingray 1")
    prg.add(854950, "TTL4-15 ON")
    prg.add(855000, "TTL4-15 OFF")
    prg.add(899500, "Trig ON Stingray 1")
    prg.add(900000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(901000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(901500, "Trig OFF Stingray 1")
    prg.add(1454950, "TTL4-15 ON")
    prg.add(1455000, "TTL4-15 OFF")
    prg.add(1499500, "Trig ON Stingray 1")
    prg.add(1500000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1501000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1501500, "Trig OFF Stingray 1")
    prg.add(2054950, "TTL4-15 ON")
    prg.add(2055000, "TTL4-15 OFF")
    prg.add(2099500, "Trig ON Stingray 1")
    prg.add(2100000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2101000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2101500, "Trig OFF Stingray 1")
    prg.add(2654950, "TTL4-15 ON")
    prg.add(2655000, "TTL4-15 OFF")
    prg.add(2699500, "Trig ON Stingray 1")
    prg.add(2700000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2701000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2701500, "Trig OFF Stingray 1")
    return prg