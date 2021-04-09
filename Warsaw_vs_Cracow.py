from string import punctuation
from ipa_transcribe_polish import transcribe

# sound inventory vowels
OPEN_FRONT = 'a'
OPEN_MID_ROUND_NAS_DYPH = '\u0254\u0303w\u0303'
MID_OPEN_FRONT = '\u025B'
MID_OPEN_FRONT_NAS_DYPH = '\u025B\u0303w\u0303'
CLOSE_FRONT = '\u0069'
MID_OPEN_BACK_ROUND = '\u0254'
CLOSE_BACK_ROUND = 'u'
CLOSE_CENT = '\u0268'
TILDE = '\u0303'
SPACE = ' '

# palatalised
PAL = '\u02B2'

# sound inventory consonants
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


# character - ipa symbol maps
ipa_dict = {
    'a': OPEN_FRONT,
    'ą': OPEN_MID_ROUND_NAS_DYPH,
    'b': VD_BILAB_STOP,
    'c': VS_ALV_AFF,
    'ć': VS_PAL_AFF,
    'ch': VS_VEL_FRIC,
    'd': VD_DENT_STOP,
    'dź': VD_PAL_AFF,
    'dz': VD_ALV_AFF,
    'dż': VD_POSTALV_AFF,
    'e': MID_OPEN_FRONT,
    'ę': MID_OPEN_FRONT_NAS_DYPH,
    'f': VS_LABDENT_FRIC,
    'g': VD_VEL_STOP,
    'h': VS_VEL_FRIC,
    'i': CLOSE_FRONT,
    'j': PAL_APPROX,
    'k': VS_VEL_STOP,
    'l': ALV_LAT_APPROX,
    'ł': BILAB_APPROX,
    'm': BILAB_NAS,
    'n': DENT_NAS,
    'ń': PAL_NAS,
    'o': MID_OPEN_BACK_ROUND,
    'ó': CLOSE_BACK_ROUND,
    'p': VS_BILAB_STOP,
    'r': ALV_TRILL,
    's': VS_ALV_FRIC,
    'ś': VS_PAL_FRIC,
    't': VS_DENT_STOP,
    'u': CLOSE_BACK_ROUND,
    'w': VD_LABDENT_FRIC,
    'y': CLOSE_CENT,
    'z': VD_ALV_FRIC,
    'ż': VD_POSTALV_FRIC,
    'ź': VD_PAL_FRIC
}

# vowels
ipa_vowels = [
    OPEN_FRONT,
    OPEN_MID_ROUND_NAS_DYPH,
    MID_OPEN_FRONT,
    MID_OPEN_FRONT_NAS_DYPH,
    CLOSE_FRONT,
    MID_OPEN_BACK_ROUND,
    CLOSE_BACK_ROUND,
    CLOSE_CENT,
    SPACE
]

# voiced - voiceless pairs of obstruents
voicing_dict = {
    VD_BILAB_STOP: VS_BILAB_STOP,
    VD_DENT_STOP: VS_DENT_STOP,
    VD_ALV_AFF: VS_ALV_AFF,
    VD_PAL_AFF: VS_PAL_AFF,
    VD_POSTALV_AFF: VS_POSTALV_AFF,
    VD_VEL_STOP: VS_VEL_STOP,
    VD_LABDENT_FRIC: VS_LABDENT_FRIC,
    VD_ALV_FRIC: VS_ALV_FRIC,
    VD_VEL_FRIC: VS_VEL_FRIC,
    VD_POSTALV_FRIC: VS_POSTALV_FRIC,
    VD_PAL_FRIC: VS_PAL_FRIC
}

# voiceless - voiced pairs of obstruents
voi_dict_rev = {value: key for key, value in voicing_dict.items()}

