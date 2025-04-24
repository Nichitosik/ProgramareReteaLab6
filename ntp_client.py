import ntplib
from datetime import datetime, timedelta
import time


def get_ntp_time():
    """Obține ora exactă de la un server NTP."""
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3)
        # Convertim timpul NTP în format datetime (UTC)
        ntp_time = datetime.fromtimestamp(response.tx_time)
        return ntp_time
    except Exception as e:
        print(f"Eroare la obținerea orei NTP: {e}")
        return None


def get_local_time(ntp_time):
    """Obține ora locală bazată pe fusul orar al sistemului."""
    if ntp_time is None:
        return None
    # Ajustăm pentru fusul orar local
    local_offset = time.localtime().tm_gmtoff / 3600  # Offset în ore
    local_time = ntp_time + timedelta(hours=local_offset)
    return local_time


def parse_timezone(timezone_str):
    """Parsează fusul orar din formatul 'GMT+X' sau 'GMT-X'."""
    try:
        # Verifică formatul
        if not (timezone_str.startswith("GMT+") or timezone_str.startswith("GMT-")):
            raise ValueError("Formatul trebuie să fie 'GMT+X' sau 'GMT-X'")

        # Extrage offset-ul
        offset_str = timezone_str[3:]  # Scoate 'GMT'
        offset = int(offset_str)

        # Verifică intervalul valid (0-11)
        if not (0 <= abs(offset) <= 11):
            raise ValueError("Offset-ul trebuie să fie între 0 și 11")

        # Returnează offset-ul (pozitiv sau negativ)
        return offset if timezone_str.startswith("GMT+") else -offset
    except ValueError as e:
        print(f"Eroare: {e}")
        return None


def get_timezone_time(ntp_time, offset):
    """Calculează ora pentru fusul orar specificat."""
    if ntp_time is None or offset is None:
        return None
    return ntp_time + timedelta(hours=offset)


def main():
    """Funcția principală a aplicației."""
    print("=== Client NTP ===")

    # Cere fusul orar
    timezone_str = input("Introdu fusul orar (ex. GMT+2, GMT-5): ")
    offset = parse_timezone(timezone_str)

    if offset is None:
        print("Fus orar invalid. Programul se închide.")
        return

    # Obține ora NTP
    ntp_time = get_ntp_time()
    if ntp_time is None:
        print("Nu s-a putut obține ora exactă. Verifică conexiunea la internet.")
        return

    # Obține ora locală
    local_time = get_local_time(ntp_time)

    # Obține ora în fusul orar specificat
    timezone_time = get_timezone_time(ntp_time, offset)

    # Afișează rezultatele
    print("\nRezultate:")
    print(f"Ora exactă UTC: {ntp_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Ora locală: {local_time.strftime('%Y-%m-%d %H:%M:%S')} (GMT{time.localtime().tm_gmtoff // 3600:+d})")
    print(f"Ora în {timezone_str}: {timezone_time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
