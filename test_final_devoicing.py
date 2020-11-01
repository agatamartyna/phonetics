samples = {
    'standard': 'standart',
    'wąż': 'v ̃ɔ̃w ʂ',
    'bug': 'buk'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])