# non-continuant obstruents
non_cont_obstr = {
    VD_BILAB_STOP: VS_BILAB_STOP,
    VD_DENT_STOP: VS_DENT_STOP,
    VD_ALV_AFF: VS_ALV_AFF,
    VD_PAL_AFF: VS_PAL_AFF,
    VD_POSTALV_AFF: VS_POSTALV_AFF,
    VD_VEL_STOP: VS_VEL_STOP,
}

# continuant obsturents
cont_obstr = ['w', 'f', 'z', 's', 'sz', 'ż', 'rz', 'ś', 'si', 'ź', 'zi', 'h', 'ch']

# simplify cluster
clusters_dict = {
    VS_ALV_AFF + CLOSE_FRONT: VS_PAL_AFF + CLOSE_FRONT,
    VS_ALV_FRIC + CLOSE_FRONT: VS_PAL_FRIC + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC + CLOSE_FRONT: VD_PAL_AFF + CLOSE_FRONT,
    VD_ALV_FRIC + CLOSE_FRONT: VD_PAL_FRIC + CLOSE_FRONT,
    VS_ALV_AFF + VS_VEL_FRIC: VS_VEL_FRIC,
    ALV_TRILL + VD_ALV_FRIC: VD_POSTALV_FRIC,
    VS_ALV_FRIC + VD_ALV_FRIC: VS_POSTALV_FRIC,
    VS_ALV_AFF + VD_ALV_FRIC: VS_DENT_STOP+VS_POSTALV_FRIC,
    DENT_NAS + CLOSE_FRONT: PAL_NAS + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC: VD_ALV_AFF,
    VD_DENT_STOP + VD_PAL_FRIC: VD_PAL_AFF
}

# palatalised sounds with multiple character notation in pairs one-to-one transcription - sound
soft_clusters_dict = {
    VS_ALV_AFF + CLOSE_FRONT: VS_PAL_AFF + CLOSE_FRONT,
    VS_ALV_FRIC + CLOSE_FRONT: VS_PAL_FRIC + CLOSE_FRONT,
    VD_DENT_STOP + VD_ALV_FRIC + CLOSE_FRONT: VD_POSTALV_AFF + CLOSE_FRONT,
    VD_ALV_AFF + CLOSE_FRONT: VD_PAL_FRIC + CLOSE_FRONT,
    DENT_NAS + CLOSE_FRONT: PAL_NAS + CLOSE_FRONT
}

# sibilants arranged into pairs voiceless - voiced
sibilants_dict = {
    VS_ALV_AFF: VD_ALV_AFF,
    VS_PAL_AFF: VD_PAL_AFF,
    VS_POSTALV_AFF: VD_POSTALV_AFF,
    VS_ALV_FRIC: VD_ALV_FRIC,
    VS_PAL_FRIC: VD_PAL_FRIC,
    VS_POSTALV_FRIC: VD_POSTALV_FRIC
}

# palatals
pals = [
    VS_PAL_AFF,
    VD_PAL_AFF,
    VS_PAL_FRIC,
    VD_PAL_FRIC,
    PAL_NAS
]

# non-palatals
non_pals = [
    VS_BILAB_STOP, VD_BILAB_STOP,
    VS_DENT_STOP, VD_DENT_STOP,
    VS_LABDENT_FRIC, VD_LABDENT_FRIC,
    VS_VEL_STOP, VD_VEL_STOP,
    VS_VEL_FRIC, VD_VEL_FRIC,
    ALV_LAT_APPROX, ALV_TRILL,
    BILAB_NAS, DENT_NAS
]

# vocalics
vocs = [PAL_APPROX, BILAB_APPROX, ALV_LAT_APPROX, ALV_TRILL, DENT_NAS, BILAB_NAS, PAL_NAS]


