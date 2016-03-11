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
    prg.add(299950, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(430000, "Trig ON Stingray 1")
    prg.add(430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(432000, "Trig OFF Stingray 1")
    prg.add(799990, "Pulse uw ON")
    prg.add(800000, "Pulse uw OFF")
    prg.add(930000, "Trig ON Stingray 1")
    prg.add(930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(932000, "Trig OFF Stingray 1")
    prg.add(1299990, "Pulse uw ON")
    prg.add(1300000, "Pulse uw OFF")
    prg.add(1430000, "Trig ON Stingray 1")
    prg.add(1430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1432000, "Trig OFF Stingray 1")
    prg.add(1799990, "Pulse uw ON")
    prg.add(1800000, "Pulse uw OFF")
    prg.add(1930000, "Trig ON Stingray 1")
    prg.add(1930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1932000, "Trig OFF Stingray 1")
    prg.add(2299990, "Pulse uw ON")
    prg.add(2300000, "Pulse uw OFF")
    prg.add(2430000, "Trig ON Stingray 1")
    prg.add(2430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2432000, "Trig OFF Stingray 1")
    prg.add(2799990, "Pulse uw ON")
    prg.add(2800000, "Pulse uw OFF")
    prg.add(2930000, "Trig ON Stingray 1")
    prg.add(2930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2932000, "Trig OFF Stingray 1")
    prg.add(3299990, "Pulse uw ON")
    prg.add(3300000, "Pulse uw OFF")
    prg.add(3430000, "Trig ON Stingray 1")
    prg.add(3430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3432000, "Trig OFF Stingray 1")
    prg.add(3799990, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3930000, "Trig ON Stingray 1")
    prg.add(3930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3932000, "Trig OFF Stingray 1")
    prg.add(4299990, "Pulse uw ON")
    prg.add(4300000, "Pulse uw OFF")
    prg.add(4430000, "Trig ON Stingray 1")
    prg.add(4430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4432000, "Trig OFF Stingray 1")
    prg.add(4799990, "Pulse uw ON")
    prg.add(4800000, "Pulse uw OFF")
    prg.add(4930000, "Trig ON Stingray 1")
    prg.add(4930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4932000, "Trig OFF Stingray 1")
    prg.add(5299990, "Pulse uw ON")
    prg.add(5300000, "Pulse uw OFF")
    prg.add(5430000, "Trig ON Stingray 1")
    prg.add(5430019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5432000, "Trig OFF Stingray 1")
    prg.add(5474500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(5484500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(5494500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(5514500, "Na Dark Spot Amp", 1.000000)
    prg.add(5524500, "Na Repumper MOT Amp", 1.000000)
    prg.add(5799990, "Pulse uw ON")
    prg.add(5800000, "Pulse uw OFF")
    prg.add(5874500, "Shutter Probe Na Open")
    prg.add(5930000, "Trig ON Stingray 1")
    prg.add(5930019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5932000, "Trig OFF Stingray 1")
    prg.add(6299990, "Pulse uw ON")
    prg.add(6300000, "Pulse uw OFF")
    prg.add(6430000, "Trig ON Stingray 1")
    prg.add(6430019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6432000, "Trig OFF Stingray 1")
    prg.add(6799990, "Pulse uw ON")
    prg.add(6800000, "Pulse uw OFF")
    prg.add(6844500, "Shutter Probe K Open")
    prg.add(6854500, "Shutter RepumperMOT K Open")
    prg.add(6864500, "Shutter repump Na Open")
    prg.add(6930000, "Trig ON Stingray 1")
    prg.add(6930019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6932000, "Trig OFF Stingray 1")
    prg.add(7299990, "Pulse uw ON")
    prg.add(7300000, "Pulse uw OFF")
    prg.add(7384500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(7430000, "Trig ON Stingray 1")
    prg.add(7430019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(7431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(7432000, "Trig OFF Stingray 1")
    prg.add(7847500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(7857500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(7876500, "Optical Levit OFF")
    prg.add(7877500, "Shutter 3DMOT cool Na Open")
    prg.add(7888500, "Shutter Optical Levit Close")
    prg.add(8367000, "B comp y", 0.000000)
    prg.add(8367530, "B comp y", 0.260000)
    prg.add(8368049, "B comp y", 0.530000)
    prg.add(8368579, "B comp y", 0.790000)
    prg.add(8369109, "B comp y", 1.050000)
    prg.add(8369630, "B comp y", 1.320000)
    prg.add(8370160, "B comp y", 1.580000)
    prg.add(8370680, "B comp y", 1.840000)
    prg.add(8371210, "B comp y", 2.110000)
    prg.add(8371740, "B comp y", 2.370000)
    prg.add(8372260, "B comp y", 2.630000)
    prg.add(8372790, "B comp y", 2.890000)
    prg.add(8373320, "B comp y", 3.160000)
    prg.add(8373840, "B comp y", 3.420000)
    prg.add(8374370, "B comp y", 3.680000)
    prg.add(8374890, "B comp y", 3.950000)
    prg.add(8375420, "B comp y", 4.210000)
    prg.add(8375950, "B comp y", 4.470000)
    prg.add(8376470, "B comp y", 4.740000)
    prg.add(8376500, "IGBT 1 pinch", -10.000000)
    prg.add(8376520, "IGBT 3 Open")
    prg.add(8376559, "IGBT 2 pinch+comp", 10.000000)
    prg.add(8376660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(8376760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(8376860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(8376960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(8377000, "B comp y", 5.000000)
    prg.add(8377060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(8377160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(8377260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(8377360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(8377460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(8377560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(8377660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(8377760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(8377859, "IGBT 2 pinch+comp", 7.400000)
    prg.add(8377960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(8378060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(8378160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(8378260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(8378360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(8378460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(8378560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(8378660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(8378760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(8378860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(8378960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(8379059, "IGBT 2 pinch+comp", 5.000000)
    prg.add(8379160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(8379260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(8379360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(8379460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(8379560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(8379660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(8379760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(8379860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(8379960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(8380060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(8380160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(8380260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(8380359, "IGBT 2 pinch+comp", 2.400000)
    prg.add(8380460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(8380560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(8380660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(8380760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(8380860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(8380960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(8381060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(8381160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(8381260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(8381360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(8381460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(8381559, "IGBT 2 pinch+comp", 0.000000)
    prg.add(8381660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(8381760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(8381860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(8381960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(8382060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(8382160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(8382260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(8382360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(8382460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(8382560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(8382660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(8382760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(8382859, "IGBT 2 pinch+comp", -2.600000)
    prg.add(8382960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(8383060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(8383160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(8383260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(8383360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(8383460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(8383560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(8383660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(8383760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(8383860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(8383960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(8384059, "IGBT 2 pinch+comp", -5.000000)
    prg.add(8384160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(8384260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(8384360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(8384460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(8384560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(8384660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(8384760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(8384860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(8384960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(8385060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(8385160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(8385260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(8385359, "IGBT 2 pinch+comp", -7.600000)
    prg.add(8385460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(8385560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(8385660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(8385760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(8385860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(8385960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(8386060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(8386160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(8386260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(8386360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(8386460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(8386559, "IGBT 2 pinch+comp", -10.000000)
    prg.add(8386600, "IGBT 4 Open")
    prg.add(8386620, "IGBT 5 Open")
    prg.add(8386849, "IGBT 1 pinch", -10.000000)
    prg.add(8386860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(8386870, "IGBT 3 Close")
    prg.add(8386880, "IGBT 4 Close")
    prg.add(8386890, "IGBT 5 Open")
    prg.add(8386900, "Delta 2 Voltage", 0.000000)
    prg.add(8386910, "Delta 1 Current", 15.270000)
    prg.add(8386950, "B comp x", 0.000000)
    prg.add(8387000, "B comp y", 5.000000)
    prg.add(8387530, "B comp y", 4.740000)
    prg.add(8388049, "B comp y", 4.470000)
    prg.add(8388579, "B comp y", 4.210000)
    prg.add(8389110, "B comp y", 3.950000)
    prg.add(8389630, "B comp y", 3.680000)
    prg.add(8390160, "B comp y", 3.420000)
    prg.add(8390680, "B comp y", 3.160000)
    prg.add(8391210, "B comp y", 2.890000)
    prg.add(8391740, "B comp y", 2.630000)
    prg.add(8392260, "B comp y", 2.370000)
    prg.add(8392790, "B comp y", 2.110000)
    prg.add(8393320, "B comp y", 1.840000)
    prg.add(8393840, "B comp y", 1.580000)
    prg.add(8394370, "B comp y", 1.320000)
    prg.add(8394890, "B comp y", 1.050000)
    prg.add(8395420, "B comp y", 0.790000)
    prg.add(8395950, "B comp y", 0.530000)
    prg.add(8396470, "B comp y", 0.260000)
    prg.add(8397000, "B comp y", 0.000000)
    prg.add(9858500, "B comp y", 1.000000)
    prg.add(9871500, "IGBT 1 pinch", -10.000000)
    prg.add(9871510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(9871520, "IGBT 3 Open")
    prg.add(9871530, "IGBT 4 Open")
    prg.add(9871540, "IGBT 5 Open")
    prg.add(9871550, "IGBT 6 Open")
    prg.add(9871570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9871900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(9875000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(9875500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(9875900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(9876300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9876700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9877000, "Trig Slow Stingray ON")
    prg.add(9877100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(9877500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(9877900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(9878550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9878900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(9879500, "Trig Slow Stingray OFF")
    prg.add(10127500, "Shutter Probe Na Close")
    prg.add(10137500, "Shutter Probe K Close")
    prg.add(10376500, "Optical Levit ON")
    prg.add(10877000, "Trig Slow Stingray ON")
    prg.add(10877500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(10877900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(10878500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(10878900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10879500, "Trig Slow Stingray OFF")
    prg.add(10887500, "Na Repumper MOT Amp", 1.000000)
    prg.add(10897500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(10907500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(11877000, "Trig Slow Stingray ON")
    prg.add(11879000, "Trig Slow Stingray OFF")
    prg.add(12877000, "Trig Slow Stingray ON")
    prg.add(12879000, "Trig Slow Stingray OFF")
    prg.add(13387500, "Optical Levit OFF")
    prg.add(13626500, "Shutter Optical Levit Close")
    prg.add(13877500, "B comp y", 0.000000)
    prg.add(18376500, "Optical Levit ON")
    return prg