prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4002500, "Shutter Probe Na Open")
    prg.add(-3512500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-3502500, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-724500, "Optical Levit ON")
    prg.add(-700, "Na Probe/Push (+) freq", 110.000000)
    prg.add(-300, "Na Probe/Push (-) freq", 110.000000)
    prg.add(0, "Trig ON Stingray 1")
    prg.add(100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(299950, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(335000, "Trig ON Stingray 1")
    prg.add(335500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(336500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(337000, "Trig OFF Stingray 1")
    prg.add(599950, "Pulse uw ON")
    prg.add(600000, "Pulse uw OFF")
    prg.add(635000, "Trig ON Stingray 1")
    prg.add(635500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(636500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(637000, "Trig OFF Stingray 1")
    prg.add(899950, "Pulse uw ON")
    prg.add(900000, "Pulse uw OFF")
    prg.add(935000, "Trig ON Stingray 1")
    prg.add(935500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(936500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(937000, "Trig OFF Stingray 1")
    prg.add(1079500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(1089500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(1099500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(1119500, "Na Dark Spot Amp", 1.000000)
    prg.add(1129500, "Na Repumper MOT Amp", 1.000000)
    prg.add(1199950, "Pulse uw ON")
    prg.add(1200000, "Pulse uw OFF")
    prg.add(1235000, "Trig ON Stingray 1")
    prg.add(1235500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1236500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1237000, "Trig OFF Stingray 1")
    prg.add(1479500, "Shutter Probe Na Open")
    prg.add(1499950, "Pulse uw ON")
    prg.add(1500000, "Pulse uw OFF")
    prg.add(1535000, "Trig ON Stingray 1")
    prg.add(1535500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1536500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1537000, "Trig OFF Stingray 1")
    prg.add(1799950, "Pulse uw ON")
    prg.add(1800000, "Pulse uw OFF")
    prg.add(1835000, "Trig ON Stingray 1")
    prg.add(1835500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1836500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1837000, "Trig OFF Stingray 1")
    prg.add(1969500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2099950, "Pulse uw ON")
    prg.add(2100000, "Pulse uw OFF")
    prg.add(2135000, "Trig ON Stingray 1")
    prg.add(2135500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2136500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2137000, "Trig OFF Stingray 1")
    prg.add(2399950, "Pulse uw ON")
    prg.add(2400000, "Pulse uw OFF")
    prg.add(2435000, "Trig ON Stingray 1")
    prg.add(2435500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2436500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2437000, "Trig OFF Stingray 1")
    prg.add(2449500, "Shutter Probe K Open")
    prg.add(2459500, "Shutter RepumperMOT K Open")
    prg.add(2469500, "Shutter repump Na Open")
    prg.add(2699950, "Pulse uw ON")
    prg.add(2700000, "Pulse uw OFF")
    prg.add(2735000, "Trig ON Stingray 1")
    prg.add(2735500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(2736500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(2737000, "Trig OFF Stingray 1")
    prg.add(2989500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(2999950, "Pulse uw ON")
    prg.add(3000000, "Pulse uw OFF")
    prg.add(3035000, "Trig ON Stingray 1")
    prg.add(3035500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(3036500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3037000, "Trig OFF Stingray 1")
    prg.add(3452500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(3462500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(3481500, "Optical Levit OFF")
    prg.add(3482500, "Shutter 3DMOT cool Na Open")
    prg.add(3493500, "Shutter Optical Levit Close")
    prg.add(3972000, "B comp y", 0.000000)
    prg.add(3972530, "B comp y", 0.260000)
    prg.add(3973050, "B comp y", 0.530000)
    prg.add(3973580, "B comp y", 0.790000)
    prg.add(3974110, "B comp y", 1.050000)
    prg.add(3974630, "B comp y", 1.320000)
    prg.add(3975160, "B comp y", 1.580000)
    prg.add(3975680, "B comp y", 1.840000)
    prg.add(3976210, "B comp y", 2.110000)
    prg.add(3976740, "B comp y", 2.370000)
    prg.add(3977260, "B comp y", 2.630000)
    prg.add(3977790, "B comp y", 2.890000)
    prg.add(3978320, "B comp y", 3.160000)
    prg.add(3978840, "B comp y", 3.420000)
    prg.add(3979370, "B comp y", 3.680000)
    prg.add(3979889, "B comp y", 3.950000)
    prg.add(3980419, "B comp y", 4.210000)
    prg.add(3980950, "B comp y", 4.470000)
    prg.add(3981470, "B comp y", 4.740000)
    prg.add(3981500, "IGBT 1 pinch", -10.000000)
    prg.add(3981520, "IGBT 3 Open")
    prg.add(3981560, "IGBT 2 pinch+comp", 10.000000)
    prg.add(3981660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(3981760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(3981860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(3981960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(3982000, "B comp y", 5.000000)
    prg.add(3982060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(3982160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(3982260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(3982360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(3982460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(3982559, "IGBT 2 pinch+comp", 8.000000)
    prg.add(3982660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(3982760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(3982860, "IGBT 2 pinch+comp", 7.400000)
    prg.add(3982960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(3983060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(3983159, "IGBT 2 pinch+comp", 6.800000)
    prg.add(3983260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(3983360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(3983460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(3983560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(3983660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(3983759, "IGBT 2 pinch+comp", 5.600000)
    prg.add(3983860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(3983960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(3984060, "IGBT 2 pinch+comp", 5.000000)
    prg.add(3984160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(3984260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(3984360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(3984460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(3984560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(3984660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(3984760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(3984860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(3984960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(3985059, "IGBT 2 pinch+comp", 3.000000)
    prg.add(3985160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(3985260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(3985360, "IGBT 2 pinch+comp", 2.400000)
    prg.add(3985460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(3985560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(3985659, "IGBT 2 pinch+comp", 1.800000)
    prg.add(3985760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(3985860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(3985960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(3986060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(3986160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(3986259, "IGBT 2 pinch+comp", 0.600000)
    prg.add(3986360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(3986460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(3986560, "IGBT 2 pinch+comp", 0.000000)
    prg.add(3986660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(3986760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(3986860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(3986960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(3987060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(3987160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(3987260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(3987360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(3987460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(3987559, "IGBT 2 pinch+comp", -2.000000)
    prg.add(3987660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(3987760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(3987860, "IGBT 2 pinch+comp", -2.600000)
    prg.add(3987960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(3988060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(3988159, "IGBT 2 pinch+comp", -3.200000)
    prg.add(3988260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(3988360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(3988460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(3988560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(3988660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(3988759, "IGBT 2 pinch+comp", -4.400000)
    prg.add(3988860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(3988960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(3989060, "IGBT 2 pinch+comp", -5.000000)
    prg.add(3989160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(3989260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(3989360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(3989460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(3989560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(3989660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(3989760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(3989860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(3989960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(3990059, "IGBT 2 pinch+comp", -7.000000)
    prg.add(3990160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(3990260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(3990360, "IGBT 2 pinch+comp", -7.600000)
    prg.add(3990460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(3990560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(3990659, "IGBT 2 pinch+comp", -8.200000)
    prg.add(3990760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(3990860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(3990960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(3991060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(3991160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(3991259, "IGBT 2 pinch+comp", -9.400000)
    prg.add(3991360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(3991460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(3991560, "IGBT 2 pinch+comp", -10.000000)
    prg.add(3991600, "IGBT 4 Open")
    prg.add(3991620, "IGBT 5 Open")
    prg.add(3991850, "IGBT 1 pinch", -10.000000)
    prg.add(3991860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(3991870, "IGBT 3 Close")
    prg.add(3991880, "IGBT 4 Close")
    prg.add(3991890, "IGBT 5 Open")
    prg.add(3991900, "Delta 2 Voltage", 0.000000)
    prg.add(3991909, "Delta 1 Current", 15.400000)
    prg.add(3991950, "B comp x", 0.000000)
    prg.add(3992000, "B comp y", 5.000000)
    prg.add(3992530, "B comp y", 4.740000)
    prg.add(3993050, "B comp y", 4.470000)
    prg.add(3993580, "B comp y", 4.210000)
    prg.add(3994110, "B comp y", 3.950000)
    prg.add(3994630, "B comp y", 3.680000)
    prg.add(3995160, "B comp y", 3.420000)
    prg.add(3995680, "B comp y", 3.160000)
    prg.add(3996210, "B comp y", 2.890000)
    prg.add(3996740, "B comp y", 2.630000)
    prg.add(3997260, "B comp y", 2.370000)
    prg.add(3997790, "B comp y", 2.110000)
    prg.add(3998320, "B comp y", 1.840000)
    prg.add(3998840, "B comp y", 1.580000)
    prg.add(3999370, "B comp y", 1.320000)
    prg.add(3999889, "B comp y", 1.050000)
    prg.add(4000419, "B comp y", 0.790000)
    prg.add(4000950, "B comp y", 0.530000)
    prg.add(4001470, "B comp y", 0.260000)
    prg.add(4002000, "B comp y", 0.000000)
    prg.add(5463500, "B comp y", 1.000000)
    prg.add(5476500, "IGBT 1 pinch", -10.000000)
    prg.add(5476510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(5476520, "IGBT 3 Open")
    prg.add(5476530, "IGBT 4 Open")
    prg.add(5476540, "IGBT 5 Open")
    prg.add(5476550, "IGBT 6 Open")
    prg.add(5477100, "K probe Cooler (-) freq", 99.500000)
    prg.add(5477500, "K Cooler 2p (+) freq", 97.500000)
    prg.add(5477900, "K Repumper 1p (+) Amp", 1000.000000)
    prg.add(5478300, "K Repumper 1p (+) freq", 115.000000)
    prg.add(5478700, "K Repumper 2p (+) freq", 96.000000)
    prg.add(5480000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(5480500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(5480900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(5481300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5481700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5482000, "Trig Slow Stingray ON")
    prg.add(5482100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(5482500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(5482900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(5483550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(5483900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(5484500, "Trig Slow Stingray OFF")
    prg.add(5732500, "Shutter Probe Na Close")
    prg.add(5742500, "Shutter Probe K Close")
    prg.add(5981500, "Optical Levit ON")
    prg.add(6482000, "Trig Slow Stingray ON")
    prg.add(6482500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(6482900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(6483500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(6483900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(6484500, "Trig Slow Stingray OFF")
    prg.add(6492500, "Na Repumper MOT Amp", 1.000000)
    prg.add(6502500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(6512500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(7482000, "Trig Slow Stingray ON")
    prg.add(7484000, "Trig Slow Stingray OFF")
    prg.add(8482000, "Trig Slow Stingray ON")
    prg.add(8484000, "Trig Slow Stingray OFF")
    prg.add(8992500, "Optical Levit OFF")
    prg.add(9482500, "B comp y", 0.000000)
    return prg
