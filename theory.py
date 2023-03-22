from music21 import harmony, interval, pitch, scale

chord_by_interval_dict = {
'':['M3','P5'],
'm':['m3','P5'],
'5':['P5'],
'+':['M3','A5'],
'dim':['m3','d5'],
'sus4':['P4','P5'],
'sus2':['M2','P5'],

'6':['M3','P5','M6'],
'6/9':['M3','P5','M6','M9'],
'm6':['m3','P5','M6'],
'mb6':['m3','P5','m6'],
'm6/9':['m3','P5','M6','M9'],

'm7':['m3','P5','m7'],
'dim7':['m3','d5','d7'],
'dim7':['m3','d5','M6'],
'm7b5':['m3','d5','m7'],
'm(maj7)':['m3','P5','M7'],

'7':['M3','P5','m7'],
'maj7':['M3','P5','M7'],
'maj7#11':['M3','P5','M7','A11'],

'7b5':['M3','d5','m7'],
'7b9':['M3','P5','m7','m9'],
'7#9':['M3','P5','m7','A9'],
'7b5#9':['M3','d5','m7','A9'],
'7#11':['M3','P5','m7','A11'],

'7#5':['M3','A5','m7'],
'+7':['M3','A5','m7'],
'aug7':['M3','A5','m7'],
'7b9#5':['M3','A5','m7','m9'],
'7#9#5':['M3','A5','m7','A9'],
'+7b9':['M3','A5','m7','m9'],
'+7#9':['M3','A5','m7','A9'],
'7sus4':['P4','P5','m7'],

'add9':['M3','P5','M9'],
'+9':['M3','A5','m7','M9'],
'maj9':['M3','P5','M7','M9'],
'm9':['m3','P5','m7','M9'],
'9':['M3','P5','m7','M9'],
'm9b5':['m3','d5','m7','M9'],
'm9(maj7)':['m3','P5','M7','M9'],
'9#5':['M3','A5','m7','M9'],
'9b5':['M3','d5','m7','M9'],
'9sus4':['P4','P5','m7','M9'],

'maj11':['M3','P5','M7','M9','P11'],
'm11':['m3','P5','m7','M9','P11'],
'11':['M3','P5','m7','M9','P11'],
'#11':['M3','P5','m7','M9','A11'],

'maj13':['M3','P5','M7','M9','m13'],
'm13':['m3','P5','m7','M9','P11','M13'],
'13':['M3','P5','m7','M9','M13'],
'13sus4':['P4','P5','m7','M9','M13']
}

chord_by_name_dict = {
'':'major',
'm':'minor',
'5':'power cord',
'+':'augmented',
'dim':'diminished',
'sus4':'suspended 4th',
'sus2':'suspended 2nd',

'6':'major add 6th',
'6/9':'major add 6th & 9th',
'm6':'minor add 6th',
'mb6':'minor add flat 6th',
'm6/9':'minor add 6th & 9th',

'm7':'minor 7th',
'dim7':'diminished 7th',
'm7b5':'minor 7th flat five',
'm(maj7)':'minor major 7th',

'7':'dominant 7th',
'maj7':'major 7th',
'maj7#11':'major 7th sharp eleven',

'7b5':'seventh flat five',
'7b9':'seventh flat nine',
'7#9':'seventh sharp nine',
'7b5#9':'dominant 7th, flat 5th, sharp 9th',
'7#11':'dominant 7th, sharp 11th',

'7#5':'dominant augmented 7th',
'+7':'dominant 7th, sharp 5th',
'aug7':'augmented 7th',
'7b9#5':'augmented 7th flat nine',
'7#9#5':'augmented 7th sharp nine',
'+7b9':'dominant 7th, sharp 5th, flat 9th',
'+7#9':'dominant 7th, sharp 5th, sharp 9th',
'7sus4':'seventh suspended 4th',

'add9':'major add 9th',
'+9':'9th, sharp 5th',
'maj9':'major 9th',
'm9':'minor 9th',
'9':'dominant 9th',
'm9b5':'minor 9th, flat 5th',
'm9(maj7)':'minor 9th (major 7)',
'9#5':'dominant 9th sharp 5th',
'9b5':'dominant 9th flat 5th',
'9sus4':'9th suspended 4th',

'maj11':'major 11th',
'm11':'minor 11th',
'11':'11th',
'#11':'sharp 11th',

'maj13':'major 13th',
'm13':'minor 13th',
'13':'13th',
'13sus4':'13th suspended 4th'
}

