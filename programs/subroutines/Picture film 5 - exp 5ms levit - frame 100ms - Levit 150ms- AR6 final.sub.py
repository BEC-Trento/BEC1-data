prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4278000, "Shutter Probe Na Open")
    prg.add(-3788000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-3778000, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-1000000, "Optical Levit ON")
    prg.add(-276200, "Na Probe/Push (+) freq", 110.000000)
    prg.add(-275800, "Na Probe/Push (-) freq", 110.000000)
    prg.add(-275500, "Trig ON Stingray 1")
    prg.add(-275400, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(-275000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(-274000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-273500, "Trig OFF Stingray 1")
    prg.add(-140, "Pulse uw ON")
    prg.add(0, "Pulse uw OFF")
    prg.add(54500, "Trig ON Stingray 1")
    prg.add(55000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(56000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(56500, "Trig OFF Stingray 1")
    prg.add(141060, "Optical Levit ON")
    prg.add(999990, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1001000, "Optical Levit OFF")
    prg.add(1049500, "Trig ON Stingray 1")
    prg.add(1050000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1051000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1051500, "Trig OFF Stingray 1")
    prg.add(1132060, "Optical Levit ON")
    prg.add(1999990, "Pulse uw ON")
    prg.add(2000000, "Pulse uw OFF")
    prg.add(2001000, "Optical Levit OFF")
    prg.add(2049500, "Trig ON Stingray 1")
    prg.add(2050000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2051000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2051500, "Trig OFF Stingray 1")
    prg.add(2098000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(2108000, "K probe Repumper (+) Amp", 1.000000)
    prg.add(2118000, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(2132060, "Optical Levit ON")
    prg.add(2138000, "Na Dark Spot Amp", 1.000000)
    prg.add(2148000, "Na Repumper MOT Amp", 1.000000)
    prg.add(2988000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2999990, "Pulse uw ON")
    prg.add(3000000, "Pulse uw OFF")
    prg.add(3001000, "Optical Levit OFF")
    prg.add(3049500, "Trig ON Stingray 1")
    prg.add(3050000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(3051000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3051500, "Trig OFF Stingray 1")
    prg.add(3132060, "Optical Levit ON")
    prg.add(3468000, "Shutter Probe K Open")
    prg.add(3478000, "Shutter RepumperMOT K Open")
    prg.add(3488000, "Shutter repump Na Open")
    prg.add(3999990, "Pulse uw ON")
    prg.add(4000000, "Pulse uw OFF")
    prg.add(4001000, "Optical Levit OFF")
    prg.add(4008000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(4049500, "Trig ON Stingray 1")
    prg.add(4050000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(4051000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(4051500, "Trig OFF Stingray 1")
    prg.add(4132060, "Optical Levit ON")
    prg.add(4471000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(4475700, "Optical Levit OFF")
    prg.add(4481000, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(4501000, "Shutter 3DMOT cool Na Open")
    prg.add(4510000, "Shutter Optical Levit Close")
    prg.add(4990500, "B comp y", 0.000000)
    prg.add(4991030, "B comp y", 0.260000)
    prg.add(4991550, "B comp y", 0.530000)
    prg.add(4992080, "B comp y", 0.790000)
    prg.add(4992610, "B comp y", 1.050000)
    prg.add(4993130, "B comp y", 1.320000)
    prg.add(4993660, "B comp y", 1.580000)
    prg.add(4994180, "B comp y", 1.840000)
    prg.add(4994710, "B comp y", 2.110000)
    prg.add(4995240, "B comp y", 2.370000)
    prg.add(4995760, "B comp y", 2.630000)
    prg.add(4996290, "B comp y", 2.890000)
    prg.add(4996820, "B comp y", 3.160000)
    prg.add(4997340, "B comp y", 3.420000)
    prg.add(4997870, "B comp y", 3.680000)
    prg.add(4998390, "B comp y", 3.950000)
    prg.add(4998920, "B comp y", 4.210000)
    prg.add(4999450, "B comp y", 4.470000)
    prg.add(4999970, "B comp y", 4.740000)
    prg.add(5000000, "IGBT 1 pinch", -10.000000)
    prg.add(5000020, "IGBT 3 Open")
    prg.add(5000060, "IGBT 2 pinch+comp", 10.000000)
    prg.add(5000160, "IGBT 2 pinch+comp", 9.800000)
    prg.add(5000260, "IGBT 2 pinch+comp", 9.600000)
    prg.add(5000360, "IGBT 2 pinch+comp", 9.400000)
    prg.add(5000460, "IGBT 2 pinch+comp", 9.200000)
    prg.add(5000500, "B comp y", 5.000000)
    prg.add(5000560, "IGBT 2 pinch+comp", 9.000000)
    prg.add(5000660, "IGBT 2 pinch+comp", 8.800000)
    prg.add(5000760, "IGBT 2 pinch+comp", 8.600000)
    prg.add(5000860, "IGBT 2 pinch+comp", 8.400000)
    prg.add(5000960, "IGBT 2 pinch+comp", 8.200000)
    prg.add(5001060, "IGBT 2 pinch+comp", 8.000000)
    prg.add(5001160, "IGBT 2 pinch+comp", 7.800000)
    prg.add(5001260, "IGBT 2 pinch+comp", 7.600000)
    prg.add(5001360, "IGBT 2 pinch+comp", 7.400000)
    prg.add(5001460, "IGBT 2 pinch+comp", 7.200000)
    prg.add(5001560, "IGBT 2 pinch+comp", 7.000000)
    prg.add(5001660, "IGBT 2 pinch+comp", 6.800000)
    prg.add(5001760, "IGBT 2 pinch+comp", 6.600000)
    prg.add(5001860, "IGBT 2 pinch+comp", 6.400000)
    prg.add(5001960, "IGBT 2 pinch+comp", 6.200000)
    prg.add(5002060, "IGBT 2 pinch+comp", 6.000000)
    prg.add(5002160, "IGBT 2 pinch+comp", 5.800000)
    prg.add(5002260, "IGBT 2 pinch+comp", 5.600000)
    prg.add(5002360, "IGBT 2 pinch+comp", 5.400000)
    prg.add(5002460, "IGBT 2 pinch+comp", 5.200000)
    prg.add(5002560, "IGBT 2 pinch+comp", 5.000000)
    prg.add(5002660, "IGBT 2 pinch+comp", 4.800000)
    prg.add(5002760, "IGBT 2 pinch+comp", 4.600000)
    prg.add(5002860, "IGBT 2 pinch+comp", 4.400000)
    prg.add(5002960, "IGBT 2 pinch+comp", 4.200000)
    prg.add(5003060, "IGBT 2 pinch+comp", 4.000000)
    prg.add(5003160, "IGBT 2 pinch+comp", 3.800000)
    prg.add(5003260, "IGBT 2 pinch+comp", 3.600000)
    prg.add(5003360, "IGBT 2 pinch+comp", 3.400000)
    prg.add(5003460, "IGBT 2 pinch+comp", 3.200000)
    prg.add(5003560, "IGBT 2 pinch+comp", 3.000000)
    prg.add(5003660, "IGBT 2 pinch+comp", 2.800000)
    prg.add(5003760, "IGBT 2 pinch+comp", 2.600000)
    prg.add(5003860, "IGBT 2 pinch+comp", 2.400000)
    prg.add(5003960, "IGBT 2 pinch+comp", 2.200000)
    prg.add(5004060, "IGBT 2 pinch+comp", 2.000000)
    prg.add(5004160, "IGBT 2 pinch+comp", 1.800000)
    prg.add(5004260, "IGBT 2 pinch+comp", 1.600000)
    prg.add(5004360, "IGBT 2 pinch+comp", 1.400000)
    prg.add(5004460, "IGBT 2 pinch+comp", 1.200000)
    prg.add(5004560, "IGBT 2 pinch+comp", 1.000000)
    prg.add(5004660, "IGBT 2 pinch+comp", 0.800000)
    prg.add(5004760, "IGBT 2 pinch+comp", 0.600000)
    prg.add(5004860, "IGBT 2 pinch+comp", 0.400000)
    prg.add(5004960, "IGBT 2 pinch+comp", 0.200000)
    prg.add(5005060, "IGBT 2 pinch+comp", 0.000000)
    prg.add(5005160, "IGBT 2 pinch+comp", -0.200000)
    prg.add(5005260, "IGBT 2 pinch+comp", -0.400000)
    prg.add(5005360, "IGBT 2 pinch+comp", -0.600000)
    prg.add(5005460, "IGBT 2 pinch+comp", -0.800000)
    prg.add(5005560, "IGBT 2 pinch+comp", -1.000000)
    prg.add(5005660, "IGBT 2 pinch+comp", -1.200000)
    prg.add(5005760, "IGBT 2 pinch+comp", -1.400000)
    prg.add(5005860, "IGBT 2 pinch+comp", -1.600000)
    prg.add(5005960, "IGBT 2 pinch+comp", -1.800000)
    prg.add(5006060, "IGBT 2 pinch+comp", -2.000000)
    prg.add(5006160, "IGBT 2 pinch+comp", -2.200000)
    prg.add(5006260, "IGBT 2 pinch+comp", -2.400000)
    prg.add(5006360, "IGBT 2 pinch+comp", -2.600000)
    prg.add(5006460, "IGBT 2 pinch+comp", -2.800000)
    prg.add(5006560, "IGBT 2 pinch+comp", -3.000000)
    prg.add(5006660, "IGBT 2 pinch+comp", -3.200000)
    prg.add(5006760, "IGBT 2 pinch+comp", -3.400000)
    prg.add(5006860, "IGBT 2 pinch+comp", -3.600000)
    prg.add(5006960, "IGBT 2 pinch+comp", -3.800000)
    prg.add(5007060, "IGBT 2 pinch+comp", -4.000000)
    prg.add(5007160, "IGBT 2 pinch+comp", -4.200000)
    prg.add(5007260, "IGBT 2 pinch+comp", -4.400000)
    prg.add(5007360, "IGBT 2 pinch+comp", -4.600000)
    prg.add(5007460, "IGBT 2 pinch+comp", -4.800000)
    prg.add(5007560, "IGBT 2 pinch+comp", -5.000000)
    prg.add(5007660, "IGBT 2 pinch+comp", -5.200000)
    prg.add(5007760, "IGBT 2 pinch+comp", -5.400000)
    prg.add(5007860, "IGBT 2 pinch+comp", -5.600000)
    prg.add(5007960, "IGBT 2 pinch+comp", -5.800000)
    prg.add(5008060, "IGBT 2 pinch+comp", -6.000000)
    prg.add(5008160, "IGBT 2 pinch+comp", -6.200000)
    prg.add(5008260, "IGBT 2 pinch+comp", -6.400000)
    prg.add(5008360, "IGBT 2 pinch+comp", -6.600000)
    prg.add(5008460, "IGBT 2 pinch+comp", -6.800000)
    prg.add(5008560, "IGBT 2 pinch+comp", -7.000000)
    prg.add(5008660, "IGBT 2 pinch+comp", -7.200000)
    prg.add(5008760, "IGBT 2 pinch+comp", -7.400000)
    prg.add(5008860, "IGBT 2 pinch+comp", -7.600000)
    prg.add(5008960, "IGBT 2 pinch+comp", -7.800000)
    prg.add(5009060, "IGBT 2 pinch+comp", -8.000000)
    prg.add(5009160, "IGBT 2 pinch+comp", -8.200000)
    prg.add(5009260, "IGBT 2 pinch+comp", -8.400000)
    prg.add(5009360, "IGBT 2 pinch+comp", -8.600000)
    prg.add(5009460, "IGBT 2 pinch+comp", -8.800000)
    prg.add(5009560, "IGBT 2 pinch+comp", -9.000000)
    prg.add(5009660, "IGBT 2 pinch+comp", -9.200000)
    prg.add(5009760, "IGBT 2 pinch+comp", -9.400000)
    prg.add(5009860, "IGBT 2 pinch+comp", -9.600000)
    prg.add(5009960, "IGBT 2 pinch+comp", -9.800000)
    prg.add(5010060, "IGBT 2 pinch+comp", -10.000000)
    prg.add(5010100, "IGBT 4 Open")
    prg.add(5010120, "IGBT 5 Open")
    prg.add(5010350, "IGBT 1 pinch", -10.000000)
    prg.add(5010360, "IGBT 2 pinch+comp", -10.000000)
    prg.add(5010370, "IGBT 3 Close")
    prg.add(5010380, "IGBT 4 Close")
    prg.add(5010390, "IGBT 5 Open")
    prg.add(5010400, "Delta 2 Voltage", 0.000000)
    prg.add(5010410, "Delta 1 Current", 15.400000)
    prg.add(5010450, "B comp x", 0.000000)
    prg.add(5010500, "B comp y", 5.000000)
    prg.add(5011030, "B comp y", 4.740000)
    prg.add(5011550, "B comp y", 4.470000)
    prg.add(5012080, "B comp y", 4.210000)
    prg.add(5012610, "B comp y", 3.950000)
    prg.add(5013130, "B comp y", 3.680000)
    prg.add(5013660, "B comp y", 3.420000)
    prg.add(5014180, "B comp y", 3.160000)
    prg.add(5014710, "B comp y", 2.890000)
    prg.add(5015240, "B comp y", 2.630000)
    prg.add(5015760, "B comp y", 2.370000)
    prg.add(5016290, "B comp y", 2.110000)
    prg.add(5016820, "B comp y", 1.840000)
    prg.add(5017340, "B comp y", 1.580000)
    prg.add(5017870, "B comp y", 1.320000)
    prg.add(5018390, "B comp y", 1.050000)
    prg.add(5018920, "B comp y", 0.790000)
    prg.add(5019450, "B comp y", 0.530000)
    prg.add(5019970, "B comp y", 0.260000)
    prg.add(5020500, "B comp y", 0.000000)
    prg.add(6482000, "B comp y", 1.000000)
    prg.add(6495000, "IGBT 1 pinch", -10.000000)
    prg.add(6495010, "IGBT 2 pinch+comp", -10.000000)
    prg.add(6495019, "IGBT 3 Open")
    prg.add(6495030, "IGBT 4 Open")
    prg.add(6495040, "IGBT 5 Open")
    prg.add(6495050, "IGBT 6 Open")
    prg.add(6495599, "K probe Cooler (-) freq", 99.500000)
    prg.add(6496000, "K Cooler 2p (+) freq", 97.500000)
    prg.add(6496400, "K Repumper 1p (+) Amp", 1000.000000)
    prg.add(6496799, "K Repumper 1p (+) freq", 115.000000)
    prg.add(6497200, "K Repumper 2p (+) freq", 96.000000)
    prg.add(6498500, "Na Repumper MOT Amp", 1000.000000)
    prg.add(6499000, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(6499400, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(6499800, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6500200, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6500500, "Trig Slow Stingray ON")
    prg.add(6500599, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(6501000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(6501400, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(6502050, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(6502400, "K probe Cooler (-) Amp", 1.000000)
    prg.add(6503000, "Trig Slow Stingray OFF")
    prg.add(6751000, "Shutter Probe Na Close")
    prg.add(6761000, "Shutter Probe K Close")
    prg.add(7000000, "Optical Levit ON")
    prg.add(7500500, "Trig Slow Stingray ON")
    prg.add(7501000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(7501400, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(7502000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(7502400, "K probe Cooler (-) Amp", 1.000000)
    prg.add(7503000, "Trig Slow Stingray OFF")
    prg.add(7511000, "Na Repumper MOT Amp", 1.000000)
    prg.add(7521000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(7531000, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(8500500, "Trig Slow Stingray ON")
    prg.add(8502500, "Trig Slow Stingray OFF")
    prg.add(9500500, "Trig Slow Stingray ON")
    prg.add(9502500, "Trig Slow Stingray OFF")
    prg.add(10011000, "Optical Levit OFF")
    prg.add(10501000, "B comp y", 0.000000)
    return prg
