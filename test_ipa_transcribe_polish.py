samples = {
    'ząb': 'zɔmp',
    'ślub': 'ɕlup',
    'kręty': 'krɛntɨ',
    'bieżnia': 'bʲɛʒɲa'
}

from ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])
