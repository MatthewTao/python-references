from nicegui import ui

def speak(text):
    ui.run_javascript(f'''
        const utterance = new SpeechSynthesisUtterance("{text}");
        speechSynthesis.speak(utterance);
    ''')

ui.button('Speak', on_click=lambda: speak('Hello from NiceGUI!'))

ui.run()
