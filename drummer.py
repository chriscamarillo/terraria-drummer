from util import Window
from mido import MidiFile

drum_set = {
    'Kick-Drum': 2,
    'Floor-Tom': 5,
    'Mid-Tom': 8,
    'Hi-Tom': 14,
    'Snare-Drum': 17,
    'Base-Tom': 20,
    'Hi-Hat-closed': 24,
    'Ride-Cymbal': 27,
    'China-Cymbal': 32,
    'Crash-Cymbal': 35
}

midi_note = {
    35: 'Kick-Drum',
    36: 'Kick-Drum',
    41: 'Floor-Tom',
    43: 'Floor-Tom',
    47: 'Mid-Tom',
    48: 'Mid-Tom',
    50: 'Hi-Tom',
    38: 'Snare-Drum',
    40: 'Snare-Drum',
    42: 'Hi-Hat-closed',
    51: 'Ride-Cymbal',
    59: 'Ride-Cymbal',
    52: 'China-Cymbal',
    49: 'Crash-Cymbal',
    57: 'Crash-Cymbal'
}

def play(instrument):
    w = Window()
    if instrument in drum_set:
        l, t, r, b = w.get_terraria_dim()
        midX = (l + r) // 2
        midY = (t + b) // 2
        offSetX = int((r - l) * drum_set[instrument]/100)
        Window.click(midX + offSetX, midY)

def main():
    mid = MidiFile('toxicity.mid')
    playing = True
    track = iter(mid.play())

    while track:
        # pause / play
        if Window.space_press():
            while Window.space_press():
                pass
            playing = not playing
        if playing:
            msg = next(track)
            print(msg)
            if msg.type == 'note_on' and msg.note in midi_note:
                play(midi_note[msg.note])

if __name__ == '__main__':
    main()