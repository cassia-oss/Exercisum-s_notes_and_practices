def recite(start_verse, end_verse):
    lyrics = []
    sorting_numbers = ('first',
                      'second',
                      'third',
                      'fourth',
                      'fifth',
                      'sixth',
                      'seventh',
                      'eighth',
                      'ninth',
                      'tenth',
                      'eleventh',
                      'twelfth')
    gift_list = ('twelve Drummers Drumming, ',
                 'eleven Pipers Piping, ',
                 'ten Lords-a-Leaping, ',
                 'nine Ladies Dancing, ',
                 'eight Maids-a-Milking, ',
                 'seven Swans-a-Swimming, ',
                 'six Geese-a-Laying, ',
                 'five Gold Rings, ',
                 'four Calling Birds, ',
                 'three French Hens, ',
                 'two Turtle Doves, ',
                 'and a Partridge in a Pear Tree.')
    for i in range(12):
        if i == 0 :
            lyrics.append(f"On the {sorting_numbers[i]} day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
        else:
            lyrics.append(f"On the {sorting_numbers[i]} day of Christmas my true love gave to me: {str(''.join(gift_list[11 - i:]))}")
    return lyrics[start_verse - 1:end_verse]
    pass
