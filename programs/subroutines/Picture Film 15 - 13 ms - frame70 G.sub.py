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
    prg.add(299970, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(430000, "Trig ON Stingray 1")
    prg.add(430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(432000, "Trig OFF Stingray 1")
    prg.add(999960, "Pulse uw ON")
    prg.add(1000000, "Pulse uw OFF")
    prg.add(1130000, "Trig ON Stingray 1")
    prg.add(1130020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1130500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1131500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1131900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1132000, "Trig OFF Stingray 1")
    prg.add(1699960, "Pulse uw ON")
    prg.add(1700000, "Pulse uw OFF")
    prg.add(1830000, "Trig ON Stingray 1")
    prg.add(1830020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1830500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1831500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1831900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1832000, "Trig OFF Stingray 1")
    prg.add(2399960, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2530000, "Trig ON Stingray 1")
    prg.add(2530020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2530500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2531500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2531900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2532000, "Trig OFF Stingray 1")
    prg.add(3099960, "Pulse uw ON")
    prg.add(3100000, "Pulse uw OFF")
    prg.add(3230000, "Trig ON Stingray 1")
    prg.add(3230020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3230500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3231500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3231900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3232000, "Trig OFF Stingray 1")
    prg.add(3799960, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3930000, "Trig ON Stingray 1")
    prg.add(3930020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3930500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3931500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3931900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3932000, "Trig OFF Stingray 1")
    prg.add(4499960, "Pulse uw ON")
    prg.add(4500000, "Pulse uw OFF")
    prg.add(4630000, "Trig ON Stingray 1")
    prg.add(4630020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4630500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4631500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4631900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4632000, "Trig OFF Stingray 1")
    prg.add(5199960, "Pulse uw ON")
    prg.add(5200000, "Pulse uw OFF")
    prg.add(5330000, "Trig ON Stingray 1")
    prg.add(5330019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5330500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5331500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5331900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5332000, "Trig OFF Stingray 1")
    prg.add(5899960, "Pulse uw ON")
    prg.add(5900000, "Pulse uw OFF")
    prg.add(6030000, "Trig ON Stingray 1")
    prg.add(6030019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6030500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6031500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6031900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6032000, "Trig OFF Stingray 1")
    prg.add(6599960, "Pulse uw ON")
    prg.add(6600000, "Pulse uw OFF")
    prg.add(6730000, "Trig ON Stingray 1")
    prg.add(6730019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(6730500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(6731500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(6731900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(6732000, "Trig OFF Stingray 1")
    prg.add(7299960, "Pulse uw ON")
    prg.add(7300000, "Pulse uw OFF")
    prg.add(7430000, "Trig ON Stingray 1")
    prg.add(7430019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(7431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(7432000, "Trig OFF Stingray 1")
    prg.add(7999960, "Pulse uw ON")
    prg.add(8000000, "Pulse uw OFF")
    prg.add(8130000, "Trig ON Stingray 1")
    prg.add(8130019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8130500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8131500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8131900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8132000, "Trig OFF Stingray 1")
    prg.add(8274500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(8284500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(8294500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(8314500, "Na Dark Spot Amp", 1.000000)
    prg.add(8324500, "Na Repumper MOT Amp", 1.000000)
    prg.add(8674500, "Shutter Probe Na Open")
    prg.add(8699960, "Pulse uw ON")
    prg.add(8700000, "Pulse uw OFF")
    prg.add(8830000, "Trig ON Stingray 1")
    prg.add(8830020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8830500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8831500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8831900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8832000, "Trig OFF Stingray 1")
    prg.add(9399960, "Pulse uw ON")
    prg.add(9400000, "Pulse uw OFF")
    prg.add(9530000, "Trig ON Stingray 1")
    prg.add(9530020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9530500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9531500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(9531900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(9532000, "Trig OFF Stingray 1")
    prg.add(9644500, "Shutter Probe K Open")
    prg.add(9654500, "Shutter RepumperMOT K Open")
    prg.add(9664500, "Shutter repump Na Open")
    prg.add(10099960, "Pulse uw ON")
    prg.add(10100000, "Pulse uw OFF")
    prg.add(10184500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(10230000, "Trig ON Stingray 1")
    prg.add(10230020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(10230500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(10231500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(10231900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(10232000, "Trig OFF Stingray 1")
    prg.add(10647500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(10657500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(10676500, "Optical Levit OFF")
    prg.add(10677500, "Shutter 3DMOT cool Na Open")
    prg.add(10688500, "Shutter Optical Levit Close")
    prg.add(11167000, "B comp y", 0.000000)
    prg.add(11167530, "B comp y", 0.260000)
    prg.add(11168050, "B comp y", 0.530000)
    prg.add(11168580, "B comp y", 0.790000)
    prg.add(11169110, "B comp y", 1.050000)
    prg.add(11169630, "B comp y", 1.320000)
    prg.add(11170160, "B comp y", 1.580000)
    prg.add(11170680, "B comp y", 1.840000)
    prg.add(11171210, "B comp y", 2.110000)
    prg.add(11171740, "B comp y", 2.370000)
    prg.add(11172260, "B comp y", 2.630000)
    prg.add(11172790, "B comp y", 2.890000)
    prg.add(11173320, "B comp y", 3.160000)
    prg.add(11173840, "B comp y", 3.420000)
    prg.add(11174369, "B comp y", 3.680000)
    prg.add(11174890, "B comp y", 3.950000)
    prg.add(11175420, "B comp y", 4.210000)
    prg.add(11175950, "B comp y", 4.470000)
    prg.add(11176470, "B comp y", 4.740000)
    prg.add(11176500, "IGBT 1 pinch", -10.000000)
    prg.add(11176520, "IGBT 3 Open")
    prg.add(11176560, "IGBT 2 pinch+comp", 10.000000)
    prg.add(11176660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(11176760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(11176860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(11176960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(11177000, "B comp y", 5.000000)
    prg.add(11177059, "IGBT 2 pinch+comp", 9.000000)
    prg.add(11177159, "IGBT 2 pinch+comp", 8.800000)
    prg.add(11177260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(11177360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(11177460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(11177560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(11177660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(11177760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(11177860, "IGBT 2 pinch+comp", 7.400000)
    prg.add(11177960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(11178060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(11178160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(11178260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(11178360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(11178460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(11178560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(11178660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(11178760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(11178860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(11178960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(11179060, "IGBT 2 pinch+comp", 5.000000)
    prg.add(11179160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(11179260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(11179360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(11179460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(11179559, "IGBT 2 pinch+comp", 4.000000)
    prg.add(11179659, "IGBT 2 pinch+comp", 3.800000)
    prg.add(11179760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(11179860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(11179960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(11180060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(11180160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(11180260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(11180360, "IGBT 2 pinch+comp", 2.400000)
    prg.add(11180460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(11180560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(11180660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(11180760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(11180860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(11180960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(11181060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(11181160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(11181260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(11181360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(11181460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(11181560, "IGBT 2 pinch+comp", 0.000000)
    prg.add(11181660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(11181760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(11181860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(11181960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(11182059, "IGBT 2 pinch+comp", -1.000000)
    prg.add(11182159, "IGBT 2 pinch+comp", -1.200000)
    prg.add(11182260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(11182360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(11182460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(11182560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(11182660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(11182760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(11182860, "IGBT 2 pinch+comp", -2.600000)
    prg.add(11182960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(11183060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(11183160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(11183260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(11183360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(11183460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(11183560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(11183660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(11183760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(11183860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(11183960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(11184060, "IGBT 2 pinch+comp", -5.000000)
    prg.add(11184160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(11184260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(11184360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(11184460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(11184559, "IGBT 2 pinch+comp", -6.000000)
    prg.add(11184659, "IGBT 2 pinch+comp", -6.200000)
    prg.add(11184760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(11184860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(11184960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(11185060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(11185160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(11185260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(11185360, "IGBT 2 pinch+comp", -7.600000)
    prg.add(11185460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(11185560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(11185660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(11185760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(11185860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(11185960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(11186060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(11186160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(11186260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(11186360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(11186460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(11186560, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11186600, "IGBT 4 Open")
    prg.add(11186620, "IGBT 5 Open")
    prg.add(11186850, "IGBT 1 pinch", -10.000000)
    prg.add(11186860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(11186869, "IGBT 3 Close")
    prg.add(11186880, "IGBT 4 Close")
    prg.add(11186890, "IGBT 5 Open")
    prg.add(11186900, "Delta 2 Voltage", 0.000000)
    prg.add(11186910, "Delta 1 Current", 15.400000)
    prg.add(11186950, "B comp x", 0.000000)
    prg.add(11187000, "B comp y", 5.000000)
    prg.add(11187530, "B comp y", 4.740000)
    prg.add(11188050, "B comp y", 4.470000)
    prg.add(11188580, "B comp y", 4.210000)
    prg.add(11189110, "B comp y", 3.950000)
    prg.add(11189630, "B comp y", 3.680000)
    prg.add(11190160, "B comp y", 3.420000)
    prg.add(11190680, "B comp y", 3.160000)
    prg.add(11191210, "B comp y", 2.890000)
    prg.add(11191740, "B comp y", 2.630000)
    prg.add(11192260, "B comp y", 2.370000)
    prg.add(11192790, "B comp y", 2.110000)
    prg.add(11193320, "B comp y", 1.840000)
    prg.add(11193840, "B comp y", 1.580000)
    prg.add(11194369, "B comp y", 1.320000)
    prg.add(11194890, "B comp y", 1.050000)
    prg.add(11195420, "B comp y", 0.790000)
    prg.add(11195950, "B comp y", 0.530000)
    prg.add(11196470, "B comp y", 0.260000)
    prg.add(11197000, "B comp y", 0.000000)
    prg.add(12658500, "B comp y", 1.000000)
    prg.add(12671500, "IGBT 1 pinch", -10.000000)
    prg.add(12671510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(12671520, "IGBT 3 Open")
    prg.add(12671530, "IGBT 4 Open")
    prg.add(12671540, "IGBT 5 Open")
    prg.add(12671550, "IGBT 6 Open")
    prg.add(12671570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12671900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(12675000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(12675500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(12675900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(12676300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(12676700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(12677000, "Trig Slow Stingray ON")
    prg.add(12677100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(12677500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(12677900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(12678550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(12678900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(12679500, "Trig Slow Stingray OFF")
    prg.add(12927500, "Shutter Probe Na Close")
    prg.add(12937500, "Shutter Probe K Close")
    prg.add(13176500, "Optical Levit ON")
    prg.add(13677000, "Trig Slow Stingray ON")
    prg.add(13677500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(13677900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(13678500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(13678900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(13679500, "Trig Slow Stingray OFF")
    prg.add(13687500, "Na Repumper MOT Amp", 1.000000)
    prg.add(13697500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(13707500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(14677000, "Trig Slow Stingray ON")
    prg.add(14679000, "Trig Slow Stingray OFF")
    prg.add(15677000, "Trig Slow Stingray ON")
    prg.add(15679000, "Trig Slow Stingray OFF")
    prg.add(16187500, "Optical Levit OFF")
    prg.add(16426500, "Shutter Optical Levit Close")
    prg.add(16677500, "B comp y", 0.000000)
    prg.add(21176500, "Optical Levit ON")
    return prg
