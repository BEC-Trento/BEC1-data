prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL0")
    prg.add(500, "Config Field OFF.sub")
    prg.add(10000, "Initialize 0 TTL3")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(68000000, "Na 3D MOT cool (-) Amp", 300.000000, enable=False)
    prg.add(68010000, "Delta 1 Current", 8.500000, enable=False)
    prg.add(70000000, "Rele 5 Close")
    prg.add(79000000, "Rele 5 Open")
    prg.add(79500000, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(79950000, "Melassa K amp.sub")
    prg.add(79950400, "Melassa K freq-short.sub")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off NaK.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(81000000, "All Shutter Close NaK.sub")
    prg.add(85000000, "Mirrors Imaging")
    prg.add(86000000, "All AOM On NaK.sub")
    prg.add(89000000, "B comp x", 248.000000)
    prg.add(90000000, "Evaporation Ramp.sub")
    prg.add(375000000, "Decompress Current MT.sub")
    prg.add(375010000, "Decompress Voltage MT.sub")
    prg.add(449000000, "Shutter OT x Open")
    prg.add(452000000, "Trigger OT ramp_x ON")
    prg.add(452000009, "Trigger OT ramp_x OFF")
    prg.add(473340000, "MT Off ramp_100ms.sub")
    prg.add(473865000, "B comp y", 1.870000)
    prg.add(475566000, "Trigger LZ ON")
    prg.add(475566400, "Trigger LZ OFF")
    prg.add(476570000, "Config Levitation F1+1.sub")
    prg.add(476770000, "Config Field OFF.sub")
    prg.add(476776000, "Picture NaK.sub")
    prg.add(479000000, "Shutter OT x Close")
    prg.add(501500000, "Set MOT NaK.sub")
    prg.add(502000000, "Dark Spot MOT load.sub")
    prg.add(502100000, "Config MOT.sub")
    prg.add(503000000, "Dipole Trap x (+) Amp", 1000.000000)
    prg.add(503100000, "Dipole Trap y (-) Amp", 1000.000000)
    prg.add(510000000, "All Shutter Open Na.sub")
    prg.add(515000000, "Shutter OT x Open", enable=False)
    return prg
