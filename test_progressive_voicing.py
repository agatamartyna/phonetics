samples = {
    'liczba': 'lʲidʐba',
    'poczdam':'pɔdʐdam',
    'prośba':'prɔʑba',
    'kośba': 'kɔʑba',

}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])