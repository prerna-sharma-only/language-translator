from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

def translate_text(text, source, target):
    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return translated
    except:
        return "Translation error. Try again."


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