chord_by_degree_dict = {
'': "1, 3, 5",
'm': "1, -3, 5",
'5': "1, 5",
'+': "1, 3, #5",
'dim': "1, -3, -5",
'sus4': "1, 4, 5",
'sus2': "1, 2, 5",

'6': "1, 3, 5, 6",
'6/9': "1, 3, 5, 6, 9",
'm6': "1, -3, 5, 6",
'mb6': "1, -3, 5, -6",
'm6/9': "1, -3, 5, 6, 9",

'm7': "1, -3, 5, -7",
'dim7': "1, -3, -5, --7",
'dim7': "1, -3, -5, 6",
'm7b5': "1, -3, -5, -7",
'm(maj7)': "1, -3, 5, 7",

'7': "1, 3, 5, -7",
'maj7': "1, 3, 5, 7",
'maj7#11': "1, 3, 5, 7, #11",

'7b5': "1, 3, -5, -7",
'7b9': "1, 3, 5, -7, -9",
'7#9': "1, 3, 5, -7, #9",
'7b5#9': "1, 3, -5, -7, #9",
'7#11': "1, 3, 5, -7, #11",

'7#5': "1, 3, #5, -7",
'+7': "1, 3, #5, -7",
'aug7': "1, 3, #5, 7",
'7b9#5': "1, 3, #5, -7, -9",
'7#9#5': "1, 3, #5, -7, #9",
'+7b9': "1, 3, #5, -7, -9",
'+7#9': "1, 3, #5, -7, #9",
'7sus4': "1, 4, 5, -7",

'add9': "1, 3, 5, 9",
'+9': "1, 3, #5, 9",
'maj9': "1, 3, 5, 7, 9",
'm9': "1, -3, 5, -7, 9",
'9': "1, 3, 5, -7, 9",
'm9b5': "1, -3, -5, -7, 9",
'm9(maj7)': "1, -3, 5, 7, 9",
'9#5': "1, 3, #5, -7, 9",
'9b5': "1, 3, -5, -7, 9",
'9sus4': "1, 4, 5, -7, 9",

'maj11': "1, 3, 5, 7, 9, 11",
'm11': "1, -3, 5, -7, 9, 11",
'11': "1, 3, 5, -7, 9, 11",
'#11': "1, 3, 5, -7, 9, #11",

'maj13': "1, 3, 5, 7, 9, 13",
'm13': "1, -3, 5, -7, 9, 11, 13",
'13': "1, 3, 5, -7, 9, 13",
'13sus4': "1, 4, 5, -7, 9, 13"
}

chord_interval_list = list(chord_by_interval_dict.keys())

chord_types = harmony.CHORD_TYPES
for c in list(harmony.CHORD_TYPES):
    harmony.removeChordSymbols(c)

for dict_key in chord_interval_list:
    harmony.addNewChordSymbol(chord_by_name_dict[dict_key].title(), chord_by_degree_dict[dict_key], [dict_key])

