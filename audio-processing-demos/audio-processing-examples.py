# download ffmpeg and unzip to "C:\ffmpeg" and set the path var "C:\ffmpeg\bin"
# you can dowonload it form here https://www.ffmpeg.org/
# see also this:  https://stackoverflow.com/questions/51219531/pydub-unable-to-locate-ffprobe

# Enjoy your mix DJ :-)


from pydub import AudioSegment

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffplay.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"
print(AudioSegment.converter)


def create_reverse_and_merged_audio_file(file_path):
    original = AudioSegment.from_wav(file_path)
    print(type(original))
    print(original)
    reversed_audio = original.reverse()  # reversed the original audio
    reversed_audio.export('reversed.wav')
    reversed_audio = reversed_audio + 15  # increase volume by 15
    first_two = original[0:5000]  # 5 seconds long
    first_two.export('first_5_seconds.wav')
    merged = original + AudioSegment.silent(
        1000) + reversed_audio  # add the original file the reversed audio + Adding 1s silence
    merged.export('merged_original_reversed.wav')


create_reverse_and_merged_audio_file('sample.wav')
