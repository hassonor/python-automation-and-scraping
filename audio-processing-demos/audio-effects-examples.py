from pydub import AudioSegment

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffplay.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"


def audio_effects_make_it(file_path):
    song = AudioSegment.from_mp3(file_path)

    song_low = song.log_pass_filter(2000)
    song_low.export('song_low.wav')

    song_left = song.pan(-1)  # only left speaker (default 0)
    song_right = song.pan(1)  # only right speaker

    song_final = song_left + song_right + song_low
    song_final.export('song_final.wav')


audio_effects_make_it('files/song.wav')
