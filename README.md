# Werkplaats 4 - Inhaalopdracht - _fietsindicator_

Dit is een configuratie app waarmee je omgevingen/apps kan toevoegen aan een sqllite database. Je moet hierbij inloggen. Als je geen account hebt kan een account maken op de website. Je account word geregistreerd in de database. Nadat je je geregistreerd hebt kan je jezelf inloggen. Inloggen kan niet geschieden zonder account. Nadat je bent ingelogd kom je op de homepagina. Op de homepagina wordt automatisch alle geregistreerde gegevens uit de database weergegeven door middel van een AJAX call. Om de 5 seconden word de pagina automatisch ververst. Op deze manier krijg je direct de nieuwe toegevoegde apps te zien. Links boven heb je een bar met een knop voor het uitloggen en toevoegen van een nieuwe app. Zodra je op de: "Add new app" klikt, kom je op een nieuwe scherm waarbij je de volgende gegevens kan invoeren: Name, Environments, IP, Pincode. Nadat je dit hebt gedaan en op submit klikt, kom je bij een "succes" scherm. Hierna zal je kunnen klikken op een knop die ervoor zorgt dat je weer bij de homepage terecht komt. 

Developer: Bünyamin E. Bölükbas
Studentnr: 1058754

## Opdracht

Story 1: Als gebruiker wil ik een nieuwe applicatie kunnen toevoegen, met een naam
en een IP filter
- Maak HTML / jinja met een formulier voor het applicatiescherm
- Voeg mockup (=platte HTML) toe voor het blok omgevingen / bestanden en het blok
logging - Voeg een tabel toe voor applicaties in de database
- Maak een Flask route (/application/<id>) om een bestaande applicatie uit de database op
te vragen.
- Maak een Flask route (een POST naar /application/<id>) om een nieuwe applicatie op te
slaan of een bestaande te wijzigen.
Story 2: Als gebruiker wil ik op het applicatie scherm nieuwe omgeving labels
kunnen toevoegen en “bestanden” aan een omgeving kunnen toevoegen
- Voeg een tabel voor omgevingen toe aan de database. Deze moeten verwijzen naar de
tabel met applicaties.
- Voeg een knop “Nieuwe omgeving” en een lijst met “Omgevingen” toe aan het
applicatiescherm
- Maak een route (POST /application/<id>/omgevingen>) om een nieuwe omgeving op te
slaan. Deze gaat na opslaan terug naar het applicatiescherm
- Voeg een tabel voor bestanden toe aan de database. Deze moeten verwijzen naar de tabel
met omgevingen.
- Maak een route (/application/<id>/omgevingen/<omgeving_id>) om het scherm voor een
nieuw bestand te openen
- Maak een route (POST /application/<id>/omgevingen/<omgeving_id>) om een nieuw
bestand op te slaan bij een applicatie en zijn omgeving. Na opslaan mag het
applicatiescherm weer geopend worden.
Story 3: Als gebruiker wil ik beginnen met een scherm met alle applicaties, nadat ik
ben ingelogd
- Maak HTML / jinja met een scherm met alle applicaties erop en een knop om een nieuwe
applicatie aan te maken
- Maak een route (/applicaties) die dit scherm toont
- Maak een loginscherm in HTML
- Maak een tabel in de database voor gebruikersnamen en wachtwoorden
- Maak een route (“/”) die controleert of de gebruiker is ingelogd. Zo niet, toon het
loginscherm. Zo wel, stuur de gebruiker door naar /applicaties

## vereisten

Python (version 3.12.0) https://www.python.org/downloads/ (Please note, when installing python, make sure to check the "Add python.exe to PATH") </br>
Git (version 2.44.0) https://git-scm.com/downloads<br>
Flask pip install
Virtual environment (env/venv/virtualenv)

## Installatie

Om Flask te kunnen starten zul je eerst de Flask packages moeten installeren. Wil je latere problemen met versies voorkomen, dan raden we je aan een virtual environment te maken en daar de modules in te installeren:

pip install virtualenv
virtualenv venv
.\venv\scripts\activate
pip install -r requirements.txt

## Referenties

Voor het inloggen van de applicatie moet je jezelf eerst registreren. Dit doe je door op de knop ''Register'' te klikken. Hierna kan je een accountnaam en wachtwoord kiezen waarmee je vervolgens kan inloggen.

## Gebruik

1: log in bij de loginpagina
2: klik op add new app
3: voer gegevens in van:
Name
Environments
IP
Pincode
4: klik op submit
5: klik op: return home
6: logout

## Bronnen

* Github repo addres: https://github.com/Rac-Software-Development/werkplaats-3---inhaalopdracht-Bunyamin-1058754/activity?after=djE6ks8AAAAEGrL_HwA
* https://getbootstrap.com/docs/5.3/getting-started/javascript/
* https://chat.openai.com/

## Ai gebruik

Heb gebruik gemaakt van ChatGPT + Github Co-pilot voor het formatteren van de code van de volgende bestanden:
- app.py
- home.html
- login.html
- result.html
- register



## Versie historie

Repository aangemaakt: 07-06-2023
Product version 1.1 opgeleverd: 20-03-2024