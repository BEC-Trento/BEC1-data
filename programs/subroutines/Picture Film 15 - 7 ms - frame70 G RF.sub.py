prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4002500, "Shutter Probe Na Open")
    prg.add(-3512500, "Na Probe/Push (-) freq", 150.000000)
    prg.add(-3502500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(-724500, "Optical Levit ON")
    prg.add(-69000, "Optical Levit OFF")
    prg.add(0, "Trig ON Stingray 1")
    prg.add(20, "Na Probe/Push (-) freq", 110.000000)
    prg.add(500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(7590, "Optical Levit ON")
    prg.add(299960, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(301000, "Optical Levit OFF")
    prg.add(370000, "Trig ON Stingray 1")
    prg.add(370020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(370500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(371500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(371900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(372000, "Trig OFF Stingray 1")
    prg.add(377590, "Optical Levit ON")
    prg.add(999960, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1001000, "Optical Levit OFF")
    prg.add(1070000, "Trig ON Stingray 1")
    prg.add(1070020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1070500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1071500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1071900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1072000, "Trig OFF Stingray 1")
    prg.add(1077590, "Optical Levit ON")
    prg.add(1699960, "Pulse uw ON")
    prg.add(1700000, "Pulse uw OFF")
    prg.add(1701000, "Optical Levit OFF")
    prg.add(1770000, "Trig ON Stingray 1")
    prg.add(1770020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1770500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1771500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1771900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1772000, "Trig OFF Stingray 1")
    prg.add(1777589, "Optical Levit ON")
    prg.add(2399960, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2401000, "Optical Levit OFF")
    prg.add(2470000, "Trig ON Stingray 1")
    prg.add(2470020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2470500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2471500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2471900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2472000, "Trig OFF Stingray 1")
    prg.add(2477590, "Optical Levit ON")
    prg.add(3099960, "Pulse uw ON")
    prg.add(3100000, "Pulse uw OFF")
    prg.add(3101000, "Optical Levit OFF")
    prg.add(3170000, "Trig ON Stingray 1")
    prg.add(3170020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3170500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3171500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3171900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3172000, "Trig OFF Stingray 1")
    prg.add(3177590, "Optical Levit ON")
    prg.add(3799960, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3801000, "Optical Levit OFF")
    prg.add(3870000, "Trig ON Stingray 1")
    prg.add(3870020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3870500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3871500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3871900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3872000, "Trig OFF Stingray 1")
    prg.add(3877590, "Optical Levit ON")
    prg.add(4499960, "Pulse uw ON")
    prg.add(4500000, "Pulse uw OFF")
    prg.add(4501000, "Optical Levit OFF")
    prg.add(4570000, "Trig ON Stingray 1")
    prg.add(4570020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4570500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4571500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4571900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4572000, "Trig OFF Stingray 1")
    prg.add(4577590, "Optical Levit ON")
    prg.add(5199960, "Pulse uw ON")
    prg.add(5200000, "Pulse uw OFF")
    prg.add(5201000, "Optical Levit OFF")
    prg.add(5270000, "Trig ON Stingray 1")
    prg.add(5270019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5270500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5271500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5271900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5272000, "Trig OFF Stingray 1")
    prg.add(5277590, "Optical Levit ON")
    prg.add(5899960, "Pulse uw ON")
    prg.add(5900000, "Pulse uw OFF")
    prg.add(5901000, "Optical Levit OFF")
    prg.add(5970000, "Trig ON Stingray 1")
    prg.add(5970019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5970500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5971500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5971900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5972000, "Trig OFF Stingray 1")
    prg.add(5977590, "Optical Levit ON")
    prg.add(6599960, "Pulse uw ON")
    prg.add(6600000, "Pulse uw OFF")
    prg.add(6601000, "Optical Levit OFF")
    prg.add(6670000, "Trig ON Stingray 1")
    prg.add(6670019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6670500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6671500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6671900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6672000, "Trig OFF Stingray 1")
    prg.add(6677590, "Optical Levit ON")
    prg.add(7299960, "Pulse uw ON")
    prg.add(7300000, "Pulse uw OFF")
    prg.add(7301000, "Optical Levit OFF")
    prg.add(7370000, "Trig ON Stingray 1")
    prg.add(7370019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7370500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7371500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(7371900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(7372000, "Trig OFF Stingray 1")
    prg.add(7377590, "Optical Levit ON")
    prg.add(7999960, "Pulse uw ON")
    prg.add(8000000, "Pulse uw OFF")
    prg.add(8001000, "Optical Levit OFF")
    prg.add(8070000, "Trig ON Stingray 1")
    prg.add(8070019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8070500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8071500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8071900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8072000, "Trig OFF Stingray 1")
    prg.add(8077590, "Optical Levit ON")
    prg.add(8214500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(8224500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(8234500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(8254500, "Na Dark Spot Amp", 1.000000)
    prg.add(8264500, "Na Repumper MOT Amp", 1.000000)
    prg.add(8614500, "Shutter Probe Na Open")
    prg.add(8699960, "Pulse uw ON")
    prg.add(8700000, "Pulse uw OFF")
    prg.add(8701000, "Optical Levit OFF")
    prg.add(8770000, "Trig ON Stingray 1")
    prg.add(8770020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8770500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8771500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8771900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8772000, "Trig OFF Stingray 1")
    prg.add(8777590, "Optical Levit ON")
    prg.add(9399960, "Pulse uw ON")
    prg.add(9400000, "Pulse uw OFF")
    prg.add(9401000, "Optical Levit OFF")
    prg.add(9470000, "Trig ON Stingray 1")
    prg.add(9470020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9470500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9471500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(9471900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(9472000, "Trig OFF Stingray 1")
    prg.add(9477590, "Optical Levit ON")
    prg.add(9584500, "Shutter Probe K Open")
    prg.add(9594500, "Shutter RepumperMOT K Open")
    prg.add(9604500, "Shutter repump Na Open")
    prg.add(10099960, "Pulse uw ON")
    prg.add(10100000, "Pulse uw OFF")
    prg.add(10101000, "Optical Levit OFF")
    prg.add(10124500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10170000, "Trig ON Stingray 1")
    prg.add(10170020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(10170500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(10171500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(10171900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(10172000, "Trig OFF Stingray 1")
    prg.add(10177590, "Optical Levit ON")
    prg.add(10587500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(10597500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(10616500, "Optical Levit OFF")
    prg.add(10617500, "Shutter 3DMOT cool Na Open")
    prg.add(10628500, "Shutter Optical Levit Close")
    prg.add(11107000, "B comp y", 0.000000)
    prg.add(11107530, "B comp y", 0.260000)
    prg.add(11108050, "B comp y", 0.530000)
    prg.add(11108580, "B comp y", 0.790000)
    prg.add(11109110, "B comp y", 1.050000)
    prg.add(11109630, "B comp y", 1.320000)
    prg.add(11110160, "B comp y", 1.580000)
    prg.add(11110680, "B comp y", 1.840000)
    prg.add(11111210, "B comp y", 2.110000)
    prg.add(11111740, "B comp y", 2.370000)
    prg.add(11112260, "B comp y", 2.630000)
    prg.add(11112790, "B comp y", 2.890000)
    prg.add(11113320, "B comp y", 3.160000)
    prg.add(11113840, "B comp y", 3.420000)
    prg.add(11114369, "B comp y", 3.680000)
    prg.add(11114890, "B comp y", 3.950000)
    prg.add(11115420, "B comp y", 4.210000)
    prg.add(11115950, "B comp y", 4.470000)
    prg.add(11116470, "B comp y", 4.740000)
    prg.add(11116500, "IGBT 1 pinch", -10.000000)
    prg.add(11116520, "IGBT 3 Open")
    prg.add(11116560, "IGBT 2 pinch+comp", 10.000000)
    prg.add(11116660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(11116760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(11116860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(11116960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(11117000, "B comp y", 5.000000)
    prg.add(11117059, "IGBT 2 pinch+comp", 9.000000)
    prg.add(11117159, "IGBT 2 pinch+comp", 8.800000)
    prg.add(11117260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(11117360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(11117460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(11117560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(11117660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(11117760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(11117860, "IGBT 2 pinch+comp", 7.400000)
    prg.add(11117960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(11118060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(11118160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(11118260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(11118360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(11118460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(11118560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(11118660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(11118760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(11118860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(11118960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(11119060, "IGBT 2 pinch+comp", 5.000000)
    prg.add(11119160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(11119260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(11119360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(11119460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(11119559, "IGBT 2 pinch+comp", 4.000000)
    prg.add(11119659, "IGBT 2 pinch+comp", 3.800000)
    prg.add(11119760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(11119860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(11119960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(11120060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(11120160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(11120260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(11120360, "IGBT 2 pinch+comp", 2.400000)
    prg.add(11120460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(11120560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(11120660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(11120760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(11120860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(11120960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(11121060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(11121160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(11121260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(11121360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(11121460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(11121560, "IGBT 2 pinch+comp", 0.000000)
    prg.add(11121660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(11121760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(11121860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(11121960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(11122059, "IGBT 2 pinch+comp", -1.000000)
    prg.add(11122159, "IGBT 2 pinch+comp", -1.200000)
    prg.add(11122260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(11122360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(11122460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(11122560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(11122660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(11122760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(11122860, "IGBT 2 pinch+comp", -2.600000)
    prg.add(11122960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(11123060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(11123160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(11123260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(11123360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(11123460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(11123560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(11123660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(11123760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(11123860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(11123960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(11124060, "IGBT 2 pinch+comp", -5.000000)
    prg.add(11124160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(11124260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(11124360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(11124460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(11124559, "IGBT 2 pinch+comp", -6.000000)
    prg.add(11124659, "IGBT 2 pinch+comp", -6.200000)
    prg.add(11124760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(11124860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(11124960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(11125060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(11125160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(11125260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(11125360, "IGBT 2 pinch+comp", -7.600000)
    prg.add(11125460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(11125560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(11125660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(11125760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(11125860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(11125960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(11126060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(11126160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(11126260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(11126360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(11126460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(11126560, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11126600, "IGBT 4 Open")
    prg.add(11126620, "IGBT 5 Open")
    prg.add(11126850, "IGBT 1 pinch", -10.000000)
    prg.add(11126860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11126869, "IGBT 3 Close")
    prg.add(11126880, "IGBT 4 Close")
    prg.add(11126890, "IGBT 5 Open")
    prg.add(11126900, "Delta 2 Voltage", 0.000000)
    prg.add(11126910, "Delta 1 Current", 15.400000)
    prg.add(11126950, "B comp x", 0.000000)
    prg.add(11127000, "B comp y", 5.000000)
    prg.add(11127530, "B comp y", 4.740000)
    prg.add(11128050, "B comp y", 4.470000)
    prg.add(11128580, "B comp y", 4.210000)
    prg.add(11129110, "B comp y", 3.950000)
    prg.add(11129630, "B comp y", 3.680000)
    prg.add(11130160, "B comp y", 3.420000)
    prg.add(11130680, "B comp y", 3.160000)
    prg.add(11131210, "B comp y", 2.890000)
    prg.add(11131740, "B comp y", 2.630000)
    prg.add(11132260, "B comp y", 2.370000)
    prg.add(11132790, "B comp y", 2.110000)
    prg.add(11133320, "B comp y", 1.840000)
    prg.add(11133840, "B comp y", 1.580000)
    prg.add(11134369, "B comp y", 1.320000)
    prg.add(11134890, "B comp y", 1.050000)
    prg.add(11135420, "B comp y", 0.790000)
    prg.add(11135950, "B comp y", 0.530000)
    prg.add(11136470, "B comp y", 0.260000)
    prg.add(11137000, "B comp y", 0.000000)
    prg.add(12598500, "B comp y", 1.000000)
    prg.add(12611500, "IGBT 1 pinch", -10.000000)
    prg.add(12611510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(12611520, "IGBT 3 Open")
    prg.add(12611530, "IGBT 4 Open")
    prg.add(12611540, "IGBT 5 Open")
    prg.add(12611550, "IGBT 6 Open")
    prg.add(12611570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12611900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(12615000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(12615500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(12615900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(12616300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(12616700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(12617000, "Trig Slow Stingray ON")
    prg.add(12617100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(12617500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(12617900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(12618550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12618900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(12619500, "Trig Slow Stingray OFF")
    prg.add(12867500, "Shutter Probe Na Close")
    prg.add(12877500, "Shutter Probe K Close")
    prg.add(13116500, "Optical Levit ON")
    prg.add(13617000, "Trig Slow Stingray ON")
    prg.add(13617500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(13617900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(13618500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(13618900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(13619500, "Trig Slow Stingray OFF")
    prg.add(13627500, "Na Repumper MOT Amp", 1.000000)
    prg.add(13637500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(13647500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(14617000, "Trig Slow Stingray ON")
    prg.add(14619000, "Trig Slow Stingray OFF")
    prg.add(15617000, "Trig Slow Stingray ON")
    prg.add(15619000, "Trig Slow Stingray OFF")
    prg.add(16127500, "Optical Levit OFF")
    prg.add(16366500, "Shutter Optical Levit Close")
    prg.add(16617500, "B comp y", 0.000000)
    prg.add(21116500, "Optical Levit ON")
    return prg