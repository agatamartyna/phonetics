samples = {
    'wiewiórka': 'vʲjɛvʲjurka',
    'wywiad': 'vɨvʲjat',
    'wywietrzcie':'vɨvʲjɛtʂtɕɛ',
    'babia': 'babʲja',
    'liliana': 'lʲilʲjana',
    'pięknie': 'pʲjɛŋkɲɛ'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])