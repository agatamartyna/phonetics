from ipa_transcribe_polish import transcribe

# consonants
VD_BILAB_STOP = 'b'
VS_ALV_AFF = 'ts'
VS_PAL_AFF = 't\u0255'
VS_POSTALV_AFF = 't\u0282'
VD_DENT_STOP = 'd'
VD_PAL_AFF = 'd\u0291'
VD_ALV_AFF = 'dz'
VD_POSTALV_AFF = 'd\u0290'
VS_LABDENT_FRIC = 'f'
VD_VEL_STOP = '\u0261'
VS_VEL_FRIC = 'x'
VD_VEL_FRIC = '\u0263'
PAL_APPROX = 'j'
VS_VEL_STOP = 'k'
ALV_LAT_APPROX = 'l'
BILAB_APPROX = 'w'
BILAB_NAS = 'm'
DENT_NAS = 'n'
PAL_NAS = '\u0272'
VS_BILAB_STOP = 'p'
ALV_TRILL = 'r'
VS_ALV_FRIC = 's'
VS_PAL_FRIC = '\u0255'
VS_DENT_STOP = 't'
VD_LABDENT_FRIC = 'v'
VS_POSTALV_FRIC = '\u0282'
VD_ALV_FRIC = 'z'
VD_POSTALV_FRIC = '\u0290'
VD_PAL_FRIC = '\u0291'

"""
nasalised vowels - notation which more or less works with my editor (tilde 
before the nasalised item) - works with most items
"""
OPEN_MID_ROUND_NAS_DYPH = '\u0303\u0254\u0303w'
MID_OPEN_FRONT_NAS_DYPH = '\u0303\u025B\u0303w'

"""
nasalised vowels - something that seems to be the canonical notation 
which does not work with my editor (tilde after the item which it's
supposed to modify)
"""
MID_OPEN_ROUND_ALT = '\u0254\u0303w\u0303'
MID_OPEN_FRONT_ALT = '\u025B\u0303w\u0303'

mine = [OPEN_MID_ROUND_NAS_DYPH, MID_OPEN_FRONT_NAS_DYPH]
cano = [MID_OPEN_ROUND_ALT, MID_OPEN_FRONT_ALT]

consies = [
    VD_BILAB_STOP, VS_ALV_AFF, VS_PAL_AFF, VS_POSTALV_AFF, VD_DENT_STOP, VD_PAL_AFF,
    VD_ALV_AFF, VD_POSTALV_AFF, VS_LABDENT_FRIC, VD_VEL_STOP, VS_VEL_FRIC, VD_VEL_FRIC,
    PAL_APPROX, VS_VEL_STOP, ALV_LAT_APPROX, BILAB_APPROX, BILAB_NAS, DENT_NAS,
    PAL_NAS, VS_BILAB_STOP, ALV_TRILL, VS_ALV_FRIC, VS_PAL_FRIC, VS_DENT_STOP,
    VD_LABDENT_FRIC, VS_POSTALV_FRIC, VD_ALV_FRIC, VD_POSTALV_FRIC, VD_PAL_FRIC
]

for consie in consies:
    print(consie + mine[0], '-', consie + mine[1], '-', consie + cano[0], '-', consie + cano[1])
print('i' + mine[0], '-', 'i' + mine[1], '-', 'i' + cano[0], '-', 'i' + cano[1])