harmony.addNewChordSymbol("Major 13th Sharp 11th", "1,3,5,7,9,#11,13", ["maj13#11"])
harmony.addNewChordSymbol("Major Sharp 11th", "1,3,5,7,9,#11", ["maj9#11"])
harmony.addNewChordSymbol("Dominant 9th Sharp 11th", "1,3,5,-7,9,#11", ["9#11"])
harmony.addNewChordSymbol("Minor Add Ninth", "1,-3,5,9", ["m(add9)"])
harmony.addNewChordSymbol("Major 11th Suspended 4th", "1,4,5,7,9,11", ["maj11sus4"])
harmony.addNewChordSymbol("9th Suspended 4th", "1,4,5,-7,9", ["9sus4"])
harmony.addNewChordSymbol("Dominant 13th Flat 9th", "1,3,5,-7,-9,13", ["13b9"])
harmony.addNewChordSymbol("Dominant 13th Sharp 9th", "1,3,5,-7,#9,13", ["13#9"])
harmony.addNewChordSymbol("Dominant 13th Sharp 11th", "1,3,5,-7,9,#11,13", ["13#11"])
harmony.addNewChordSymbol('Major 7th Sharp 11th', "1,3,5,7,#11", ["maj7#11"])
harmony.addNewChordSymbol('Major 7th Flat 5th', "1,3,-5,7", ["maj7b5"])
harmony.addNewChordSymbol('Major 7th Flat 5th', "1,3,-5,7", ["maj7b5"])

for c in chord_types:
    if c not in ["Neapolitan", "Italian", "French", "German", "pedal", "power", "Tristan"]:
        harmony.addNewChordSymbol(c, chord_types[c][0], chord_types[c][1])

### you need to make sure that every chord symbol is properly labeled so if it returns as "other", we know it's wrong

### Church Modes ###
ionian_scale = scale.AbstractDiatonicScale("major")
ionian_scale.type = "1st Mode of Ionian"

dorian_scale = scale.AbstractDiatonicScale("dorian")
dorian_scale.type = "2nd Mode of Ionian"

phrygian_scale = scale.AbstractDiatonicScale("phrygian")
phrygian_scale.type = "3rd Mode of Ionian"

lydian_scale = scale.AbstractDiatonicScale("lydian")
lydian_scale.type = "4th Mode of Ionian"

mixolydian_scale = scale.AbstractDiatonicScale("mixolydian")
mixolydian_scale.type = "5th Mode of Ionian"

aeolian_scale = scale.AbstractDiatonicScale("aeolian")
aeolian_scale.type = "6th Mode of Ionian"

locrian_scale = scale.AbstractDiatonicScale("locrian")
locrian_scale.type = "7th Mode of Ionian"

