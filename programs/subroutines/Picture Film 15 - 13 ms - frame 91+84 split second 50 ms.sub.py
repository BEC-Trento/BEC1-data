prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(7089954, "Pulse uw ON")
    prg.add(7090000, "Pulse uw OFF")
    prg.add(7220000, "Trig ON Stingray 1")
    prg.add(7220019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7220500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7221500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(7221900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(7222000, "Trig OFF Stingray 1")
    prg.add(7929952, "Pulse uw ON")
    prg.add(7930000, "Pulse uw OFF")
    prg.add(8060000, "Trig ON Stingray 1")
    prg.add(8060019, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8060500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8061500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8061900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8062000, "Trig OFF Stingray 1")
    prg.add(8769950, "Pulse uw ON")
    prg.add(8770000, "Pulse uw OFF")
    prg.add(8900000, "Trig ON Stingray 1")
    prg.add(8900020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(8900500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(8901500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(8901900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(8902000, "Trig OFF Stingray 1")
    prg.add(9304500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(9314500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(9324500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(9344500, "Na Dark Spot Amp", 1.000000)
    prg.add(9354500, "Na Repumper MOT Amp", 1.000000)
    prg.add(9609948, "Pulse uw ON")
    prg.add(9610000, "Pulse uw OFF")
    prg.add(9704500, "Shutter Probe Na Open")
    prg.add(9740000, "Trig ON Stingray 1")
    prg.add(9740020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(9740500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(9741500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(9741900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(9742000, "Trig OFF Stingray 1")
    prg.add(10449945, "Pulse uw ON")
    prg.add(10450000, "Pulse uw OFF")
    prg.add(10580000, "Trig ON Stingray 1")
    prg.add(10580020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(10580500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(10581500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(10581900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(10582000, "Trig OFF Stingray 1")
    prg.add(10674500, "Shutter Probe K Open")
    prg.add(10684500, "Shutter RepumperMOT K Open")
    prg.add(10694500, "Shutter repump Na Open")
    prg.add(11214500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(11289943, "Pulse uw ON")
    prg.add(11290000, "Pulse uw OFF")
    prg.add(11420000, "Trig ON Stingray 1")
    prg.add(11420020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(11420500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(11421500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(11421900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(11422000, "Trig OFF Stingray 1")
    prg.add(11677500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(11687500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(11706500, "Optical Levit OFF")
    prg.add(11707500, "Shutter 3DMOT cool Na Open")
    prg.add(11718500, "Shutter Optical Levit Close")
    prg.add(12129940, "Pulse uw ON")
    prg.add(12130000, "Pulse uw OFF")
    prg.add(12260000, "Trig ON Stingray 1")
    prg.add(12260020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(12260500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(12261500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(12261900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(12262000, "Trig OFF Stingray 1")
    prg.add(13197000, "B comp y", 0.000000)
    prg.add(13197530, "B comp y", 0.260000)
    prg.add(13198050, "B comp y", 0.530000)
    prg.add(13198580, "B comp y", 0.790000)
    prg.add(13199110, "B comp y", 1.050000)
    prg.add(13199630, "B comp y", 1.320000)
    prg.add(13200160, "B comp y", 1.580000)
    prg.add(13200680, "B comp y", 1.840000)
    prg.add(13201210, "B comp y", 2.110000)
    prg.add(13201740, "B comp y", 2.370000)
    prg.add(13202260, "B comp y", 2.630000)
    prg.add(13202790, "B comp y", 2.890000)
    prg.add(13203320, "B comp y", 3.160000)
    prg.add(13203840, "B comp y", 3.420000)
    prg.add(13204369, "B comp y", 3.680000)
    prg.add(13204890, "B comp y", 3.950000)
    prg.add(13205420, "B comp y", 4.210000)
    prg.add(13205950, "B comp y", 4.470000)
    prg.add(13206470, "B comp y", 4.740000)
    prg.add(13206500, "IGBT 1 pinch", -10.000000)
    prg.add(13206520, "IGBT 3 Open")
    prg.add(13206560, "IGBT 2 pinch+comp", 10.000000)
    prg.add(13206660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(13206760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(13206860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(13206960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(13207000, "B comp y", 5.000000)
    prg.add(13207059, "IGBT 2 pinch+comp", 9.000000)
    prg.add(13207159, "IGBT 2 pinch+comp", 8.800000)
    prg.add(13207260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(13207360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(13207460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(13207560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(13207660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(13207760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(13207860, "IGBT 2 pinch+comp", 7.400000)
    prg.add(13207960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(13208060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(13208160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(13208260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(13208360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(13208460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(13208560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(13208660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(13208760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(13208860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(13208960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(13209060, "IGBT 2 pinch+comp", 5.000000)
    prg.add(13209160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(13209260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(13209360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(13209460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(13209559, "IGBT 2 pinch+comp", 4.000000)
    prg.add(13209659, "IGBT 2 pinch+comp", 3.800000)
    prg.add(13209760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(13209860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(13209960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(13210060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(13210160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(13210260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(13210360, "IGBT 2 pinch+comp", 2.400000)
    prg.add(13210460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(13210560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(13210660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(13210760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(13210860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(13210960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(13211060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(13211160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(13211260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(13211360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(13211460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(13211560, "IGBT 2 pinch+comp", 0.000000)
    prg.add(13211660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(13211760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(13211860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(13211960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(13212059, "IGBT 2 pinch+comp", -1.000000)
    prg.add(13212159, "IGBT 2 pinch+comp", -1.200000)
    prg.add(13212260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(13212360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(13212460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(13212560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(13212660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(13212760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(13212860, "IGBT 2 pinch+comp", -2.600000)
    prg.add(13212960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(13213060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(13213160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(13213260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(13213360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(13213460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(13213560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(13213660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(13213760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(13213860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(13213960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(13214060, "IGBT 2 pinch+comp", -5.000000)
    prg.add(13214160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(13214260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(13214360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(13214460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(13214559, "IGBT 2 pinch+comp", -6.000000)
    prg.add(13214659, "IGBT 2 pinch+comp", -6.200000)
    prg.add(13214760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(13214860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(13214960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(13215060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(13215160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(13215260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(13215360, "IGBT 2 pinch+comp", -7.600000)
    prg.add(13215460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(13215560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(13215660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(13215760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(13215860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(13215960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(13216060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(13216160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(13216260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(13216360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(13216460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(13216560, "IGBT 2 pinch+comp", -10.000000)
    prg.add(13216600, "IGBT 4 Open")
    prg.add(13216620, "IGBT 5 Open")
    prg.add(13216850, "IGBT 1 pinch", -10.000000)
    prg.add(13216860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(13216869, "IGBT 3 Close")
    prg.add(13216880, "IGBT 4 Close")
    prg.add(13216890, "IGBT 5 Open")
    prg.add(13216900, "Delta 2 Voltage", 0.000000)
    prg.add(13216910, "Delta 1 Current", 15.400000)
    prg.add(13216950, "B comp x", 0.000000)
    prg.add(13217000, "B comp y", 5.000000)
    prg.add(13217530, "B comp y", 4.740000)
    prg.add(13218050, "B comp y", 4.470000)
    prg.add(13218580, "B comp y", 4.210000)
    prg.add(13219110, "B comp y", 3.950000)
    prg.add(13219630, "B comp y", 3.680000)
    prg.add(13220160, "B comp y", 3.420000)
    prg.add(13220680, "B comp y", 3.160000)
    prg.add(13221210, "B comp y", 2.890000)
    prg.add(13221740, "B comp y", 2.630000)
    prg.add(13222260, "B comp y", 2.370000)
    prg.add(13222790, "B comp y", 2.110000)
    prg.add(13223320, "B comp y", 1.840000)
    prg.add(13223840, "B comp y", 1.580000)
    prg.add(13224369, "B comp y", 1.320000)
    prg.add(13224890, "B comp y", 1.050000)
    prg.add(13225420, "B comp y", 0.790000)
    prg.add(13225950, "B comp y", 0.530000)
    prg.add(13226470, "B comp y", 0.260000)
    prg.add(13227000, "B comp y", 0.000000)
    prg.add(13688500, "B comp y", 1.000000)
    prg.add(13701500, "IGBT 1 pinch", -10.000000)
    prg.add(13701510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(13701520, "IGBT 3 Open")
    prg.add(13701530, "IGBT 4 Open")
    prg.add(13701540, "IGBT 5 Open")
    prg.add(13701550, "IGBT 6 Open")
    prg.add(13701570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(13701900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(13705000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(13705500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(13705900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(13706300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(13706700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(13707000, "Trig Slow Stingray ON")
    prg.add(13707100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(13707500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(13707900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(13708550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(13708900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(13709500, "Trig Slow Stingray OFF")
    prg.add(13957500, "Shutter Probe Na Close")
    prg.add(13967500, "Shutter Probe K Close")
    prg.add(14206500, "Optical Levit ON")
    prg.add(14707000, "Trig Slow Stingray ON")
    prg.add(14707500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(14707900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(14708500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(14708900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(14709500, "Trig Slow Stingray OFF")
    prg.add(14717500, "Na Repumper MOT Amp", 1.000000)
    prg.add(14727500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(14737500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(15707000, "Trig Slow Stingray ON")
    prg.add(15709000, "Trig Slow Stingray OFF")
    prg.add(16707000, "Trig Slow Stingray ON")
    prg.add(16709000, "Trig Slow Stingray OFF")
    prg.add(17217500, "Optical Levit OFF")
    prg.add(17456500, "Shutter Optical Levit Close")
    prg.add(17707500, "B comp y", 0.000000)
    prg.add(22206500, "Optical Levit ON")
    return prg
