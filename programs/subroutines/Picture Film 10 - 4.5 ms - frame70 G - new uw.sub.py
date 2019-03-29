prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4002500, "Shutter Probe Na Open")
    prg.add(-3512500, "Na Probe/Push (-) freq", 150.000000)
    prg.add(-3502500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(-724500, "Optical Levit ON")
    prg.add(0, "Trig ON Stingray 1")
    prg.add(20, "Na Probe/Push (-) freq", 110.000000)
    prg.add(500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(299900, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(345000, "Trig ON Stingray 1")
    prg.add(345020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(345500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(346500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(346900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(347000, "Trig OFF Stingray 1")
    prg.add(999970, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1045000, "Trig ON Stingray 1")
    prg.add(1045020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1045500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1046500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1046900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1047000, "Trig OFF Stingray 1")
    prg.add(1699970, "Pulse uw ON")
    prg.add(1700000, "Pulse uw OFF")
    prg.add(1745000, "Trig ON Stingray 1")
    prg.add(1745020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1745500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1746500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1746900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1747000, "Trig OFF Stingray 1")
    prg.add(2399970, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2445000, "Trig ON Stingray 1")
    prg.add(2445020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2445500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2446500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2446900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2447000, "Trig OFF Stingray 1")
    prg.add(3099970, "Pulse uw ON")
    prg.add(3100000, "Pulse uw OFF")
    prg.add(3145000, "Trig ON Stingray 1")
    prg.add(3145020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3145500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3146500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3146900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3147000, "Trig OFF Stingray 1")
    prg.add(3799970, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3845000, "Trig ON Stingray 1")
    prg.add(3845020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3845500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3846500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3846900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3847000, "Trig OFF Stingray 1")
    prg.add(4499970, "Pulse uw ON")
    prg.add(4500000, "Pulse uw OFF")
    prg.add(4545000, "Trig ON Stingray 1")
    prg.add(4545020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4545500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4546500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4546900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4547000, "Trig OFF Stingray 1")
    prg.add(4689500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(4699500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(4709500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(4729500, "Na Dark Spot Amp", 1.000000)
    prg.add(4739500, "Na Repumper MOT Amp", 1.000000)
    prg.add(5089500, "Shutter Probe Na Open")
    prg.add(5199970, "Pulse uw ON")
    prg.add(5200000, "Pulse uw OFF")
    prg.add(5245000, "Trig ON Stingray 1")
    prg.add(5245019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5245500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5246500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5246900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5247000, "Trig OFF Stingray 1")
    prg.add(5899970, "Pulse uw ON")
    prg.add(5900000, "Pulse uw OFF")
    prg.add(5945000, "Trig ON Stingray 1")
    prg.add(5945019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5945500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5946500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5946900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5947000, "Trig OFF Stingray 1")
    prg.add(6059500, "Shutter Probe K Open")
    prg.add(6069500, "Shutter RepumperMOT K Open")
    prg.add(6079500, "Shutter repump Na Open")
    prg.add(6599500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(6599970, "Pulse uw ON")
    prg.add(6600000, "Pulse uw OFF")
    prg.add(6645000, "Trig ON Stingray 1")
    prg.add(6645019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6645500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6646500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6646900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6647000, "Trig OFF Stingray 1")
    prg.add(7062500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(7072500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(7091500, "Optical Levit OFF")
    prg.add(7092500, "Shutter 3DMOT cool Na Open")
    prg.add(7103500, "Shutter Optical Levit Close")
    prg.add(7582000, "B comp y", 0.000000)
    prg.add(7582530, "B comp y", 0.260000)
    prg.add(7583049, "B comp y", 0.530000)
    prg.add(7583579, "B comp y", 0.790000)
    prg.add(7584109, "B comp y", 1.050000)
    prg.add(7584630, "B comp y", 1.320000)
    prg.add(7585160, "B comp y", 1.580000)
    prg.add(7585680, "B comp y", 1.840000)
    prg.add(7586210, "B comp y", 2.110000)
    prg.add(7586740, "B comp y", 2.370000)
    prg.add(7587260, "B comp y", 2.630000)
    prg.add(7587790, "B comp y", 2.890000)
    prg.add(7588320, "B comp y", 3.160000)
    prg.add(7588840, "B comp y", 3.420000)
    prg.add(7589370, "B comp y", 3.680000)
    prg.add(7589890, "B comp y", 3.950000)
    prg.add(7590420, "B comp y", 4.210000)
    prg.add(7590950, "B comp y", 4.470000)
    prg.add(7591470, "B comp y", 4.740000)
    prg.add(7591500, "IGBT 1 pinch", -10.000000)
    prg.add(7591520, "IGBT 3 Open")
    prg.add(7591559, "IGBT 2 pinch+comp", 10.000000)
    prg.add(7591660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(7591760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(7591860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(7591960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(7592000, "B comp y", 5.000000)
    prg.add(7592060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(7592160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(7592260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(7592360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(7592460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(7592560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(7592660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(7592760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(7592859, "IGBT 2 pinch+comp", 7.400000)
    prg.add(7592960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(7593060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(7593160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(7593260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(7593360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(7593460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(7593560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(7593660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(7593760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(7593860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(7593960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(7594059, "IGBT 2 pinch+comp", 5.000000)
    prg.add(7594160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(7594260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(7594360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(7594460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(7594560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(7594660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(7594760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(7594860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(7594960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(7595060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(7595160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(7595260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(7595359, "IGBT 2 pinch+comp", 2.400000)
    prg.add(7595460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(7595560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(7595660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(7595760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(7595860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(7595960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(7596060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(7596160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(7596260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(7596360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(7596460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(7596559, "IGBT 2 pinch+comp", 0.000000)
    prg.add(7596660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(7596760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(7596860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(7596960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(7597060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(7597160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(7597260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(7597360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(7597460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(7597560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(7597660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(7597760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(7597859, "IGBT 2 pinch+comp", -2.600000)
    prg.add(7597960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(7598060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(7598160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(7598260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(7598360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(7598460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(7598560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(7598660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(7598760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(7598860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(7598960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(7599059, "IGBT 2 pinch+comp", -5.000000)
    prg.add(7599160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(7599260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(7599360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(7599460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(7599560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(7599660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(7599760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(7599860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(7599960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(7600060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(7600160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(7600260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(7600359, "IGBT 2 pinch+comp", -7.600000)
    prg.add(7600460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(7600560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(7600660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(7600760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(7600860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(7600960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(7601060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(7601160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(7601260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(7601360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(7601460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(7601559, "IGBT 2 pinch+comp", -10.000000)
    prg.add(7601600, "IGBT 4 Open")
    prg.add(7601620, "IGBT 5 Open")
    prg.add(7601849, "IGBT 1 pinch", -10.000000)
    prg.add(7601860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(7601870, "IGBT 3 Close")
    prg.add(7601880, "IGBT 4 Close")
    prg.add(7601890, "IGBT 5 Open")
    prg.add(7601900, "Delta 2 Voltage", 0.000000)
    prg.add(7601910, "Delta 1 Current", 15.400000)
    prg.add(7601950, "B comp x", 0.000000)
    prg.add(7602000, "B comp y", 5.000000)
    prg.add(7602530, "B comp y", 4.740000)
    prg.add(7603049, "B comp y", 4.470000)
    prg.add(7603579, "B comp y", 4.210000)
    prg.add(7604109, "B comp y", 3.950000)
    prg.add(7604630, "B comp y", 3.680000)
    prg.add(7605160, "B comp y", 3.420000)
    prg.add(7605680, "B comp y", 3.160000)
    prg.add(7606210, "B comp y", 2.890000)
    prg.add(7606740, "B comp y", 2.630000)
    prg.add(7607260, "B comp y", 2.370000)
    prg.add(7607790, "B comp y", 2.110000)
    prg.add(7608320, "B comp y", 1.840000)
    prg.add(7608840, "B comp y", 1.580000)
    prg.add(7609370, "B comp y", 1.320000)
    prg.add(7609890, "B comp y", 1.050000)
    prg.add(7610420, "B comp y", 0.790000)
    prg.add(7610950, "B comp y", 0.530000)
    prg.add(7611470, "B comp y", 0.260000)
    prg.add(7612000, "B comp y", 0.000000)
    prg.add(9073500, "B comp y", 1.000000)
    prg.add(9086500, "IGBT 1 pinch", -10.000000)
    prg.add(9086510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(9086520, "IGBT 3 Open")
    prg.add(9086530, "IGBT 4 Open")
    prg.add(9086540, "IGBT 5 Open")
    prg.add(9086550, "IGBT 6 Open")
    prg.add(9086570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9086900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(9090000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(9090500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(9090900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(9091300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9091700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9092000, "Trig Slow Stingray ON")
    prg.add(9092100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(9092500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(9092900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(9093550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9093900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(9094500, "Trig Slow Stingray OFF")
    prg.add(9342500, "Shutter Probe Na Close")
    prg.add(9352500, "Shutter Probe K Close")
    prg.add(9591500, "Optical Levit ON")
    prg.add(10092000, "Trig Slow Stingray ON")
    prg.add(10092500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(10092900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(10093500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(10093900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10094500, "Trig Slow Stingray OFF")
    prg.add(10102500, "Na Repumper MOT Amp", 1.000000)
    prg.add(10112500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(10122500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(11092000, "Trig Slow Stingray ON")
    prg.add(11094000, "Trig Slow Stingray OFF")
    prg.add(12092000, "Trig Slow Stingray ON")
    prg.add(12094000, "Trig Slow Stingray OFF")
    prg.add(12602500, "Optical Levit OFF")
    prg.add(12841500, "Shutter Optical Levit Close")
    prg.add(13092500, "B comp y", 0.000000)
    prg.add(17591500, "Optical Levit ON")
    return prg
