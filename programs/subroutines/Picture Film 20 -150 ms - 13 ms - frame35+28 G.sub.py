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
    prg.add(299964, "Pulse uw ON")
    prg.add(300000, "Pulse uw OFF")
    prg.add(430000, "Trig ON Stingray 1")
    prg.add(430020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(430500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(431500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(431900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(432000, "Trig OFF Stingray 1")
    prg.add(649964, "Pulse uw ON")
    prg.add(650000, "Pulse uw OFF")
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
    prg.add(3169951, "Pulse uw ON")
    prg.add(3170000, "Pulse uw OFF")
    prg.add(3300000, "Trig ON Stingray 1")
    prg.add(3300020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3300500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3301500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3301900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3302000, "Trig OFF Stingray 1")
    prg.add(3449950, "Pulse uw ON")
    prg.add(3450000, "Pulse uw OFF")
    prg.add(3580000, "Trig ON Stingray 1")
    prg.add(3580020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3580500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3581500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3581900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3582000, "Trig OFF Stingray 1")
    prg.add(3729948, "Pulse uw ON")
    prg.add(3730000, "Pulse uw OFF")
    prg.add(3754500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(3764500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(3774500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(3794500, "Na Dark Spot Amp", 1.000000)
    prg.add(3804500, "Na Repumper MOT Amp", 1.000000)
    prg.add(3860000, "Trig ON Stingray 1")
    prg.add(3860020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3860500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3861500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3861900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3862000, "Trig OFF Stingray 1")
    prg.add(4009948, "Pulse uw ON")
    prg.add(4010000, "Pulse uw OFF")
    prg.add(4140000, "Trig ON Stingray 1")
    prg.add(4140020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4140500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4141500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4141900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4142000, "Trig OFF Stingray 1")
    prg.add(4154500, "Shutter Probe Na Open")
    prg.add(4289947, "Pulse uw ON")
    prg.add(4290000, "Pulse uw OFF")
    prg.add(4420000, "Trig ON Stingray 1")
    prg.add(4420020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4420500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4421500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4421900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4422000, "Trig OFF Stingray 1")
    prg.add(4569944, "Pulse uw ON")
    prg.add(4570000, "Pulse uw OFF")
    prg.add(4700000, "Trig ON Stingray 1")
    prg.add(4700020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4700500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4701500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4701900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4702000, "Trig OFF Stingray 1")
    prg.add(4849942, "Pulse uw ON")
    prg.add(4850000, "Pulse uw OFF")
    prg.add(4980000, "Trig ON Stingray 1")
    prg.add(4980020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4980500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4981500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4981900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4982000, "Trig OFF Stingray 1")
    prg.add(5124500, "Shutter Probe K Open")
    prg.add(5129940, "Pulse uw ON")
    prg.add(5130000, "Pulse uw OFF")
    prg.add(5134500, "Shutter RepumperMOT K Open")
    prg.add(5144500, "Shutter repump Na Open")
    prg.add(5260000, "Trig ON Stingray 1")
    prg.add(5260019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5260500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5261500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5261900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5262000, "Trig OFF Stingray 1")
    prg.add(5409937, "Pulse uw ON")
    prg.add(5410000, "Pulse uw OFF")
    prg.add(5540000, "Trig ON Stingray 1")
    prg.add(5540019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5540500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5541500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5541900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5542000, "Trig OFF Stingray 1")
    prg.add(5664500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(5689933, "Pulse uw ON")
    prg.add(5690000, "Pulse uw OFF")
    prg.add(5820000, "Trig ON Stingray 1")
    prg.add(5820019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(5820500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(5821500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(5821900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(5822000, "Trig OFF Stingray 1")
    prg.add(6127500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(6137500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(6156500, "Optical Levit OFF")
    prg.add(6157500, "Shutter 3DMOT cool Na Open")
    prg.add(6168500, "Shutter Optical Levit Close")
    prg.add(6647000, "B comp y", 0.000000)
    prg.add(6647530, "B comp y", 0.260000)
    prg.add(6648049, "B comp y", 0.530000)
    prg.add(6648579, "B comp y", 0.790000)
    prg.add(6649109, "B comp y", 1.050000)
    prg.add(6649630, "B comp y", 1.320000)
    prg.add(6650160, "B comp y", 1.580000)
    prg.add(6650680, "B comp y", 1.840000)
    prg.add(6651210, "B comp y", 2.110000)
    prg.add(6651740, "B comp y", 2.370000)
    prg.add(6652260, "B comp y", 2.630000)
    prg.add(6652790, "B comp y", 2.890000)
    prg.add(6653320, "B comp y", 3.160000)
    prg.add(6653840, "B comp y", 3.420000)
    prg.add(6654370, "B comp y", 3.680000)
    prg.add(6654890, "B comp y", 3.950000)
    prg.add(6655420, "B comp y", 4.210000)
    prg.add(6655950, "B comp y", 4.470000)
    prg.add(6656470, "B comp y", 4.740000)
    prg.add(6656500, "IGBT 1 pinch", -10.000000)
    prg.add(6656520, "IGBT 3 Open")
    prg.add(6656559, "IGBT 2 pinch+comp", 10.000000)
    prg.add(6656660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(6656760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(6656860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(6656960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(6657000, "B comp y", 5.000000)
    prg.add(6657060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(6657160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(6657260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(6657360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(6657460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(6657560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(6657660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(6657760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(6657859, "IGBT 2 pinch+comp", 7.400000)
    prg.add(6657960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(6658060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(6658160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(6658260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(6658360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(6658460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(6658560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(6658660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(6658760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(6658860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(6658960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(6659059, "IGBT 2 pinch+comp", 5.000000)
    prg.add(6659160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(6659260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(6659360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(6659460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(6659560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(6659660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(6659760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(6659860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(6659960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(6660060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(6660160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(6660260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(6660359, "IGBT 2 pinch+comp", 2.400000)
    prg.add(6660460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(6660560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(6660660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(6660760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(6660860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(6660960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(6661060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(6661160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(6661260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(6661360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(6661460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(6661559, "IGBT 2 pinch+comp", 0.000000)
    prg.add(6661660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(6661760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(6661860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(6661960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(6662060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(6662160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(6662260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(6662360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(6662460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(6662560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(6662660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(6662760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(6662859, "IGBT 2 pinch+comp", -2.600000)
    prg.add(6662960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(6663060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(6663160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(6663260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(6663360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(6663460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(6663560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(6663660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(6663760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(6663860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(6663960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(6664059, "IGBT 2 pinch+comp", -5.000000)
    prg.add(6664160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(6664260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(6664360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(6664460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(6664560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(6664660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(6664760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(6664860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(6664960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(6665060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(6665160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(6665260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(6665359, "IGBT 2 pinch+comp", -7.600000)
    prg.add(6665460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(6665560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(6665660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(6665760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(6665860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(6665960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(6666060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(6666160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(6666260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(6666360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(6666460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(6666559, "IGBT 2 pinch+comp", -10.000000)
    prg.add(6666600, "IGBT 4 Open")
    prg.add(6666620, "IGBT 5 Open")
    prg.add(6666849, "IGBT 1 pinch", -10.000000)
    prg.add(6666860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(6666870, "IGBT 3 Close")
    prg.add(6666880, "IGBT 4 Close")
    prg.add(6666890, "IGBT 5 Open")
    prg.add(6666900, "Delta 2 Voltage", 0.000000)
    prg.add(6666910, "Delta 1 Current", 15.300000)
    prg.add(6666950, "B comp x", 0.000000)
    prg.add(6667000, "B comp y", 5.000000)
    prg.add(6667530, "B comp y", 4.740000)
    prg.add(6668049, "B comp y", 4.470000)
    prg.add(6668579, "B comp y", 4.210000)
    prg.add(6669109, "B comp y", 3.950000)
    prg.add(6669630, "B comp y", 3.680000)
    prg.add(6670160, "B comp y", 3.420000)
    prg.add(6670680, "B comp y", 3.160000)
    prg.add(6671210, "B comp y", 2.890000)
    prg.add(6671740, "B comp y", 2.630000)
    prg.add(6672260, "B comp y", 2.370000)
    prg.add(6672790, "B comp y", 2.110000)
    prg.add(6673320, "B comp y", 1.840000)
    prg.add(6673840, "B comp y", 1.580000)
    prg.add(6674370, "B comp y", 1.320000)
    prg.add(6674890, "B comp y", 1.050000)
    prg.add(6675420, "B comp y", 0.790000)
    prg.add(6675950, "B comp y", 0.530000)
    prg.add(6676470, "B comp y", 0.260000)
    prg.add(6677000, "B comp y", 0.000000)
    prg.add(8138500, "B comp y", 1.000000)
    prg.add(8151500, "IGBT 1 pinch", -10.000000)
    prg.add(8151510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(8151520, "IGBT 3 Open")
    prg.add(8151530, "IGBT 4 Open")
    prg.add(8151540, "IGBT 5 Open")
    prg.add(8151550, "IGBT 6 Open")
    prg.add(8151570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(8151900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(8155000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(8155500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(8155900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(8156300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8156700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8157000, "Trig Slow Stingray ON")
    prg.add(8157100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(8157500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(8157900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(8158550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(8158900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(8159500, "Trig Slow Stingray OFF")
    prg.add(8407500, "Shutter Probe Na Close")
    prg.add(8417500, "Shutter Probe K Close")
    prg.add(9157000, "Trig Slow Stingray ON")
    prg.add(9157500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(9157900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(9158500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(9158900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(9159500, "Trig Slow Stingray OFF")
    prg.add(9167500, "Na Repumper MOT Amp", 1.000000)
    prg.add(9177500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(9187500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(10157000, "Trig Slow Stingray ON")
    prg.add(10159000, "Trig Slow Stingray OFF")
    prg.add(11157000, "Trig Slow Stingray ON")
    prg.add(11159000, "Trig Slow Stingray OFF")
    prg.add(11667500, "Optical Levit OFF")
    prg.add(11906500, "Shutter Optical Levit Close")
    prg.add(12157500, "B comp y", 0.000000)
    prg.add(16656500, "Optical Levit ON")
    return prg
