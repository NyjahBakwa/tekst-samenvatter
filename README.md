# Tekst-samenvatter

Een Flask-webapp die lange teksten samenvat met de Gemini API van Google. Je plakt een tekst of uploadt een `.txt`-bestand en kiest wat voor samenvatting je wilt. De AI antwoordt altijd in het Nederlands, ook als de tekst in een andere taal is.

## Soorten samenvatting

- **Kort**: maximaal drie zinnen
- **Hoofdpunten**: een lijst met de belangrijkste punten
- **Uitgebreid**: een samenvatting van een paar alinea's
- **Actiepunten en deadlines**: haalt taken en datums uit de tekst, handig voor notulen of een klantbriefing

## Wat ik heb geleerd

- Een AI-model aanroepen via een API vanuit Python
- Prompts schrijven die een vast soort antwoord opleveren
- Een bestand uploaden en uitlezen in Flask
- Invoer controleren voordat je die naar de API stuurt (lege of te korte tekst, verkeerd bestandstype)

## Gebruikte technieken

- Python / Flask
- Google Gemini API (`google-genai`)
- HTML, CSS, Jinja-templates

## Installeren

1. Maak een gratis API-sleutel aan op [Google AI Studio](https://aistudio.google.com/apikey).
2. Clone de repository en installeer de pakketten:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

3. Kopieer `.env.example` naar `.env` en vul je API-sleutel in.
4. Start de app:

```bash
python app.py
```

5. Open http://127.0.0.1:5000 in je browser.

## Model

Het model staat in `.env` (`GEMINI_MODEL`). Werkt het standaardmodel niet met je gratis sleutel, kies dan een ander Flash-model uit de lijst op [ai.google.dev](https://ai.google.dev/gemini-api/docs/models).
