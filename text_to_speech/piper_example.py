# Piper: fast, local neural text-to-speech. Runs fully offline once a voice is downloaded
# and sounds much more natural than the OS voices used by pyttsx3.
# Maintained project: https://github.com/OHF-Voice/piper1-gpl
# (the older rhasspy/piper repository is archived).
#
# 1. Install
#    pip install piper-tts
#
# 2. Download a voice model
#    List the available voices:
#        python -m piper.download_voices
#    Download one into the current directory (use --data-dir <DIR> to choose another folder):
#        python -m piper.download_voices en_US-lessac-medium
#    Manual alternative: browse https://huggingface.co/rhasspy/piper-voices/tree/main
#    (e.g. en/en_US/lessac/medium/) and download the files by hand.
#    Each voice needs BOTH files, side by side, with the same base name:
#        en_US-lessac-medium.onnx        <- the neural network model
#        en_US-lessac-medium.onnx.json   <- its config (sample rate, phoneme map, ...)
#    This script looks for them in the same folder as itself.
#
# 3. Model sizes (the .onnx file; the .onnx.json config is tiny, about 5 KB)
#    Checked against the rhasspy/piper-voices repo on Hugging Face:
#        x_low   ~20-28 MB   (smallest, lowest quality)
#        low     ~28-70 MB   (most are ~63 MB, e.g. en_US-amy-low)
#        medium  ~63-81 MB   (en_US-lessac-medium is ~63 MB; the sensible default)
#        high    ~63-137 MB  (en_US-lessac-high is ~114 MB; slowest, best quality)
#    The quality label describes the model that was trained, so file size and
#    quality do not always line up exactly (en_US-lessac-low and -medium are both ~63 MB).
#
# 4. Voice naming convention
#    <language>_<REGION>-<name>-<quality>
#    e.g. en_US-lessac-medium = English, United States, speaker "lessac", medium quality.
#
# Piper only produces audio; it does not play it. This script writes a WAV file and,
# on Windows only, plays it with the standard library's winsound.

import sys
import wave
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

VOICE_NAME = "en_US-lessac-medium"
MODEL_PATH = Path(__file__).parent / f"{VOICE_NAME}.onnx"
OUTPUT_PATH = Path(__file__).parent / "piper_output.wav"


def synthesize_to_wav(voice, text, path, syn_config=None):
    # synthesize_wav sets the WAV format (sample rate, 16-bit mono) and writes the audio itself.
    with wave.open(str(path), "wb") as wav_file:
        voice.synthesize_wav(text, wav_file, syn_config=syn_config)


def main():
    # load() needs the .onnx.json config next to the model, so check for both.
    config_path = MODEL_PATH.with_suffix(".onnx.json")
    if not MODEL_PATH.exists() or not config_path.exists():
        sys.exit(
            f"Voice model not found: {MODEL_PATH}\n"
            f"Download it with:\n"
            f"    python -m piper.download_voices --data-dir \"{MODEL_PATH.parent}\" {VOICE_NAME}"
        )

    voice = PiperVoice.load(MODEL_PATH)

    # Default settings.
    synthesize_to_wav(voice, "Hello! This is Piper, a local neural text to speech engine.", OUTPUT_PATH)
    print(f"Saved speech to {OUTPUT_PATH}")

    # SynthesisConfig tweaks how the voice sounds:
    #   length_scale > 1.0 slows speech down (2.0 is twice as slow), < 1.0 speeds it up
    #   volume scales loudness (0.5 is half as loud)
    slow_config = SynthesisConfig(length_scale=1.4, volume=0.8)
    synthesize_to_wav(voice, "This sentence is spoken more slowly.", OUTPUT_PATH, syn_config=slow_config)

    # voice.synthesize(text) also exists: it yields audio chunks (one per sentence) with
    # sample_rate, sample_width, sample_channels and audio_int16_bytes,
    # which is useful for streaming audio to a sound device instead of a file.

    if sys.platform == "win32":
        import winsound

        winsound.PlaySound(str(OUTPUT_PATH), winsound.SND_FILENAME)


if __name__ == "__main__":
    main()
