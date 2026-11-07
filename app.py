
import gradio as gr
import requests

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

def translate_text(text, source, target):

    if not text.strip():
        return "Please enter some text!"

    if source == target:
        return text

    url = "https://translate.googleapis.com/translate_a/single"

    params = {
        "client": "gtx",
        "sl": languages[source],
        "tl": languages[target],
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(
            url, params=params, timeout=20
        )
        response.raise_for_status()

        data = response.json()

        result = "".join(
            item[0] for item in data[0] if item[0]
        )

        return result

    except Exception as e:
        return f"Translation Error: {e}"


demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter Your Text"),
        gr.Dropdown(
            choices=list(languages.keys()),
            value="English",
            label="Source Language"
        ),
        gr.Dropdown(
            choices=list(languages.keys()),
            value="Hindi",
            label="Target Language"
        )
    ],
    outputs=gr.Textbox(label="Translated Text"),
    title="AI Language Translation Tool",
    description="Translate text between different languages."
)

demo.launch()
