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
    prg.add(390000, "Trig ON Stingray 1")
    prg.add(390020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(390500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(391500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(391900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(392000, "Trig OFF Stingray 1")
    prg.add(999960, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1090000, "Trig ON Stingray 1")
    prg.add(1090020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1090500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1091500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1091900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1092000, "Trig OFF Stingray 1")
    prg.add(1699960, "Pulse uw ON")
    prg.add(1700000, "Pulse uw OFF")
    prg.add(1790000, "Trig ON Stingray 1")
    prg.add(1790020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1790500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1791500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1791900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1792000, "Trig OFF Stingray 1")
    prg.add(2399960, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2490000, "Trig ON Stingray 1")
    prg.add(2490020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2490500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2491500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2491900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2492000, "Trig OFF Stingray 1")
    prg.add(3099960, "Pulse uw ON")
    prg.add(3100000, "Pulse uw OFF")
    prg.add(3190000, "Trig ON Stingray 1")
    prg.add(3190020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3190500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3191500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3191900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3192000, "Trig OFF Stingray 1")
    prg.add(3799960, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3890000, "Trig ON Stingray 1")
    prg.add(3890020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3890500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3891500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3891900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3892000, "Trig OFF Stingray 1")
    prg.add(4499960, "Pulse uw ON")
    prg.add(4500000, "Pulse uw OFF")
    prg.add(4590000, "Trig ON Stingray 1")
    prg.add(4590020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4590500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4591500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4591900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4592000, "Trig OFF Stingray 1")
    prg.add(5199960, "Pulse uw ON")
    prg.add(5200000, "Pulse uw OFF")
    prg.add(5290000, "Trig ON Stingray 1")
    prg.add(5290019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5290500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5291500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5291900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5292000, "Trig OFF Stingray 1")
    prg.add(5899960, "Pulse uw ON")
    prg.add(5900000, "Pulse uw OFF")
    prg.add(5990000, "Trig ON Stingray 1")
    prg.add(5990019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5990500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5991500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5991900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5992000, "Trig OFF Stingray 1")
    prg.add(6599960, "Pulse uw ON")
    prg.add(6600000, "Pulse uw OFF")
    prg.add(6690000, "Trig ON Stingray 1")
    prg.add(6690019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6690500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6691500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6691900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6692000, "Trig OFF Stingray 1")
    prg.add(7299960, "Pulse uw ON")
    prg.add(7300000, "Pulse uw OFF")
    prg.add(7390000, "Trig ON Stingray 1")
    prg.add(7390019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7390500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7391500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(7391900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(7392000, "Trig OFF Stingray 1")
    prg.add(7999960, "Pulse uw ON")
    prg.add(8000000, "Pulse uw OFF")
    prg.add(8090000, "Trig ON Stingray 1")
    prg.add(8090019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8090500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8091500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8091900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8092000, "Trig OFF Stingray 1")
    prg.add(8234500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(8244500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(8254500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(8274500, "Na Dark Spot Amp", 1.000000)
    prg.add(8284500, "Na Repumper MOT Amp", 1.000000)
    prg.add(8634500, "Shutter Probe Na Open")
    prg.add(8699960, "Pulse uw ON")
    prg.add(8700000, "Pulse uw OFF")
    prg.add(8790000, "Trig ON Stingray 1")
    prg.add(8790020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8790500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8791500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8791900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8792000, "Trig OFF Stingray 1")
    prg.add(9399960, "Pulse uw ON")
    prg.add(9400000, "Pulse uw OFF")
    prg.add(9490000, "Trig ON Stingray 1")
    prg.add(9490020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9490500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9491500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(9491900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(9492000, "Trig OFF Stingray 1")
    prg.add(9604500, "Shutter Probe K Open")
    prg.add(9614500, "Shutter RepumperMOT K Open")
    prg.add(9624500, "Shutter repump Na Open")
    prg.add(10099960, "Pulse uw ON")
    prg.add(10100000, "Pulse uw OFF")
    prg.add(10144500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10190000, "Trig ON Stingray 1")
    prg.add(10190020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(10190500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(10191500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(10191900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(10192000, "Trig OFF Stingray 1")
    prg.add(10607500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(10617500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(10636500, "Optical Levit OFF")
    prg.add(10637500, "Shutter 3DMOT cool Na Open")
    prg.add(10648500, "Shutter Optical Levit Close")
    prg.add(11127000, "B comp y", 0.000000)
    prg.add(11127530, "B comp y", 0.260000)
    prg.add(11128050, "B comp y", 0.530000)
    prg.add(11128580, "B comp y", 0.790000)
    prg.add(11129110, "B comp y", 1.050000)
    prg.add(11129630, "B comp y", 1.320000)
    prg.add(11130160, "B comp y", 1.580000)
    prg.add(11130680, "B comp y", 1.840000)
    prg.add(11131210, "B comp y", 2.110000)
    prg.add(11131740, "B comp y", 2.370000)
    prg.add(11132260, "B comp y", 2.630000)
    prg.add(11132790, "B comp y", 2.890000)
    prg.add(11133320, "B comp y", 3.160000)
    prg.add(11133840, "B comp y", 3.420000)
    prg.add(11134369, "B comp y", 3.680000)
    prg.add(11134890, "B comp y", 3.950000)
    prg.add(11135420, "B comp y", 4.210000)
    prg.add(11135950, "B comp y", 4.470000)
    prg.add(11136470, "B comp y", 4.740000)
    prg.add(11136500, "IGBT 1 pinch", -10.000000)
    prg.add(11136520, "IGBT 3 Open")
    prg.add(11136560, "IGBT 2 pinch+comp", 10.000000)
    prg.add(11136660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(11136760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(11136860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(11136960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(11137000, "B comp y", 5.000000)
    prg.add(11137059, "IGBT 2 pinch+comp", 9.000000)
    prg.add(11137159, "IGBT 2 pinch+comp", 8.800000)
    prg.add(11137260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(11137360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(11137460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(11137560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(11137660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(11137760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(11137860, "IGBT 2 pinch+comp", 7.400000)
    prg.add(11137960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(11138060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(11138160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(11138260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(11138360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(11138460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(11138560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(11138660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(11138760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(11138860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(11138960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(11139060, "IGBT 2 pinch+comp", 5.000000)
    prg.add(11139160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(11139260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(11139360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(11139460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(11139559, "IGBT 2 pinch+comp", 4.000000)
    prg.add(11139659, "IGBT 2 pinch+comp", 3.800000)
    prg.add(11139760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(11139860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(11139960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(11140060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(11140160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(11140260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(11140360, "IGBT 2 pinch+comp", 2.400000)
    prg.add(11140460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(11140560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(11140660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(11140760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(11140860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(11140960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(11141060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(11141160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(11141260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(11141360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(11141460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(11141560, "IGBT 2 pinch+comp", 0.000000)
    prg.add(11141660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(11141760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(11141860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(11141960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(11142059, "IGBT 2 pinch+comp", -1.000000)
    prg.add(11142159, "IGBT 2 pinch+comp", -1.200000)
    prg.add(11142260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(11142360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(11142460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(11142560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(11142660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(11142760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(11142860, "IGBT 2 pinch+comp", -2.600000)
    prg.add(11142960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(11143060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(11143160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(11143260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(11143360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(11143460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(11143560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(11143660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(11143760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(11143860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(11143960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(11144060, "IGBT 2 pinch+comp", -5.000000)
    prg.add(11144160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(11144260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(11144360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(11144460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(11144559, "IGBT 2 pinch+comp", -6.000000)
    prg.add(11144659, "IGBT 2 pinch+comp", -6.200000)
    prg.add(11144760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(11144860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(11144960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(11145060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(11145160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(11145260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(11145360, "IGBT 2 pinch+comp", -7.600000)
    prg.add(11145460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(11145560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(11145660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(11145760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(11145860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(11145960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(11146060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(11146160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(11146260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(11146360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(11146460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(11146560, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11146600, "IGBT 4 Open")
    prg.add(11146620, "IGBT 5 Open")
    prg.add(11146850, "IGBT 1 pinch", -10.000000)
    prg.add(11146860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11146869, "IGBT 3 Close")
    prg.add(11146880, "IGBT 4 Close")
    prg.add(11146890, "IGBT 5 Open")
    prg.add(11146900, "Delta 2 Voltage", 0.000000)
    prg.add(11146910, "Delta 1 Current", 15.400000)
    prg.add(11146950, "B comp x", 0.000000)
    prg.add(11147000, "B comp y", 5.000000)
    prg.add(11147530, "B comp y", 4.740000)
    prg.add(11148050, "B comp y", 4.470000)
    prg.add(11148580, "B comp y", 4.210000)
    prg.add(11149110, "B comp y", 3.950000)
    prg.add(11149630, "B comp y", 3.680000)
    prg.add(11150160, "B comp y", 3.420000)
    prg.add(11150680, "B comp y", 3.160000)
    prg.add(11151210, "B comp y", 2.890000)
    prg.add(11151740, "B comp y", 2.630000)
    prg.add(11152260, "B comp y", 2.370000)
    prg.add(11152790, "B comp y", 2.110000)
    prg.add(11153320, "B comp y", 1.840000)
    prg.add(11153840, "B comp y", 1.580000)
    prg.add(11154369, "B comp y", 1.320000)
    prg.add(11154890, "B comp y", 1.050000)
    prg.add(11155420, "B comp y", 0.790000)
    prg.add(11155950, "B comp y", 0.530000)
    prg.add(11156470, "B comp y", 0.260000)
    prg.add(11157000, "B comp y", 0.000000)
    prg.add(12618500, "B comp y", 1.000000)
    prg.add(12631500, "IGBT 1 pinch", -10.000000)
    prg.add(12631510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(12631520, "IGBT 3 Open")
    prg.add(12631530, "IGBT 4 Open")
    prg.add(12631540, "IGBT 5 Open")
    prg.add(12631550, "IGBT 6 Open")
    prg.add(12631570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12631900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(12635000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(12635500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(12635900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(12636300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(12636700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(12637000, "Trig Slow Stingray ON")
    prg.add(12637100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(12637500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(12637900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(12638550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12638900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(12639500, "Trig Slow Stingray OFF")
    prg.add(12887500, "Shutter Probe Na Close")
    prg.add(12897500, "Shutter Probe K Close")
    prg.add(13136500, "Optical Levit ON")
    prg.add(13637000, "Trig Slow Stingray ON")
    prg.add(13637500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(13637900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(13638500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(13638900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(13639500, "Trig Slow Stingray OFF")
    prg.add(13647500, "Na Repumper MOT Amp", 1.000000)
    prg.add(13657500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(13667500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(14637000, "Trig Slow Stingray ON")
    prg.add(14639000, "Trig Slow Stingray OFF")
    prg.add(15637000, "Trig Slow Stingray ON")
    prg.add(15639000, "Trig Slow Stingray OFF")
    prg.add(16147500, "Optical Levit OFF")
    prg.add(16386500, "Shutter Optical Levit Close")
    prg.add(16637500, "B comp y", 0.000000)
    prg.add(21136500, "Optical Levit ON")
    return prg
