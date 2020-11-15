samples = {
    'jakże': 'jaɡʐɛ',
    'wszakżeż': 'fʂaɡʐɛʂ',
    'paśże': 'paʑʐɛ'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])