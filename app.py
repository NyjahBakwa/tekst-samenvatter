import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from google import genai

load_dotenv()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # uploads max 1 MB

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

OPDRACHTEN = {
    "kort": "Vat de tekst samen in maximaal drie zinnen.",
    "hoofdpunten": "Geef de belangrijkste punten van de tekst als een lijst met streepjes (maximaal 7 punten).",
    "uitgebreid": "Maak een duidelijke samenvatting van de tekst in een paar alinea's.",
    "actiepunten": "Haal alle actiepunten, taken en deadlines uit de tekst en zet ze in een lijst met streepjes. Staan er geen actiepunten in, zeg dat dan.",
}


def maak_samenvatting(tekst, soort):
    prompt = (
        f"{OPDRACHTEN[soort]} Schrijf in het Nederlands, "
        "ook als de tekst in een andere taal is.\n\n"
        f"Tekst:\n{tekst}"
    )
    antwoord = client.models.generate_content(model=MODEL, contents=prompt)
    return antwoord.text


@app.route("/", methods=["GET", "POST"])
def index():
    tekst = ""
    soort = "kort"
    samenvatting = None
    fout = None

    if request.method == "POST":
        tekst = request.form.get("tekst", "").strip()
        soort = request.form.get("soort", "kort")
        bestand = request.files.get("bestand")

        if bestand and bestand.filename:
            if bestand.filename.lower().endswith(".txt"):
                tekst = bestand.read().decode("utf-8", errors="ignore").strip()
            else:
                fout = "Alleen .txt-bestanden worden ondersteund."

        if soort not in OPDRACHTEN:
            soort = "kort"

        if not fout and not tekst:
            fout = "Plak een tekst of upload een .txt-bestand."
        elif not fout and len(tekst.split()) < 30:
            fout = "De tekst is te kort om samen te vatten (minimaal 30 woorden)."

        if not fout:
            try:
                samenvatting = maak_samenvatting(tekst, soort)
            except Exception as e:
                fout = f"Er ging iets mis met de AI: {e}"

    return render_template(
        "index.html",
        tekst=tekst,
        soort=soort,
        samenvatting=samenvatting,
        fout=fout,
        aantal_woorden=len(tekst.split()),
    )


if __name__ == "__main__":
    app.run(debug=True)
