https://github.com/Nichitosik/ProgramareReteaLab6.git
Laborator 6: Aplicație Client NTP
Descriere
Aceasta este o aplicație de consolă dezvoltată în Python pentru Laboratorul 6 de Programare în Rețea. Aplicația utilizează protocolul NTP (Network Time Protocol) pentru a obține ora exactă de la un server NTP (pool.ntp.org) și afișează:

Ora exactă în UTC.
Ora exactă locală (bazată pe fusul orar al sistemului).
Ora exactă pentru un fus orar specificat de utilizator, în formatul „GMT+X” sau „GMT-X” (unde X este între 0 și 11).

Aplicația demonstrează înțelegerea protocolului NTP, obținerea orei locale și calcularea orei pentru o altă zonă geografică.
Obiective

Înțelegerea modului în care funcționează protocolul NTP pentru obținerea orei exacte.
Obținerea și afișarea orei locale exacte, ajustată pentru fusul orar al sistemului.
Calcularea și afișarea orei exacte pentru un fus orar specificat de utilizator.

Cerințe

Python 3.8 sau mai nou (testat cu Python 3.9).
Biblioteca ntplib (instalată în mediul virtual).
Sistem de operare: macOS (testat), compatibil și cu Linux/Windows.
Conexiune la internet pentru accesarea serverului NTP.

Instalare

Clonați repository-ul:
git clone https://github.com/Nichitosik/ProgramareReteaLab6.git
cd ProgramareReteaLab6


Creați un mediu virtual:
python3 -m venv .venv
source .venv/bin/activate


Instalați dependințele:
pip install ntplib



Cum se rulează
Din Terminal

Navigați în directorul proiectului:
cd /Users/<username>/PycharmProjects/ProgramareReteaLab6


Activați mediul virtual:
source .venv/bin/activate


Rulați aplicația:
python ntp_client.py


Interacționați cu aplicația:

Introdu un fus orar valid (ex. GMT+2, GMT-5).
Aplicația va afișa:
Ora exactă UTC.
Ora locală (cu offset-ul sistemului).
Ora în fusul orar specificat.


Exemplu de output:=== Client NTP ===
Introdu fusul orar (ex. GMT+2, GMT-5): GMT+2

Rezultate:
Ora exactă UTC: 2025-04-24 12:34:56
Ora locală: 2025-04-24 14:34:56 (GMT+2)
Ora în GMT+2: 2025-04-24 14:34:56





Din PyCharm

Deschideți proiectul:

Mergi la File > Open și selectează /Users/<username>/PycharmProjects/ProgramareReteaLab6.


Configurați interpretorul:

Mergi la PyCharm > Preferences > Project: ProgramareReteaLab6 > Python Interpreter.
Apasă pe rotița dințată (⚙️) și selectează Add Interpreter > Existing environment.
Alege /Users/<username>/PycharmProjects/ProgramareReteaLab6/.venv/bin/python.
Apasă OK.


Instalați ntplib:

În fereastra Python Interpreter, apasă +, caută ntplib, și apasă Install Package.


Rulați aplicația:

Deschide ntp_client.py în PyCharm.
Apasă butonul „Run” (triunghi verde) sau mergi la Run > Run 'ntp_client'.
Introdu un fus orar în consola PyCharm și verifică output-ul.



Observații la rulare

Conexiune la internet: Necesită acces la serverul NTP (pool.ntp.org). Dacă nu este disponibil, aplica

