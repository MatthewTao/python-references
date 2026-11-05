# pyttsx3: offline text-to-speech that uses the voices already installed in the OS.
#   - Windows: SAPI5 (Microsoft David, Zira, ...)
#   - macOS: NSSpeechSynthesizer
#   - Linux: eSpeak
# No network or model download needed, but voice quality is only as good as the OS voices.
#
# Install: pip install pyttsx3

import time

import pyttsx3


def speak(engine, text):
    # With an external event loop (startLoop(False)), queuing text with say()
    # does not block. Driving iterate() until the engine stops being busy is
    # what actually pumps the speech, so each call here speaks synchronously.
    engine.say(text)
    while engine.isBusy():
        engine.iterate()
        time.sleep(0.05)


def main():
    # Creates the engine for the current platform's speech driver.
    engine = pyttsx3.init()

    # Starts pyttsx3's external event loop instead of using runAndWait().
    # We drive the loop ourselves via iterate() inside speak().
    engine.startLoop(False)
    try:
        # Prime the iterator once before any speech is queued.
        engine.iterate()

        # say() queues the text; speak() pumps iterate() until it is spoken.
        speak(engine, "Hello! This is pyttsx3 speaking with the default voice.")

        # Voices installed on this machine. The id is what you pass back to setProperty.
        voices = engine.getProperty("voices")
        for voice in voices:
            print(f"id={voice.id}  name={voice.name}")
            engine.setProperty("voice", voice.id)
            speak(engine, f"I am speaking with the {voice.name} voice.")

        # rate is words per minute (the typical default is about 200);
        # volume is a float from 0.0 to 1.0.
        rate = engine.getProperty("rate")
        volume = engine.getProperty("volume")
        print(f"Current rate={rate}, volume={volume}")

        engine.setProperty("rate", rate - 50)  # slower speech
        engine.setProperty("volume", 0.7)  # a bit quieter
        speak(engine, "Now I am speaking more slowly and more quietly.")
    finally:
        engine.endLoop()


if __name__ == "__main__":
    main()
