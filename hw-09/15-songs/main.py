violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input('Сколько песен выбрать? '))
playlist_time = 0
for i in range(N):
    print('Название', i + 1, 'песни:', end=' ')
    s = input()
    for song in violator_songs:
        if s == song[0]:
            playlist_time += song[1]
print('Общее время звучания песен:', round(playlist_time, 2))