def transcribe_words_Cracow(text):

    # transcribe words separately and keep the original punctuation
    words = text.split(' ')
    ph_words = []
    ph_dict = {}
    for word in words:
        ph_word = ''
        if word[-1].isalpha():
            word = word.lower()
            ph_word = transcribe(word)
            ph_words += [ph_word]
            if word[-2:] in ['cz', 'ch', 'sz']:
                ph_dict[ph_word] = word[-2:]
            elif word[-1] in 'cćfhkpsśt':
                ph_dict[ph_word] = word[-1]
        else:
            punctu = word[-1]
            word = word[:-1]
            word = word.lower()
            ph_word = transcribe(word) + punctu
            ph_words += [ph_word]

    # phonological processes on word boundaries: pre-vocalic voicing
    for i in range(len(ph_words)-1):
        if (
            ph_words[i][-2:] in voi_dict_rev and
            (ph_words[i + 1][0] in vocs or ph_words[i + 1][0] in voicing_dict)
        ):
            ph_words[i] = (ph_words[i][:-2]) + (voi_dict_rev[(ph_words[i][-2:])])
        elif (
            (ph_words[i][-1]) in voi_dict_rev and
            (ph_words[i+1][0] in vocs or ph_words[i+1][0] in voicing_dict)
        ):
            ph_words[i] = (ph_words[i][:-1]) + (voi_dict_rev[(ph_words[i][-1])])

    ph_text = ' '.join(ph_words)

    return ph_text

def transcribe_words_Warsaw(text):

    # transcribe words separately and keep the original punctuation
    words = text.split(' ')
    ph_words = []
    ph_dict = {}
    for word in words:
        ph_word = ''
        if word[-1].isalpha():
            word = word.lower()
            ph_word = transcribe(word)
            ph_words += [ph_word]
        else:
            punctu = word[-1]
            word = word[:-1]
            word = word.lower()
            ph_word = transcribe(word) + punctu
            ph_words += [ph_word]
        if word[-2:] in ['ch', 'cz', 'sz']:
            ph_dict[ph_word] = word[-2:]
        elif word[-1] in 'cćfhkpsśt':
            ph_dict[ph_word] = word[-1]

    # phonological processes on word boundaries: pre-vocalic and pre-voiced voicing
    for i in range(len(ph_words)-1):
        if (
            ph_words[i][-2:] in voi_dict_rev and
            ph_words[i] in ph_dict and
            transcribe(ph_dict[ph_words[i]]) in voicing_dict and
            (ph_words[i + 1][0] in vocs or ph_words[i + 1][0] in voicing_dict or ph_words[i][-1] in ipa_vowels)
        ):
            ph_words[i] = (ph_words[i][:-2]) + (voi_dict_rev[(ph_words[i][-2:])])
        elif (
            ph_words[i][-1] in voi_dict_rev and
            ph_words[i] in ph_dict and
            transcribe(ph_dict[ph_words[i]]) in voicing_dict and
            (ph_words[i+1][0] in vocs or ph_words[i+1][0] in voicing_dict or ph_words[i][-1] in ipa_vowels)
        ):
            ph_words[i] = (ph_words[i][:-1]) + (voi_dict_rev[(ph_words[i][-1])])
        elif (
            ph_words[i][-1] in voi_dict_rev and
            ph_words[i + 1][0] in voicing_dict
        ):
            ph_words[i] = (ph_words[i][:-1]) + (voi_dict_rev[(ph_words[i][-1])])

    ph_text = ' '.join(ph_words)

    return ph_text


if __name__ == '__main__':
    accent = input("Wybierz akcent, w którym zostanie przetranskrybowany tekst: \n"
                   "1 oznacza akcent środkowopolski \n" 
                   "2 oznacza akcent południowopolski \n"
                   "Wybierz 1 lub 2: ")

    while accent not in ['1', '2'] and len(accent) != 1:
        print("Wpisz dokładnie jedną z dwóch cyfr 1 lub 2.")
        accent = input("Twój wybór to: ")

    text = input("Wpisz tekst: ")

    if accent == '1':
        print(transcribe_words_Warsaw(text))
    elif accent == '2':
        print(transcribe_words_Cracow(text))













