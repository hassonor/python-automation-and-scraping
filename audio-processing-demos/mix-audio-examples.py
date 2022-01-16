from pydub import AudioSegment

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffplay.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"


def mixing_audio_files(file_path_1, file_path_2):
    song = AudioSegment.from_wav(file_path_1)
    beat = AudioSegment.from_wav(file_path_2)

    mixed = beat.overlay(song)  # mixed the beat and song :-)
    mixed.export('files/mixed_song.wav')


mixing_audio_files('files/song.wav', 'files/beat.wav')
