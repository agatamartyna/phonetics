class Vowel:
    vowels = []
    def __init__(self, ipa, ort, back="front", aperture="close"):
        self.ipa = ipa
        self.back = back
        self.aperture = aperture
        self.ort = ort
        Vowel.vowels.append(self)

    def __str__(self):
        return f"{self.aperture} {self.back}"

    def get_ipa(self):
        return self.ipa

    def get_ort(self):
        return self.ort


class Nasalised(Vowel):
    def __init__(self, nasalised="nasalised", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nasalised = nasalised

    def __str__(self):
        return f"{self.nasalised} {self.aperture} {self.back}"


open_front = Vowel(ipa="a", ort="a", aperture="open")
close_central = Vowel(ipa='\u0268', ort="y", back="central")
open_mid_front = Vowel(ipa="\u025B",ort="e", aperture="open-mid")
close_front = Vowel(ipa="\u0069", ort="i",)
open_mid_back = Vowel(ipa="\u0254", ort="o", back="back", aperture="open_mid")
close_back = Vowel(ipa="u", ort="u", back="back")
close_back = Vowel(ipa="u", ort="ó", back="back")

open_mid_back_nas = Nasalised(ipa="\u0254\u0303w\u0303", ort="ą", back="back", aperture="open-mid")
open_mid_front_nas = Nasalised(ipa="\u025B\u0303w\u0303", ort="ę", aperture="open-mid")


class Consonant:
    consonants = []
    def __init__(
            self, ipa, ort,
            voice="voiced", place="alveolar", manner="fricative",
            obstruent="obstruent", continuant="non-continuant",
            sibilant="non-sibilant"
    ):
        self.ipa = ipa
        self.ort = ort
        self.voice = voice
        self.place = place
        self.manner = manner
        self.obstruent = obstruent
        self.continuant = continuant
        self.sibilant = sibilant
        Consonant.consonants.append(self)

    def __str__(self):
        return f"{self.voice} {self.place} {self.manner}"


vs_bilab_stop = Consonant(ort="p", ipa="p", voice="voiceless", place="bilabial", manner="stop")
vd_bilab_stop = Consonant(ort="b", ipa="b", place="bilabial", manner="stop")
vs_dent_stop = Consonant(ort="t", ipa="t", place="dental", manner="stop")
vd_dent_stop = Consonant(ort="d", ipa="d", place="dental", manner="stop")
vs_vel_stop = Consonant(ort="k", ipa="k", voice="voiceless", place="velar", manner="stop")
vd_vel_stop = Consonant(ort="g", ipa="\u0261", place="velar", manner="stop")

vs_alv_aff = Consonant(ort="c", ipa="ts", voice="voiceless", manner="affricate", sibilant="sibilant")
vd_alv_aff = Consonant(ort="dz", ipa="dz", manner="affricate", sibilant="sibilant")
vs_postalv_aff = Consonant(ort="cz", ipa="t\u0282", voice="voiceless", place="postalveolar", manner="affricate", sibilant="sibilant")
vd_postalv_aff = Consonant(ort="dż", ipa="d\u0290", place="postalveolar", manner="affricate", sibilant="sibilant")
vs_pal_aff = Consonant(ort="ć", ipa="t\u0255", place="palatal", voice="voiceless", manner="affricate", sibilant="sibilant")
vd_pal_aff = Consonant(ort="dź", ipa="d\u0291", place="palatal", manner="affricate", sibilant="sibilant")

vs_labdent_fric = Consonant(ort="f", ipa="f", voice="voiceless", place="labiodental", continuant="continuant", sibilant="sibilant")
vd_labdent_fric = Consonant(ort="w", ipa="v", place="labiodental", continuant="continuant", sibilant="sibilant")
vs_alv_fric = Consonant(ort="s", ipa="s", voice="voiceless", continuant="continuant", sibilant="sibilant")
vd_alv_fric = Consonant(ort="z", ipa="z", continuant="continuant", sibilant="sibilant")
vs_postalv_fric = Consonant(ort="sz", ipa="\u0282", voice="voiceless", place="postalveolar", continuant="continuant", sibilant="sibilant")
vd_postalv_fric = Consonant(ort="ż", ipa="\u0290", place="postalveolar", continuant="continuant", sibilant="sibilant")
vs_pal_fric = Consonant(ort="ś", ipa="\u0255", voice="voiceless", place="palatal", continuant="continuant", sibilant="sibilant")
vd_pal_fric = Consonant(ort="ź", ipa="\u0291", place="palatal", continuant="continuant", sibilant="sibilant")
vs_vel_fric = Consonant(ort="h", ipa="x", voice="voiceless", place="velar", continuant="continuant", sibilant="sibilant")
vd_vel_fric = Consonant(ort="", ipa="\u0263", place="velar", continuant="continuant", sibilant="sibilant")

bilab_approx = Consonant(ort="ł", ipa="w", place="bilabial", manner="approximant", obstruent="non-obstruent", continuant="continuant")
alv_approx = Consonant(ort="l", ipa='l', manner="approximant", obstruent="non-obstruent", continuant="continuant")
pal_approx = Consonant(ort="j", ipa="j", place="palatal", manner="approximant", obstruent="non-obstruent", continuant="continuant")

alv_trill = Consonant(ort="r", ipa="r", manner="trill", obstruent="non-obstruent", continuant="continuant")

bilab_nas = Consonant(ort="m", ipa="m", place="bilabial", manner="nasal", obstruent="non-obstruent")
dent_nas = Consonant(ort="n", ipa="n", place="dental", manner="nasal", obstruent="non-obstruent")
pal_nas = Consonant(ort="ń", ipa="n", place="palatal", manner="nasal", obstruent="non-obstruent")

objects = Vowel.vowels + Consonant.consonants


def transcribe(word):

    # one-to-one character-symbol transcription
    ph_word = ''
    for letter in word:
        for object in objects:
            if letter == object.ort:
                ph_word += object.ipa
                break


    # Progressive Voicing Morphological Conditioning
    for i in range(len(word) - 1):
        if (
                word[i:i + 2] == 'że' and
                word[i - 1].place = "voiceless"
        ):
            ph_word_1 = ''
            for letter in word[:i - 1]:
                ph_word_1 += str(ipa_dict[letter])
            ph_word2 = ''
            for letter in word[i:]:
                ph_word2 += str(ipa_dict[letter])
            vs_item = ipa_dict[word[i - 1]]
            vd_item = voi_dict_rev[vs_item]
            ph_word = ph_word1 + vd_item + ph_word2

    return ph_word

if __name__ == "__main__":
    word = input("Wpisz słowo: ")
    print(transcribe(word))


"""

tilde = '\u0303'
space = ' '
pal = '\u02B2'

print(Vowel.vowels[3].ipa)
print(Consonant.consonants[20].ipa)

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
non_pals = [VS_BILAB_STOP, VD_BILAB_STOP, VS_DENT_STOP, VD_DENT_STOP, VS_LABDENT_FRIC, VD_LABDENT_FRIC, '\u0261', 'x', 'k', 'l', 'm', 'r',]

"""