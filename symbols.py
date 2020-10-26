# sound inventory vowels

OPEN_FRONT = 'a'
OPEN_MID_ROUND_NAS_DYPH = '\u0303\u0254\u0303w'   # mid-open back vowel nasalised dyphthongised
MID_OPEN_FRONT = '\u025B'
MID_OPEN_FRONT_NAS_DYPH = '\u0303\u025B\u0303w'   # mid-open front vowel nasalised dyphthongised
CLOSE_FRONT = '\u0069'
MID_OPEN_ROUND = '\u0254'
CLOSE_BACK_ROUND = 'u'
CLOSE_CENT = '\u0268' # close central vowel

#sound inventory consonants

VD_BILAB_STOP = 'b'  # voiced bilabial stop
VS_ALV_AFF = '\u02a6'   # voiceless alvoelar affricate
VS_PAL_AFF = '\u02a8'   #voiceless palatal affricate
VS_POSTALV_AFF = 't\u0361\u0282'   # voiceless postalveolar affricate
VD_DENT_STOP = 'd'   # voiced dental stop
VD_PAL_AFF = '\u02A5'   # voiced palatal affricate
VD_ALV_AFF = '\u02A3'   # voiced alveolar affricate
VD_POSTALV_AFF = 'd\u0290'   # voiced postalveolar affricate
VS_LABDENT_FRIC = 'f'   # voiceless labiodental fricative
VD_VEL_STOP = '\u0261'   # voiced velar stop
VS_VEL_FRIC = 'x'   # voiceless velar fricative
PAL_APPROX = 'j'   # palatal approximant
VS_VEL_STOP = 'k'    # voiceless velar stop
ALV_LAT_APPROX = 'l'   # alveolar lateral approximant
BILAB_GLIDE = 'w'   # bilabial glide
BILAB_NAS = 'm'   # bialbial nasal
ALV_NAS = 'n'    # alveolar nasal
PAL_NAS = '\u0272'   # palatal nasal
VS_BILAB_STOP = 'p'   # voiceless bilabial stop
ALV_TRILL = 'r'   # alveolar trill
VD_ALV_FRIC = 's'  # voiced alveolar fricative
VS_PAL_FRIC = '\u0255'   # voiceless palatal fricative
VS_DENT_STOP = 't'   # voiceless dental stop
VD_LABDENT_FRIC = 'v'   # voiced labiodental fricative
VS_POSTALV_FRIC = '\u0282' # voiceless postalveolar fricative
VD_ALV_FRIC = 'z' # voiced alveolar fricative
VD_POSTALV_FRIC = '\u0290'   #voiced postalveolar fricative
VD_PAL_FRIC = '\u0291'   # voiced palatal fricative

transcribe_dict = {
    'a':OPEN_FRONT, 'ą':OPEN_MID_ROUND_NAS_DYPH, 'b':VD_BILAB_STOP, 'c':VS_ALV_AFF, 'ć':VS_PAL_AFF, 'cz':VS_POSTALV_AFF,
    'ch':VS_VEL_FRIC, 'd':VD_DENT_STOP, 'dź':VD_PAL_AFF, 'dz':VD_ALV_AFF, 'dż':VD_POSTALV_AFF, 'e':MID_OPEN_FRONT,
    'ę':MID_OPEN_FRONT_NAS_DYPH, 'f':VS_LABDENT_FRIC, 'g':VD_VEL_STOP, 'h':VS_VEL_FRIC, 'i':CLOSE_FRONT, 'j':PAL_APPROX,
    'k':VS_VEL_STOP, 'l':ALV_LAT_APPROX, 'ł':BILAB_GLIDE, 'm':BILAB_NAS, 'n':ALV_NAS, 'ń':PAL_NAS, 'o':MID_OPEN_ROUND, 'ó':CLOSE_BACK_ROUND,
    'p':VS_BILAB_STOP, 'r':ALV_TRILL, 's':VD_ALV_FRIC, 'ś':VS_PAL_FRIC, 'sz':VS_POSTALV_FRIC, 't':VS_DENT_STOP,
    'u':CLOSE_BACK_ROUND, 'w':VD_LABDENT_FRIC, 'y':CLOSE_CENT, 'z':VD_ALV_FRIC, 'ż':VD_POSTALV_FRIC, 'ź':VD_PAL_FRIC
}

print(transcribe_dict)