samples = {
    'babka': 'bapka',
    'rozpacz': 'rɔspatʂ',
    'kładka': 'kwatka'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])