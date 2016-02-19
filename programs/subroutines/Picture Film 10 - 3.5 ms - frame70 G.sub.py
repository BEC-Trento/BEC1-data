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
    prg.add(299960, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(335000, "Trig ON Stingray 1")
    prg.add(335020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(335500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(336500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(336900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(337000, "Trig OFF Stingray 1")
    prg.add(999960, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1035000, "Trig ON Stingray 1")
    prg.add(1035020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1035500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1036500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1036900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1037000, "Trig OFF Stingray 1")
    prg.add(1699964, "Pulse uw ON")
    prg.add(1700000, "Pulse uw OFF")
    prg.add(1735000, "Trig ON Stingray 1")
    prg.add(1735020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1735500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1736500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1736900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1737000, "Trig OFF Stingray 1")
    prg.add(2399961, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2435000, "Trig ON Stingray 1")
    prg.add(2435020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2435500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2436500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2436900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2437000, "Trig OFF Stingray 1")
    prg.add(3099957, "Pulse uw ON")
    prg.add(3100000, "Pulse uw OFF")
    prg.add(3135000, "Trig ON Stingray 1")
    prg.add(3135020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3135500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3136500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3136900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3137000, "Trig OFF Stingray 1")
    prg.add(3799955, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3835000, "Trig ON Stingray 1")
    prg.add(3835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3837000, "Trig OFF Stingray 1")
    prg.add(4499952, "Pulse uw ON")
    prg.add(4500000, "Pulse uw OFF")
    prg.add(4535000, "Trig ON Stingray 1")
    prg.add(4535020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4535500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4536500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4536900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4537000, "Trig OFF Stingray 1")
    prg.add(4679500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(4689500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(4699500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(4719500, "Na Dark Spot Amp", 1.000000)
    prg.add(4729500, "Na Repumper MOT Amp", 1.000000)
    prg.add(5079500, "Shutter Probe Na Open")
    prg.add(5199949, "Pulse uw ON")
    prg.add(5200000, "Pulse uw OFF")
    prg.add(5235000, "Trig ON Stingray 1")
    prg.add(5235019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5235500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5236500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5236900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5237000, "Trig OFF Stingray 1")
    prg.add(5899946, "Pulse uw ON")
    prg.add(5900000, "Pulse uw OFF")
    prg.add(5935000, "Trig ON Stingray 1")
    prg.add(5935019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5935500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5936500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5936900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5937000, "Trig OFF Stingray 1")
    prg.add(6049500, "Shutter Probe K Open")
    prg.add(6059500, "Shutter RepumperMOT K Open")
    prg.add(6069500, "Shutter repump Na Open")
    prg.add(6589500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(6599942, "Pulse uw ON")
    prg.add(6600000, "Pulse uw OFF")
    prg.add(6635000, "Trig ON Stingray 1")
    prg.add(6635019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6635500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6636500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6636900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6637000, "Trig OFF Stingray 1")
    prg.add(7052500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(7062500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(7081500, "Optical Levit OFF")
    prg.add(7082500, "Shutter 3DMOT cool Na Open")
    prg.add(7093500, "Shutter Optical Levit Close")
    prg.add(7572000, "B comp y", 0.000000)
    prg.add(7572530, "B comp y", 0.260000)
    prg.add(7573049, "B comp y", 0.530000)
    prg.add(7573579, "B comp y", 0.790000)
    prg.add(7574109, "B comp y", 1.050000)
    prg.add(7574630, "B comp y", 1.320000)
    prg.add(7575160, "B comp y", 1.580000)
    prg.add(7575680, "B comp y", 1.840000)
    prg.add(7576210, "B comp y", 2.110000)
    prg.add(7576740, "B comp y", 2.370000)
    prg.add(7577260, "B comp y", 2.630000)
    prg.add(7577790, "B comp y", 2.890000)
    prg.add(7578320, "B comp y", 3.160000)
    prg.add(7578840, "B comp y", 3.420000)
    prg.add(7579370, "B comp y", 3.680000)
    prg.add(7579890, "B comp y", 3.950000)
    prg.add(7580420, "B comp y", 4.210000)
    prg.add(7580950, "B comp y", 4.470000)
    prg.add(7581470, "B comp y", 4.740000)
    prg.add(7581500, "IGBT 1 pinch", -10.000000)
    prg.add(7581520, "IGBT 3 Open")
    prg.add(7581559, "IGBT 2 pinch+comp", 10.000000)
    prg.add(7581660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(7581760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(7581860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(7581960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(7582000, "B comp y", 5.000000)
    prg.add(7582060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(7582160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(7582260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(7582360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(7582460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(7582560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(7582660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(7582760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(7582859, "IGBT 2 pinch+comp", 7.400000)
    prg.add(7582960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(7583060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(7583160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(7583260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(7583360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(7583460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(7583560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(7583660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(7583760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(7583860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(7583960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(7584059, "IGBT 2 pinch+comp", 5.000000)
    prg.add(7584160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(7584260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(7584360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(7584460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(7584560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(7584660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(7584760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(7584860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(7584960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(7585060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(7585160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(7585260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(7585359, "IGBT 2 pinch+comp", 2.400000)
    prg.add(7585460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(7585560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(7585660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(7585760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(7585860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(7585960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(7586060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(7586160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(7586260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(7586360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(7586460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(7586559, "IGBT 2 pinch+comp", 0.000000)
    prg.add(7586660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(7586760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(7586860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(7586960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(7587060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(7587160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(7587260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(7587360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(7587460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(7587560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(7587660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(7587760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(7587859, "IGBT 2 pinch+comp", -2.600000)
    prg.add(7587960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(7588060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(7588160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(7588260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(7588360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(7588460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(7588560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(7588660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(7588760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(7588860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(7588960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(7589059, "IGBT 2 pinch+comp", -5.000000)
    prg.add(7589160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(7589260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(7589360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(7589460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(7589560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(7589660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(7589760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(7589860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(7589960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(7590060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(7590160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(7590260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(7590359, "IGBT 2 pinch+comp", -7.600000)
    prg.add(7590460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(7590560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(7590660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(7590760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(7590860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(7590960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(7591060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(7591160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(7591260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(7591360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(7591460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(7591559, "IGBT 2 pinch+comp", -10.000000)
    prg.add(7591600, "IGBT 4 Open")
    prg.add(7591620, "IGBT 5 Open")
    prg.add(7591849, "IGBT 1 pinch", -10.000000)
    prg.add(7591860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(7591870, "IGBT 3 Close")
    prg.add(7591880, "IGBT 4 Close")
    prg.add(7591890, "IGBT 5 Open")
    prg.add(7591900, "Delta 2 Voltage", 0.000000)
    prg.add(7591910, "Delta 1 Current", 15.400000)
    prg.add(7591950, "B comp x", 0.000000)
    prg.add(7592000, "B comp y", 5.000000)
    prg.add(7592530, "B comp y", 4.740000)
    prg.add(7593049, "B comp y", 4.470000)
    prg.add(7593579, "B comp y", 4.210000)
    prg.add(7594109, "B comp y", 3.950000)
    prg.add(7594630, "B comp y", 3.680000)
    prg.add(7595160, "B comp y", 3.420000)
    prg.add(7595680, "B comp y", 3.160000)
    prg.add(7596210, "B comp y", 2.890000)
    prg.add(7596740, "B comp y", 2.630000)
    prg.add(7597260, "B comp y", 2.370000)
    prg.add(7597790, "B comp y", 2.110000)
    prg.add(7598320, "B comp y", 1.840000)
    prg.add(7598840, "B comp y", 1.580000)
    prg.add(7599370, "B comp y", 1.320000)
    prg.add(7599890, "B comp y", 1.050000)
    prg.add(7600420, "B comp y", 0.790000)
    prg.add(7600950, "B comp y", 0.530000)
    prg.add(7601470, "B comp y", 0.260000)
    prg.add(7602000, "B comp y", 0.000000)
    prg.add(9063500, "B comp y", 1.000000)
    prg.add(9076500, "IGBT 1 pinch", -10.000000)
    prg.add(9076510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(9076520, "IGBT 3 Open")
    prg.add(9076530, "IGBT 4 Open")
    prg.add(9076540, "IGBT 5 Open")
    prg.add(9076550, "IGBT 6 Open")
    prg.add(9076570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9076900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(9080000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(9080500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(9080900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(9081300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9081700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9082000, "Trig Slow Stingray ON")
    prg.add(9082100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(9082500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(9082900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(9083550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9083900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(9084500, "Trig Slow Stingray OFF")
    prg.add(9332500, "Shutter Probe Na Close")
    prg.add(9342500, "Shutter Probe K Close")
    prg.add(9581500, "Optical Levit ON")
    prg.add(10082000, "Trig Slow Stingray ON")
    prg.add(10082500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(10082900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(10083500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(10083900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10084500, "Trig Slow Stingray OFF")
    prg.add(10092500, "Na Repumper MOT Amp", 1.000000)
    prg.add(10102500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(10112500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(11082000, "Trig Slow Stingray ON")
    prg.add(11084000, "Trig Slow Stingray OFF")
    prg.add(12082000, "Trig Slow Stingray ON")
    prg.add(12084000, "Trig Slow Stingray OFF")
    prg.add(12592500, "Optical Levit OFF")
    prg.add(12831500, "Shutter Optical Levit Close")
    prg.add(13082500, "B comp y", 0.000000)
    prg.add(17581500, "Optical Levit ON")
    return prg
