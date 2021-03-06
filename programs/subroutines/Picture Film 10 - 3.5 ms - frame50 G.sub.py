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
    prg.add(799960, "Pulse uw ON")
    prg.add(800000, "Pulse uw OFF")
    prg.add(835000, "Trig ON Stingray 1")
    prg.add(835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(837000, "Trig OFF Stingray 1")
    prg.add(1299960, "Pulse uw ON")
    prg.add(1300000, "Pulse uw OFF")
    prg.add(1335000, "Trig ON Stingray 1")
    prg.add(1335020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1335500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1336500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1336900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1337000, "Trig OFF Stingray 1")
    prg.add(1799960, "Pulse uw ON")
    prg.add(1800000, "Pulse uw OFF")
    prg.add(1835000, "Trig ON Stingray 1")
    prg.add(1835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(1835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1837000, "Trig OFF Stingray 1")
    prg.add(2299960, "Pulse uw ON")
    prg.add(2300000, "Pulse uw OFF")
    prg.add(2335000, "Trig ON Stingray 1")
    prg.add(2335020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2335500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2336500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2336900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2337000, "Trig OFF Stingray 1")
    prg.add(2799960, "Pulse uw ON")
    prg.add(2800000, "Pulse uw OFF")
    prg.add(2835000, "Trig ON Stingray 1")
    prg.add(2835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(2835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(2836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(2836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2837000, "Trig OFF Stingray 1")
    prg.add(2879500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(2889500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(2899500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(2919500, "Na Dark Spot Amp", 1.000000)
    prg.add(2929500, "Na Repumper MOT Amp", 1.000000)
    prg.add(3279500, "Shutter Probe Na Open")
    prg.add(3299960, "Pulse uw ON")
    prg.add(3300000, "Pulse uw OFF")
    prg.add(3335000, "Trig ON Stingray 1")
    prg.add(3335020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3335500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3336500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3336900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3337000, "Trig OFF Stingray 1")
    prg.add(3799960, "Pulse uw ON")
    prg.add(3800000, "Pulse uw OFF")
    prg.add(3835000, "Trig ON Stingray 1")
    prg.add(3835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(3835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(3836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(3836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(3837000, "Trig OFF Stingray 1")
    prg.add(4249500, "Shutter Probe K Open")
    prg.add(4259500, "Shutter RepumperMOT K Open")
    prg.add(4269500, "Shutter repump Na Open")
    prg.add(4299960, "Pulse uw ON")
    prg.add(4300000, "Pulse uw OFF")
    prg.add(4335000, "Trig ON Stingray 1")
    prg.add(4335020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4335500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4336500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4336900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4337000, "Trig OFF Stingray 1")
    prg.add(4789500, "K probe Cooler (-) Amp", 1.000000)
    prg.add(4799960, "Pulse uw ON")
    prg.add(4800000, "Pulse uw OFF")
    prg.add(4835000, "Trig ON Stingray 1")
    prg.add(4835020, "Na Probe/Push (-) freq", 110.000000)
    prg.add(4835500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(4836500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(4836900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(4837000, "Trig OFF Stingray 1")
    prg.add(5252500, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(5262500, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(5281500, "Optical Levit OFF")
    prg.add(5282500, "Shutter 3DMOT cool Na Open")
    prg.add(5293500, "Shutter Optical Levit Close")
    prg.add(5772000, "B comp y", 0.000000)
    prg.add(5772530, "B comp y", 0.260000)
    prg.add(5773049, "B comp y", 0.530000)
    prg.add(5773579, "B comp y", 0.790000)
    prg.add(5774109, "B comp y", 1.050000)
    prg.add(5774630, "B comp y", 1.320000)
    prg.add(5775160, "B comp y", 1.580000)
    prg.add(5775680, "B comp y", 1.840000)
    prg.add(5776210, "B comp y", 2.110000)
    prg.add(5776740, "B comp y", 2.370000)
    prg.add(5777260, "B comp y", 2.630000)
    prg.add(5777790, "B comp y", 2.890000)
    prg.add(5778320, "B comp y", 3.160000)
    prg.add(5778840, "B comp y", 3.420000)
    prg.add(5779370, "B comp y", 3.680000)
    prg.add(5779890, "B comp y", 3.950000)
    prg.add(5780420, "B comp y", 4.210000)
    prg.add(5780950, "B comp y", 4.470000)
    prg.add(5781470, "B comp y", 4.740000)
    prg.add(5781500, "IGBT 1 pinch", -10.000000)
    prg.add(5781520, "IGBT 3 Open")
    prg.add(5781559, "IGBT 2 pinch+comp", 10.000000)
    prg.add(5781660, "IGBT 2 pinch+comp", 9.800000)
    prg.add(5781760, "IGBT 2 pinch+comp", 9.600000)
    prg.add(5781860, "IGBT 2 pinch+comp", 9.400000)
    prg.add(5781960, "IGBT 2 pinch+comp", 9.200000)
    prg.add(5782000, "B comp y", 5.000000)
    prg.add(5782060, "IGBT 2 pinch+comp", 9.000000)
    prg.add(5782160, "IGBT 2 pinch+comp", 8.800000)
    prg.add(5782260, "IGBT 2 pinch+comp", 8.600000)
    prg.add(5782360, "IGBT 2 pinch+comp", 8.400000)
    prg.add(5782460, "IGBT 2 pinch+comp", 8.200000)
    prg.add(5782560, "IGBT 2 pinch+comp", 8.000000)
    prg.add(5782660, "IGBT 2 pinch+comp", 7.800000)
    prg.add(5782760, "IGBT 2 pinch+comp", 7.600000)
    prg.add(5782859, "IGBT 2 pinch+comp", 7.400000)
    prg.add(5782960, "IGBT 2 pinch+comp", 7.200000)
    prg.add(5783060, "IGBT 2 pinch+comp", 7.000000)
    prg.add(5783160, "IGBT 2 pinch+comp", 6.800000)
    prg.add(5783260, "IGBT 2 pinch+comp", 6.600000)
    prg.add(5783360, "IGBT 2 pinch+comp", 6.400000)
    prg.add(5783460, "IGBT 2 pinch+comp", 6.200000)
    prg.add(5783560, "IGBT 2 pinch+comp", 6.000000)
    prg.add(5783660, "IGBT 2 pinch+comp", 5.800000)
    prg.add(5783760, "IGBT 2 pinch+comp", 5.600000)
    prg.add(5783860, "IGBT 2 pinch+comp", 5.400000)
    prg.add(5783960, "IGBT 2 pinch+comp", 5.200000)
    prg.add(5784059, "IGBT 2 pinch+comp", 5.000000)
    prg.add(5784160, "IGBT 2 pinch+comp", 4.800000)
    prg.add(5784260, "IGBT 2 pinch+comp", 4.600000)
    prg.add(5784360, "IGBT 2 pinch+comp", 4.400000)
    prg.add(5784460, "IGBT 2 pinch+comp", 4.200000)
    prg.add(5784560, "IGBT 2 pinch+comp", 4.000000)
    prg.add(5784660, "IGBT 2 pinch+comp", 3.800000)
    prg.add(5784760, "IGBT 2 pinch+comp", 3.600000)
    prg.add(5784860, "IGBT 2 pinch+comp", 3.400000)
    prg.add(5784960, "IGBT 2 pinch+comp", 3.200000)
    prg.add(5785060, "IGBT 2 pinch+comp", 3.000000)
    prg.add(5785160, "IGBT 2 pinch+comp", 2.800000)
    prg.add(5785260, "IGBT 2 pinch+comp", 2.600000)
    prg.add(5785359, "IGBT 2 pinch+comp", 2.400000)
    prg.add(5785460, "IGBT 2 pinch+comp", 2.200000)
    prg.add(5785560, "IGBT 2 pinch+comp", 2.000000)
    prg.add(5785660, "IGBT 2 pinch+comp", 1.800000)
    prg.add(5785760, "IGBT 2 pinch+comp", 1.600000)
    prg.add(5785860, "IGBT 2 pinch+comp", 1.400000)
    prg.add(5785960, "IGBT 2 pinch+comp", 1.200000)
    prg.add(5786060, "IGBT 2 pinch+comp", 1.000000)
    prg.add(5786160, "IGBT 2 pinch+comp", 0.800000)
    prg.add(5786260, "IGBT 2 pinch+comp", 0.600000)
    prg.add(5786360, "IGBT 2 pinch+comp", 0.400000)
    prg.add(5786460, "IGBT 2 pinch+comp", 0.200000)
    prg.add(5786559, "IGBT 2 pinch+comp", 0.000000)
    prg.add(5786660, "IGBT 2 pinch+comp", -0.200000)
    prg.add(5786760, "IGBT 2 pinch+comp", -0.400000)
    prg.add(5786860, "IGBT 2 pinch+comp", -0.600000)
    prg.add(5786960, "IGBT 2 pinch+comp", -0.800000)
    prg.add(5787060, "IGBT 2 pinch+comp", -1.000000)
    prg.add(5787160, "IGBT 2 pinch+comp", -1.200000)
    prg.add(5787260, "IGBT 2 pinch+comp", -1.400000)
    prg.add(5787360, "IGBT 2 pinch+comp", -1.600000)
    prg.add(5787460, "IGBT 2 pinch+comp", -1.800000)
    prg.add(5787560, "IGBT 2 pinch+comp", -2.000000)
    prg.add(5787660, "IGBT 2 pinch+comp", -2.200000)
    prg.add(5787760, "IGBT 2 pinch+comp", -2.400000)
    prg.add(5787859, "IGBT 2 pinch+comp", -2.600000)
    prg.add(5787960, "IGBT 2 pinch+comp", -2.800000)
    prg.add(5788060, "IGBT 2 pinch+comp", -3.000000)
    prg.add(5788160, "IGBT 2 pinch+comp", -3.200000)
    prg.add(5788260, "IGBT 2 pinch+comp", -3.400000)
    prg.add(5788360, "IGBT 2 pinch+comp", -3.600000)
    prg.add(5788460, "IGBT 2 pinch+comp", -3.800000)
    prg.add(5788560, "IGBT 2 pinch+comp", -4.000000)
    prg.add(5788660, "IGBT 2 pinch+comp", -4.200000)
    prg.add(5788760, "IGBT 2 pinch+comp", -4.400000)
    prg.add(5788860, "IGBT 2 pinch+comp", -4.600000)
    prg.add(5788960, "IGBT 2 pinch+comp", -4.800000)
    prg.add(5789059, "IGBT 2 pinch+comp", -5.000000)
    prg.add(5789160, "IGBT 2 pinch+comp", -5.200000)
    prg.add(5789260, "IGBT 2 pinch+comp", -5.400000)
    prg.add(5789360, "IGBT 2 pinch+comp", -5.600000)
    prg.add(5789460, "IGBT 2 pinch+comp", -5.800000)
    prg.add(5789560, "IGBT 2 pinch+comp", -6.000000)
    prg.add(5789660, "IGBT 2 pinch+comp", -6.200000)
    prg.add(5789760, "IGBT 2 pinch+comp", -6.400000)
    prg.add(5789860, "IGBT 2 pinch+comp", -6.600000)
    prg.add(5789960, "IGBT 2 pinch+comp", -6.800000)
    prg.add(5790060, "IGBT 2 pinch+comp", -7.000000)
    prg.add(5790160, "IGBT 2 pinch+comp", -7.200000)
    prg.add(5790260, "IGBT 2 pinch+comp", -7.400000)
    prg.add(5790359, "IGBT 2 pinch+comp", -7.600000)
    prg.add(5790460, "IGBT 2 pinch+comp", -7.800000)
    prg.add(5790560, "IGBT 2 pinch+comp", -8.000000)
    prg.add(5790660, "IGBT 2 pinch+comp", -8.200000)
    prg.add(5790760, "IGBT 2 pinch+comp", -8.400000)
    prg.add(5790860, "IGBT 2 pinch+comp", -8.600000)
    prg.add(5790960, "IGBT 2 pinch+comp", -8.800000)
    prg.add(5791060, "IGBT 2 pinch+comp", -9.000000)
    prg.add(5791160, "IGBT 2 pinch+comp", -9.200000)
    prg.add(5791260, "IGBT 2 pinch+comp", -9.400000)
    prg.add(5791360, "IGBT 2 pinch+comp", -9.600000)
    prg.add(5791460, "IGBT 2 pinch+comp", -9.800000)
    prg.add(5791559, "IGBT 2 pinch+comp", -10.000000)
    prg.add(5791600, "IGBT 4 Open")
    prg.add(5791620, "IGBT 5 Open")
    prg.add(5791849, "IGBT 1 pinch", -10.000000)
    prg.add(5791860, "IGBT 2 pinch+comp", -10.000000)
    prg.add(5791870, "IGBT 3 Close")
    prg.add(5791880, "IGBT 4 Close")
    prg.add(5791890, "IGBT 5 Open")
    prg.add(5791900, "Delta 2 Voltage", 0.000000)
    prg.add(5791910, "Delta 1 Current", 15.400000)
    prg.add(5791950, "B comp x", 0.000000)
    prg.add(5792000, "B comp y", 5.000000)
    prg.add(5792530, "B comp y", 4.740000)
    prg.add(5793049, "B comp y", 4.470000)
    prg.add(5793579, "B comp y", 4.210000)
    prg.add(5794109, "B comp y", 3.950000)
    prg.add(5794630, "B comp y", 3.680000)
    prg.add(5795160, "B comp y", 3.420000)
    prg.add(5795680, "B comp y", 3.160000)
    prg.add(5796210, "B comp y", 2.890000)
    prg.add(5796740, "B comp y", 2.630000)
    prg.add(5797260, "B comp y", 2.370000)
    prg.add(5797790, "B comp y", 2.110000)
    prg.add(5798320, "B comp y", 1.840000)
    prg.add(5798840, "B comp y", 1.580000)
    prg.add(5799370, "B comp y", 1.320000)
    prg.add(5799890, "B comp y", 1.050000)
    prg.add(5800420, "B comp y", 0.790000)
    prg.add(5800950, "B comp y", 0.530000)
    prg.add(5801470, "B comp y", 0.260000)
    prg.add(5802000, "B comp y", 0.000000)
    prg.add(7263500, "B comp y", 1.000000)
    prg.add(7276500, "IGBT 1 pinch", -10.000000)
    prg.add(7276510, "IGBT 2 pinch+comp", -10.000000)
    prg.add(7276520, "IGBT 3 Open")
    prg.add(7276530, "IGBT 4 Open")
    prg.add(7276540, "IGBT 5 Open")
    prg.add(7276550, "IGBT 6 Open")
    prg.add(7276570, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(7276900, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(7280000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(7280500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(7280900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(7281300, "Na Probe/Push (+) freq", 110.000000)
    prg.add(7281700, "Na Probe/Push (-) freq", 110.000000)
    prg.add(7282000, "Trig Slow Stingray ON")
    prg.add(7282100, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(7282500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(7282900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(7283550, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(7283900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(7284500, "Trig Slow Stingray OFF")
    prg.add(7532500, "Shutter Probe Na Close")
    prg.add(7542500, "Shutter Probe K Close")
    prg.add(7781500, "Optical Levit ON")
    prg.add(8282000, "Trig Slow Stingray ON")
    prg.add(8282500, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(8282900, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(8283500, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(8283900, "K probe Cooler (-) Amp", 1.000000)
    prg.add(8284500, "Trig Slow Stingray OFF")
    prg.add(8292500, "Na Repumper MOT Amp", 1.000000)
    prg.add(8302500, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(8312500, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(9282000, "Trig Slow Stingray ON")
    prg.add(9284000, "Trig Slow Stingray OFF")
    prg.add(10282000, "Trig Slow Stingray ON")
    prg.add(10284000, "Trig Slow Stingray OFF")
    prg.add(10792500, "Optical Levit OFF")
    prg.add(11000000, "Shutter Optical Levit Close")
    prg.add(11282500, "B comp y", 0.000000)
    prg.add(15000000, "Optical Levit ON")
    return prg
