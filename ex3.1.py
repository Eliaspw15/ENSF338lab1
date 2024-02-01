import json
import matplotlib.pyplot as plt

with open('songdata.json', 'r') as file:
    data = json.load(file)

# Separate dataset by loudness values
below_eight = []
at_or_above_eight = []

for song in data:
    if song['loudness'] < -8:
        below_eight.append(song)
    elif song['loudness'] >= -8:
        at_or_above_eight.append(song)

# seperating tempo values from loudness lists
tempo_be = []
for song in below_eight:
    tempo_be.append(song['tempo'])

tempo_aae = []
for song in at_or_above_eight:
    tempo_aae.append(song['tempo'])

plt.hist(tempo_be, bins=20, color='blue', label='Loudness < -8')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Tempo Distribution for Songs')
plt.legend()
plt.savefig('hist1.png')  # Save histogram for loudness < -8

plt.clf()  # Clear plot for the second histogram

plt.hist(tempo_aae, bins=20, color='green', label='Loudness >= -8')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Tempo Distribution for Songs of Loudness Greater Than -8')
plt.legend()
plt.savefig('hist2.png')  # Save histogram for loudness >= -8
