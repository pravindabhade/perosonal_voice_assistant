import whisper
import sounddevice as sd
import soundfile as sf

model = whisper.load_model("base")

def record_audio(filename="recording.wav", duration=5):

    print("Speak now...")

    sample_rate = 16000

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(filename, recording, sample_rate)

    return filename


def transcribe(filename):

    result = model.transcribe(filename)

    return result["text"]