### Harmonic Minor Modes ###
harmonic_minor_scale = scale.AbstractDiatonicScale("aeolian")
harmonic_minor_scale._alteredDegrees = {7: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
harmonic_minor_scale.mode = "Harmonic Minor"
harmonic_minor_scale.type = "1st Mode of Harmonic Minor"

locrian_nat6_scale = scale.AbstractDiatonicScale("locrian")
locrian_nat6_scale._alteredDegrees = {6: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
locrian_nat6_scale.mode = "Locrian Flat 6"
locrian_nat6_scale.type = "2nd Mode of Harmonic Minor"

major_augmented_scale = scale.AbstractDiatonicScale("major")
major_augmented_scale._alteredDegrees = {5: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
major_augmented_scale.mode = "Major Augmented"
major_augmented_scale.type = "3rd Mode of Harmonic Minor"

lydian_diminished_scale = scale.AbstractDiatonicScale("lydian")
lydian_diminished_scale._alteredDegrees = {3: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}, 7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
lydian_diminished_scale.mode = "Lydian Diminished"
lydian_diminished_scale.type = "4th Mode of Harmonic Minor"

phrygian_dominant_scale = scale.AbstractDiatonicScale("mixolydian")
phrygian_dominant_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}, 6: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}, 7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
phrygian_dominant_scale.mode = "Phrygian Dominant"
phrygian_dominant_scale.type = "5th Mode of Harmonic Minor"

lydian_sharp2_scale = scale.AbstractDiatonicScale("lydian")
lydian_sharp2_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
lydian_sharp2_scale.mode = "Lydian Sharp 2"
lydian_sharp2_scale.type = "6th Mode of Harmonic Minor"

ultralocrian_scale = scale.AbstractDiatonicScale("locrian")
ultralocrian_scale._alteredDegrees = {4: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}, 7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
ultralocrian_scale.mode = "Ultra Locrian"
ultralocrian_scale.type = "7th Mode of Harmonic Minor"

### Melodic Minor Modes ###
melodic_minor_scale = scale.AbstractDiatonicScale("aeolian")
melodic_minor_scale._alteredDegrees = {6: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}, 7: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
melodic_minor_scale.mode = "Melodic Minor"
melodic_minor_scale.type = "1st Mode of Melodic Minor"

dorian_flat2_scale = scale.AbstractDiatonicScale("dorian")
dorian_flat2_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
dorian_flat2_scale.mode = "Dorian Flat 2"
dorian_flat2_scale.type = "2nd Mode of Melodic Minor"

lydian_augmented_scale = scale.AbstractDiatonicScale("lydian")
lydian_augmented_scale._alteredDegrees = {5: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
lydian_augmented_scale.mode = "Lydian Augmented"
lydian_augmented_scale.type = "3rd Mode of Melodic Minor"

lydian_dominant_scale = scale.AbstractDiatonicScale("lydian")
lydian_dominant_scale._alteredDegrees = {7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
lydian_dominant_scale.mode = "Lydian Dominant"
lydian_dominant_scale.type = "4th Mode of Melodic Minor"

major_minor_scale = scale.AbstractDiatonicScale("major")
major_minor_scale._alteredDegrees = {6: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}, 7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
major_minor_scale.mode = "Major Minor"
major_minor_scale.type = "5th Mode of Melodic Minor"

locrian_sharp2_scale = scale.AbstractDiatonicScale("locrian")
locrian_sharp2_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
locrian_sharp2_scale.mode = "Locrian Sharp 2"
locrian_sharp2_scale.type = "6th Mode of Melodic Minor"

superlocrian_scale = scale.AbstractDiatonicScale("locrian")
superlocrian_scale._alteredDegrees = {4: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
superlocrian_scale.mode = "Super Locrian"
superlocrian_scale.type = "7th Mode of Melodic Minor"

### Harmonic Major Modes ###
harmonic_major_scale = scale.AbstractDiatonicScale()
harmonic_major_scale._alteredDegrees = {6: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
harmonic_major_scale.type = "1st Mode of Harmonic Major"

dorian_flat5_scale = scale.AbstractDiatonicScale("dorian")
dorian_flat5_scale._alteredDegrees = {5: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
dorian_flat5_scale.mode = "Dorian Flat 5"
dorian_flat5_scale.type = "2nd Mode of Harmonic Major"

phrygian_flat4_scale = scale.AbstractDiatonicScale("phrygian")
phrygian_flat4_scale._alteredDegrees = {4: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
phrygian_flat4_scale.mode = "Phrygian Flat 4"
phrygian_flat4_scale.type = "3rd Mode of Harmonic Major"

lydian_flat3_scale = scale.AbstractDiatonicScale("lydian")
lydian_flat3_scale._alteredDegrees = {3: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
lydian_flat3_scale.mode = "Lydian Flat 3"
lydian_flat3_scale.type = "4th Mode of Harmonic Major"

mixolydian_flat2_scale = scale.AbstractDiatonicScale("mixolydian")
mixolydian_flat2_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
mixolydian_flat2_scale.mode = "Mixolydian Flat 2"
mixolydian_flat2_scale.type = "5th Mode of Harmonic Major"

lydian_augmented_sharp2_scale = scale.AbstractDiatonicScale("lydian")
lydian_augmented_sharp2_scale._alteredDegrees = {2: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}, 5: {'direction': scale.Direction.BI, 'interval': interval.Interval("a1")}}
lydian_augmented_sharp2_scale.mode = "Lydian Augmented Sharp 2"
lydian_augmented_sharp2_scale.type = "6th Mode of Harmonic Major"

locrian_doubleFlat7_scale = scale.AbstractDiatonicScale("locrian")
locrian_doubleFlat7_scale._alteredDegrees = {7: {'direction': scale.Direction.BI, 'interval': interval.Interval("-a1")}}
locrian_doubleFlat7_scale.mode = "Locrian Double Flat 7"
locrian_doubleFlat7_scale.type = "7th Mode of Harmonic Major"

### Miscellaneous Modes ###
wt1 = pitch.Pitch("C")
wt2 = pitch.Pitch("D")
wt3 = pitch.Pitch("E")
wt4 = pitch.Pitch("F#")
wt5 = pitch.Pitch("G#")
wt6 = pitch.Pitch("A#")
whole_tone_scale = scale.AbstractDiatonicScale()
whole_tone_scale.buildNetworkFromPitches([wt1, wt2, wt3, wt4, wt5, wt6])
whole_tone_scale.type = "Whole Tone"

c1 = pitch.Pitch("C")
c2 = pitch.Pitch("D")
c3 = pitch.Pitch("Eb")
c4 = pitch.Pitch("F")
c5 = pitch.Pitch("Gb")
c6 = pitch.Pitch("Ab")
c7 = pitch.Pitch("A")
c8 = pitch.Pitch("B")
whole_half_diminished_scale = scale.AbstractOctatonicScale()
whole_half_diminished_scale.buildNetworkFromPitches([c1, c2, c3, c4, c5, c6, c7, c8])
whole_half_diminished_scale.type = "Whole Half Diminished"

e1 = pitch.Pitch("C")
e2 = pitch.Pitch("C#")
e3 = pitch.Pitch("D#")
e4 = pitch.Pitch("E")
e5 = pitch.Pitch("F#")
e6 = pitch.Pitch("G")
e7 = pitch.Pitch("A")
e8 = pitch.Pitch("Bb")
half_whole_diminished_scale = scale.AbstractOctatonicScale()
half_whole_diminished_scale.buildNetworkFromPitches([e1, e2, e3, e4, e5, e6, e7, e8])
half_whole_diminished_scale.type = "Half Whole Diminished"


### List of all scales ###
master_scale_dict = {}
master_scale_dict["ionian"] = ionian_scale
master_scale_dict["dorian"] = dorian_scale
master_scale_dict["phrygian"] = phrygian_scale
master_scale_dict["lydian"] = lydian_scale
master_scale_dict["mixolydian"] = mixolydian_scale
master_scale_dict["aeolian"] = aeolian_scale
master_scale_dict["locrian"] = locrian_scale
master_scale_dict["harmonic minor"] = harmonic_minor_scale
master_scale_dict["locrian natural 6"] = locrian_nat6_scale
master_scale_dict["major augmented"] = major_augmented_scale
master_scale_dict["lydian diminished"] = lydian_diminished_scale
master_scale_dict["phrygian dominant"] = phrygian_dominant_scale
master_scale_dict["lydian sharp 2"] = lydian_sharp2_scale
master_scale_dict["ultralocrian"] = ultralocrian_scale
master_scale_dict["melodic minor"] = melodic_minor_scale
master_scale_dict["dorian flat 2"] = dorian_flat2_scale
master_scale_dict["lydian augmented"] = lydian_augmented_scale
master_scale_dict["lydian dominant"] = lydian_dominant_scale
master_scale_dict["major minor"] = major_minor_scale
master_scale_dict["locrian sharp 2"] = locrian_sharp2_scale
master_scale_dict["super locrian"] = superlocrian_scale
master_scale_dict["harmonic major"] = harmonic_major_scale
master_scale_dict["dorian flat 5"] = dorian_flat5_scale
master_scale_dict["phrygian flat 4"] = phrygian_flat4_scale
master_scale_dict["lydian flat 3"] = lydian_flat3_scale
master_scale_dict["mixolydian flat 2"] = mixolydian_flat2_scale
master_scale_dict["lydian augmented sharp 2"] = lydian_augmented_sharp2_scale
master_scale_dict["locrian double flat 7"] = locrian_doubleFlat7_scale
master_scale_dict["whole tone"] = whole_tone_scale
master_scale_dict["whole half diminished"] = whole_half_diminished_scale
master_scale_dict["half whole diminished"] = half_whole_diminished_scale

scale_key_list = list(master_scale_dict.keys())

