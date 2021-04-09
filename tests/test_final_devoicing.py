samples = {
    'standard': 'standart',
    'wąż': 'ṽɔ̃wʂ',

}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])