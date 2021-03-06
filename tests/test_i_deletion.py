samples = {
    'ziemia':'ʑɛmʲja',
    'siał': 'ɕaw',
    'podziało':'pɔdʑawɔ',
    'wyziębiony':'vɨʑɛmbʲjɔnɨ',
    'ciecierzyca': 'tɕɛtɕɛʐɨtsa',
    'nasiusiała': 'naɕuɕawa'
}

from ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])