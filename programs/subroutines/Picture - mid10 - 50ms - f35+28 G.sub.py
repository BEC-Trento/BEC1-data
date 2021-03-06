prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4002500, "Shutter Probe Na Open")
    prg.add(-3512500, "Na Probe/Push (-) freq", 150.000000)
    prg.add(-3502500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(-732000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(-724500, "Optical Levit ON")
    prg.add(-722000, "K probe Repumper (+) Amp", 1.000000)
    prg.add(-712000, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(-692000, "Na Dark Spot Amp", 1.000000)
    prg.add(-682000, "Na Repumper MOT Amp", 1.000000)
    prg.add(-332000, "Shutter Probe Na Open")
    prg.add(0, "Trig ON Stingray 1")
    prg.add(20, "Na Probe/Push (-) freq", 110.000000)
    prg.add(500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(299964, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(430000, "Trig ON Stingray 1")
    prg.add(430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(432000, "Trig OFF Stingray 1")
    prg.add(638000, "Shutter Probe K Open")
    prg.add(648000, "Shutter RepumperMOT K Open")
    prg.add(649964, "Pulse uw ON")
    prg.add(650000, "Pulse uw OFF")
    prg.add(658000, "Shutter repump Na Open")
    prg.add(780000, "Trig ON Stingray 1")
    prg.add(780020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(780500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(781500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(781900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(782000, "Trig OFF Stingray 1")
    prg.add(929963, "Pulse uw ON")
    prg.add(930000, "Pulse uw OFF")
    prg.add(1060000, "Trig ON Stingray 1")
    prg.add(1060020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1060500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1061500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1061900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1062000, "Trig OFF Stingray 1")
    prg.add(1178000, "K probe Cooler (-) Amp", 1.000000)
    prg.add(1209962, "Pulse uw ON")
    prg.add(1210000, "Pulse uw OFF")
    prg.add(1340000, "Trig ON Stingray 1")
    prg.add(1340020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1340500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1341500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1341900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1342000, "Trig OFF Stingray 1")
    prg.add(1489960, "Pulse uw ON")
    prg.add(1490000, "Pulse uw OFF")
    prg.add(1620000, "Trig ON Stingray 1")
    prg.add(1620020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1620500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1621500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1621900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1622000, "Trig OFF Stingray 1")
    prg.add(1641000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(1651000, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(1670000, "Optical Levit OFF")
    prg.add(1671000, "Shutter 3DMOT cool Na Open")
    prg.add(1682000, "Shutter Optical Levit Close")
    prg.add(1769957, "Pulse uw ON")
    prg.add(1770000, "Pulse uw OFF")
    prg.add(1900000, "Trig ON Stingray 1")
    prg.add(1900020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1900500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1901500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1901900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1902000, "Trig OFF Stingray 1")
    prg.add(2049956, "Pulse uw ON")
    prg.add(2050000, "Pulse uw OFF")
    prg.add(2180000, "Trig ON Stingray 1")
    prg.add(2180020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2180500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2181500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2181900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2182000, "Trig OFF Stingray 1")
    prg.add(2329955, "Pulse uw ON")
    prg.add(2330000, "Pulse uw OFF")
    prg.add(2460000, "Trig ON Stingray 1")
    prg.add(2460020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2460500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2461500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2461900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2462000, "Trig OFF Stingray 1")
    prg.add(2609953, "Pulse uw ON")
    prg.add(2610000, "Pulse uw OFF")
    prg.add(2740000, "Trig ON Stingray 1")
    prg.add(2740020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2740500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2741500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2741900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2742000, "Trig OFF Stingray 1")
    prg.add(2889952, "Pulse uw ON")
    prg.add(2890000, "Pulse uw OFF")
    prg.add(3020000, "Trig ON Stingray 1")
    prg.add(3020020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3020500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3021500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3021900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3022000, "Trig OFF Stingray 1")
    prg.add(3160500, "B comp y", 0.000000)
    prg.add(3161030, "B comp y", 0.260000)
    prg.add(3161549, "B comp y", 0.530000)
    prg.add(3162080, "B comp y", 0.790000)
    prg.add(3162610, "B comp y", 1.050000)
    prg.add(3163130, "B comp y", 1.320000)
    prg.add(3163660, "B comp y", 1.580000)
    prg.add(3164180, "B comp y", 1.840000)
    prg.add(3164710, "B comp y", 2.110000)
    prg.add(3165240, "B comp y", 2.370000)
    prg.add(3165760, "B comp y", 2.630000)
    prg.add(3166290, "B comp y", 2.890000)
    prg.add(3166820, "B comp y", 3.160000)
    prg.add(3167340, "B comp y", 3.420000)
    prg.add(3167870, "B comp y", 3.680000)
    prg.add(3168390, "B comp y", 3.950000)
    prg.add(3168920, "B comp y", 4.210000)
    prg.add(3169450, "B comp y", 4.470000)
    prg.add(3169970, "B comp y", 4.740000)
    prg.add(3170000, "IGBT 1 pinch", -10.000000)
    prg.add(3170020, "IGBT 3 Open")
    prg.add(3170059, "IGBT 2 pinch+comp", 10.000000)
    prg.add(3170160, "IGBT 2 pinch+comp", 9.800000)
    prg.add(3170260, "IGBT 2 pinch+comp", 9.600000)
    prg.add(3170360, "IGBT 2 pinch+comp", 9.400000)
    prg.add(3170460, "IGBT 2 pinch+comp", 9.200000)
    prg.add(3170500, "B comp y", 5.000000)
    prg.add(3170560, "IGBT 2 pinch+comp", 9.000000)
    prg.add(3170659, "IGBT 2 pinch+comp", 8.800000)
    prg.add(3170760, "IGBT 2 pinch+comp", 8.600000)
    prg.add(3170860, "IGBT 2 pinch+comp", 8.400000)
    prg.add(3170960, "IGBT 2 pinch+comp", 8.200000)
    prg.add(3171060, "IGBT 2 pinch+comp", 8.000000)
    prg.add(3171160, "IGBT 2 pinch+comp", 7.800000)
    prg.add(3171259, "IGBT 2 pinch+comp", 7.600000)
    prg.add(3171360, "IGBT 2 pinch+comp", 7.400000)
    prg.add(3171460, "IGBT 2 pinch+comp", 7.200000)
    prg.add(3171560, "IGBT 2 pinch+comp", 7.000000)
    prg.add(3171660, "IGBT 2 pinch+comp", 6.800000)
    prg.add(3171760, "IGBT 2 pinch+comp", 6.600000)
    prg.add(3171860, "IGBT 2 pinch+comp", 6.400000)
    prg.add(3171960, "IGBT 2 pinch+comp", 6.200000)
    prg.add(3172060, "IGBT 2 pinch+comp", 6.000000)
    prg.add(3172160, "IGBT 2 pinch+comp", 5.800000)
    prg.add(3172260, "IGBT 2 pinch+comp", 5.600000)
    prg.add(3172360, "IGBT 2 pinch+comp", 5.400000)
    prg.add(3172460, "IGBT 2 pinch+comp", 5.200000)
    prg.add(3172559, "IGBT 2 pinch+comp", 5.000000)
    prg.add(3172660, "IGBT 2 pinch+comp", 4.800000)
    prg.add(3172760, "IGBT 2 pinch+comp", 4.600000)
    prg.add(3172860, "IGBT 2 pinch+comp", 4.400000)
    prg.add(3172960, "IGBT 2 pinch+comp", 4.200000)
    prg.add(3173060, "IGBT 2 pinch+comp", 4.000000)
    prg.add(3173159, "IGBT 2 pinch+comp", 3.800000)
    prg.add(3173260, "IGBT 2 pinch+comp", 3.600000)
    prg.add(3173360, "IGBT 2 pinch+comp", 3.400000)
    prg.add(3173460, "IGBT 2 pinch+comp", 3.200000)
    prg.add(3173560, "IGBT 2 pinch+comp", 3.000000)
    prg.add(3173660, "IGBT 2 pinch+comp", 2.800000)
    prg.add(3173759, "IGBT 2 pinch+comp", 2.600000)
    prg.add(3173860, "IGBT 2 pinch+comp", 2.400000)
    prg.add(3173960, "IGBT 2 pinch+comp", 2.200000)
    prg.add(3174060, "IGBT 2 pinch+comp", 2.000000)
    prg.add(3174160, "IGBT 2 pinch+comp", 1.800000)
    prg.add(3174260, "IGBT 2 pinch+comp", 1.600000)
    prg.add(3174360, "IGBT 2 pinch+comp", 1.400000)
    prg.add(3174460, "IGBT 2 pinch+comp", 1.200000)
    prg.add(3174560, "IGBT 2 pinch+comp", 1.000000)
    prg.add(3174660, "IGBT 2 pinch+comp", 0.800000)
    prg.add(3174760, "IGBT 2 pinch+comp", 0.600000)
    prg.add(3174860, "IGBT 2 pinch+comp", 0.400000)
    prg.add(3174960, "IGBT 2 pinch+comp", 0.200000)
    prg.add(3175059, "IGBT 2 pinch+comp", 0.000000)
    prg.add(3175160, "IGBT 2 pinch+comp", -0.200000)
    prg.add(3175260, "IGBT 2 pinch+comp", -0.400000)
    prg.add(3175360, "IGBT 2 pinch+comp", -0.600000)
    prg.add(3175460, "IGBT 2 pinch+comp", -0.800000)
    prg.add(3175560, "IGBT 2 pinch+comp", -1.000000)
    prg.add(3175659, "IGBT 2 pinch+comp", -1.200000)
    prg.add(3175760, "IGBT 2 pinch+comp", -1.400000)
    prg.add(3175860, "IGBT 2 pinch+comp", -1.600000)
    prg.add(3175960, "IGBT 2 pinch+comp", -1.800000)
    prg.add(3176060, "IGBT 2 pinch+comp", -2.000000)
    prg.add(3176160, "IGBT 2 pinch+comp", -2.200000)
    prg.add(3176259, "IGBT 2 pinch+comp", -2.400000)
    prg.add(3176360, "IGBT 2 pinch+comp", -2.600000)
    prg.add(3176460, "IGBT 2 pinch+comp", -2.800000)
    prg.add(3176560, "IGBT 2 pinch+comp", -3.000000)
    prg.add(3176660, "IGBT 2 pinch+comp", -3.200000)
    prg.add(3176760, "IGBT 2 pinch+comp", -3.400000)
    prg.add(3176860, "IGBT 2 pinch+comp", -3.600000)
    prg.add(3176960, "IGBT 2 pinch+comp", -3.800000)
    prg.add(3177060, "IGBT 2 pinch+comp", -4.000000)
    prg.add(3177160, "IGBT 2 pinch+comp", -4.200000)
    prg.add(3177260, "IGBT 2 pinch+comp", -4.400000)
    prg.add(3177360, "IGBT 2 pinch+comp", -4.600000)
    prg.add(3177460, "IGBT 2 pinch+comp", -4.800000)
    prg.add(3177559, "IGBT 2 pinch+comp", -5.000000)
    prg.add(3177660, "IGBT 2 pinch+comp", -5.200000)
    prg.add(3177760, "IGBT 2 pinch+comp", -5.400000)
    prg.add(3177860, "IGBT 2 pinch+comp", -5.600000)
    prg.add(3177960, "IGBT 2 pinch+comp", -5.800000)
    prg.add(3178060, "IGBT 2 pinch+comp", -6.000000)
    prg.add(3178159, "IGBT 2 pinch+comp", -6.200000)
    prg.add(3178260, "IGBT 2 pinch+comp", -6.400000)
    prg.add(3178360, "IGBT 2 pinch+comp", -6.600000)
    prg.add(3178460, "IGBT 2 pinch+comp", -6.800000)
    prg.add(3178560, "IGBT 2 pinch+comp", -7.000000)
    prg.add(3178660, "IGBT 2 pinch+comp", -7.200000)
    prg.add(3178759, "IGBT 2 pinch+comp", -7.400000)
    prg.add(3178860, "IGBT 2 pinch+comp", -7.600000)
    prg.add(3178960, "IGBT 2 pinch+comp", -7.800000)
    prg.add(3179060, "IGBT 2 pinch+comp", -8.000000)
    prg.add(3179160, "IGBT 2 pinch+comp", -8.200000)
    prg.add(3179260, "IGBT 2 pinch+comp", -8.400000)
    prg.add(3179360, "IGBT 2 pinch+comp", -8.600000)
    prg.add(3179460, "IGBT 2 pinch+comp", -8.800000)
    prg.add(3179560, "IGBT 2 pinch+comp", -9.000000)
    prg.add(3179660, "IGBT 2 pinch+comp", -9.200000)
    prg.add(3179760, "IGBT 2 pinch+comp", -9.400000)
    prg.add(3179860, "IGBT 2 pinch+comp", -9.600000)
    prg.add(3179960, "IGBT 2 pinch+comp", -9.800000)
    prg.add(3180059, "IGBT 2 pinch+comp", -10.000000)
    prg.add(3180100, "IGBT 4 Open")
    prg.add(3180120, "IGBT 5 Open")
    prg.add(3180350, "IGBT 1 pinch", -10.000000)
    prg.add(3180360, "IGBT 2 pinch+comp", -10.000000)
    prg.add(3180370, "IGBT 3 Close")
    prg.add(3180380, "IGBT 4 Close")
    prg.add(3180390, "IGBT 5 Open")
    prg.add(3180400, "Delta 2 Voltage", 0.000000)
    prg.add(3180410, "Delta 1 Current", 15.400000)
    prg.add(3180450, "B comp x", 0.000000)
    prg.add(3180500, "B comp y", 5.000000)
    prg.add(3181030, "B comp y", 4.740000)
    prg.add(3181549, "B comp y", 4.470000)
    prg.add(3182080, "B comp y", 4.210000)
    prg.add(3182610, "B comp y", 3.950000)
    prg.add(3183130, "B comp y", 3.680000)
    prg.add(3183660, "B comp y", 3.420000)
    prg.add(3184180, "B comp y", 3.160000)
    prg.add(3184710, "B comp y", 2.890000)
    prg.add(3185240, "B comp y", 2.630000)
    prg.add(3185760, "B comp y", 2.370000)
    prg.add(3186290, "B comp y", 2.110000)
    prg.add(3186820, "B comp y", 1.840000)
    prg.add(3187340, "B comp y", 1.580000)
    prg.add(3187870, "B comp y", 1.320000)
    prg.add(3188390, "B comp y", 1.050000)
    prg.add(3188920, "B comp y", 0.790000)
    prg.add(3189450, "B comp y", 0.530000)
    prg.add(3189970, "B comp y", 0.260000)
    prg.add(3190500, "B comp y", 0.000000)
    prg.add(3652000, "B comp y", 1.000000)
    prg.add(3665000, "IGBT 1 pinch", -10.000000)
    prg.add(3665009, "IGBT 2 pinch+comp", -10.000000)
    prg.add(3665020, "IGBT 3 Open")
    prg.add(3665030, "IGBT 4 Open")
    prg.add(3665040, "IGBT 5 Open")
    prg.add(3665050, "IGBT 6 Open")
    prg.add(3665070, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3665400, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(3668500, "Na Repumper MOT Amp", 1000.000000)
    prg.add(3669000, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(3669400, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(3669800, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3670200, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3670500, "Trig Slow Stingray ON")
    prg.add(3670600, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(3671000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(3671400, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(3672050, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3672400, "K probe Cooler (-) Amp", 1.000000)
    prg.add(3673000, "Trig Slow Stingray OFF")
    prg.add(3921000, "Shutter Probe Na Close")
    prg.add(3931000, "Shutter Probe K Close")
    prg.add(4170000, "Optical Levit ON")
    prg.add(4670500, "Trig Slow Stingray ON")
    prg.add(4671000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(4671400, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(4672000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(4672400, "K probe Cooler (-) Amp", 1.000000)
    prg.add(4673000, "Trig Slow Stingray OFF")
    prg.add(4681000, "Na Repumper MOT Amp", 1.000000)
    prg.add(4691000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(4701000, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(5670500, "Trig Slow Stingray ON")
    prg.add(5672500, "Trig Slow Stingray OFF")
    prg.add(6670500, "Trig Slow Stingray ON")
    prg.add(6672500, "Trig Slow Stingray OFF")
    prg.add(7181000, "Optical Levit OFF")
    prg.add(7420000, "Shutter Optical Levit Close")
    prg.add(7671000, "B comp y", 0.000000)
    prg.add(12170000, "Optical Levit ON")
    return prg
