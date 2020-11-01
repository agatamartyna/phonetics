samples = {
    'świat':'ɕfʲjat',
    'swat':'sfat',
    'wycwanić':'vɨtsfaɲitɕ',
    'praprzyczyna':'prapʂɨtʂɨna',
    'przetrzyma': 'pʂɛtʂɨma'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])