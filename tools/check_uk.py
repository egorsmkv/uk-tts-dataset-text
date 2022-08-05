def only_uk_sentence(v):
    char_set_lower = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'.replace(',','').replace(' ', '')
    char_set_upper = char_set_lower.upper()
    char_set = char_set_lower + char_set_upper
    char_set = char_set + '—,!?' + ' '

    return all((True if x in char_set else False for x in v))


print(only_uk_sentence('що глупа історія буде'))
print(only_uk_sentence('— Ну, ти казав, що глупа історія буде, а vox ось ти розказуєш, ніби із книжки читав'))
