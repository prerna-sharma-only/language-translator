from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

def translate_text(text, source, target):
    try:
        translator = GoogleTranslator(source=source or "auto", target=target)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print("Error:", e)
        return "Translation error"


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        text = request.form.get("text")
        source = request.form.get("source")
        target = request.form.get("target")

        if text:
            result = translate_text(text, source, target)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)