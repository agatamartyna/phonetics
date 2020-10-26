# słowik litera - dźwięk
ipa_dict = {
    'a': 'a',
    'ą': '\u0303\u0254\u0303w',
    'b': 'b',
    'c': '\u02a6',
    'ć': '\u02a8',
    'd': 'd',
    'dź': '\u02A5',
    'dz': '\u02A3',
    'dż': 'd\u0290',
    'e': '\u025B',
    'ę': '\u0303\u025B\u0303w',
    'f': 'f',
    'g': '\u0261',
    'h': 'x',
    'i': '\u0069',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'ł': 'w',
    'm': 'm',
    'n': 'n',
    'ń': '\u0272',
    'o': '\u0254',
    'ó': 'u',
    'p': '\u0070',
    'r': 'r',
    's': 's',
    'ś': '\u0255',
    't': 't',
    'u': 'u',
    'w': 'v',
    'y': '\u0268',
    'z': 'z',
    'ż': '\u0290',
    'ź': '\u0291'
}

# klasa samogłosek
ipa_vowels = [
    'a', '\u0303\u0254\u0303w', '\u025B', ' \u025B\u0303\u0303w', 'i', '\u0254', 'u', '\u0268'
]

# słownik dźwięczne - bezdźwięczne
voicing_dict = {
    'b': 'p',
    'd': 't',
    '\u02A3': '\u02a6',
    '\u02A5': '\u02a8',
    'd\u0290': 't\u0282',
    '\u0261': 'k',
    'v': 'f',
    'z': 's',
    '': 'x',
    '\u0290': '\u0282',
    '\u0291': '\u0255'
}

# słownik  bezdźwięczne-dźwięczne -
voi_dict_rev = {value: key for key, value in voicing_dict.items()}

# sekwencje dźwięków do zmiany
clusters_dict = {
    '\u02a6i': '\u02a8i',
    'si': '\u0255i',
    'dzi': '\u02A5i',
    'zi': '\u0291i',
    '\u02a6x': 'x',
    'rz': '\u0290',
    'sz': '\u0282',
    '\u02a6z': 't\u0282',
    'ni': '\u0272i',
    'dz': '\u02A3',
    'd\u0291': '\u02A5'
}

# słownik spalatalizowanych (miękich) sekwencji parami:zapis jeden do jednego - i jak to powino wyglądać
soft_clusters_dict = {
    '\u02a6i': '\u02a8i',
    'si': '\u0255i',
    'dzi': '\u02A5i',
    'zi': '\u0291i',
    'ni': '\u0272i'
}

# słownik sybilantów (takich co syczą)  parami bezdźwięczny: - dźwięczny
sibilants_dict = {
    '\u02a6': '\u02A3',
    '\u02a8': '\u02A5',
    't\u0282': 'd\u0290',
    's': 'z',
    '\u0255': '\u0291',
    '\u0282': '\u0290'
}

# spalatalizowane (miękkie)
pals = ['\u02a8', '\u0255', '\u02A5', '\u0291', '\u0272']

# niespalatalizowane
non_pals = ['b', 'd', 'f', '\u0261', 'x', 'k', 'l', 'm', 'p', 'r', 't', 'v']


def transcribe(word):

    # transkrypcja jeden do jednego: litera - dźwięk
    ph_word = ''
    for letter in word:
        ph_word += str(ipa_dict[letter])

    # żeby dwuznaki (np. 'ch', 'rz') były transkrybowane jak należy
    for cluster in soft_clusters_dict:
        for cluster in clusters_dict:
            if cluster in ph_word:
                ph_word = ph_word.replace(cluster, clusters_dict[cluster])

    #  konwencja zapisu:  w sekwencji palatal + 'i' + samogł pomija się 'i'
    for item in ph_word:
        if item in pals:
            p = ph_word.index(item)
            if p <= len(ph_word) - 3 and ph_word[p + 1] == 'i' and ph_word[p + 2] in ipa_vowels:
                ph_word = ph_word[:p + 1] + ph_word[p + 2:]

    #  konwencja zapisu:  w sekwencji spółgł +'i'+ samogł zamienia się 'i' na 'j'
    for item in ph_word:
        if item in non_pals:
            p = ph_word.index(item)
            if p <= len(ph_word) - 3 and ph_word[p + 1] == 'i' and ph_word[p + 2] in ipa_vowels:
                ph_word = ph_word[:p + 1] + 'j' + ph_word[p + 2:]

    # końcowe ubezdźwięcznienie (bo piszemy 'uwiąd' a mówimy 'uwiąt')
    for voiced in [key for key in voicing_dict.keys()]:
        if ph_word[-2:] == voiced:
            ph_word = ph_word[:-2] + voicing_dict[voiced]
        elif ph_word[-1] == voiced:
            ph_word = ph_word[:-1] + voicing_dict[voiced]

    # postępowe udźwięcznienie (bo mómiwy 'proźba' 'lidżba', 'podżdam' 'tagże')
    for i in range(len(ph_word) - 1):
        if (
                ph_word[i] in sibilants_dict and
                ph_word[i + 1] in voicing_dict
        ):
            if ph_word[i - 1:i + 1] in sibilants_dict:
                vd_item = sibilants_dict[ph_word[i - 1:i + 1]]
                ph_word = ph_word[:i - 1] + vd_item + ph_word[i + 1:]
            elif ph_word[i] in sibilants_dict:
                vd_item = sibilants_dict[ph_word[i]]
                ph_word = ph_word[:i] + vd_item + ph_word[i + 1:]
        elif (
                ph_word[i] == '\u0290' and
                'ż' in word[i - 2:i + 1] and
                ph_word[i + 1] in ipa_vowels and
                ph_word[i - 1] in voi_dict_rev
        ):
            vd_item = voi_dict_rev[ph_word[i - 1]]
            ph_word = ph_word[:i - 1] + vd_item + ph_word[i:]

    # Postępowe ubezdźwięcznienie, bo mówimy 'kszysz', a nie 'krzyż'
    for i in range(len(ph_word) - 2):
        if ph_word[i] in voi_dict_rev and ph_word[i + 1] in voicing_dict:
            vless_item = voicing_dict[ph_word[i + 1]]
            ph_word = ph_word[:i + 1] + vless_item + ph_word[i + 2:]


    # wsteczne ubezdźwięcznienie bo piszemy 'babka', 'rozpacz' a mówimy 'bapka'. 'rospacz'
    for i in range(len(ph_word) - 2):
        if ph_word[i] in voicing_dict and ph_word[i + 1] in voi_dict_rev:
            vless_item = voicing_dict[ph_word[i]]
            ph_word = ph_word[:i] + vless_item + ph_word[i + 1:]

    return ph_word


if __name__ == '__main__':
    print(transcribe(input('Wpisz słowo: ')))
