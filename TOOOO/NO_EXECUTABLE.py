import time
import subprocess
import time
import requests
from stem import Signal
from stem.control import Controller
import requests
import uuid
import random
import json
import string
from bs4 import BeautifulSoup
import json
import re
import hashlib
import secrets
import os
import sys
import pygetwindow
from pygetwindow import getWindowsWithTitle
import psutil

executable_dir = os.path.dirname(sys.executable)
fake_useragent = ''
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
tara = 'ro'

TOR_PROXY = "socks5://127.0.0.1:9050"
url = f"https://{tara}.grepolis.com/glps/registration"
PATH_TOR = r"D:\pythonProject\TOOOO\BOT_DK\AM\Tor Browser\Browser\TorBrowser\Tor\tor.exe"
tor_process = subprocess.Popen([PATH_TOR])
time.sleep(5)
PATH_TOR_BROWSER = r"D:\pythonProject\TOOOO\BOT_DK\AM\Tor Browser\Browser\firefox.exe"
tor_browser_process = subprocess.Popen([PATH_TOR_BROWSER])
time.sleep(5)

# Obține fereastra după nume sau alt criteriu specific
tor_browser_window = getWindowsWithTitle("Tor Browser")[0]

# Minimizează fereastra sau ascunde-o
tor_browser_window.hide()
time.sleep(10)
player_id = None
country='ro'
# Obține directorul în care se află executabilul

# Concatenează numele fișierului cu directorul executabilului
file_path = r"BIBLOS3.txt"

if not os.path.isfile(file_path):
    # Creează fișierul dacă nu există
    with open(file_path, "w") as file:
        file.write("")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def generate_cid_with_10_numbers():
    cid = uuid.uuid4()
    cid_str = f"cid={cid}"

    # Generăm 10 cifre aleatoare și le adăugăm la sfârșit
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    cid_with_10_numbers = cid_str + random_numbers

    return cid_with_10_numbers


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_current_ip():
    headers = {'User-Agent': UserAgent}
    response = requests.get('https://ident.me', proxies={'https': TOR_PROXY}, headers=headers)
    return response.text


def write_ip_to_file(ip_address):
    with open(file_path, "a") as file:
        file.write(f"{ip_address}\n")


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        time.sleep(10)  # Așteaptă pentru a permite schimbarea IP-ului
        current_ip = get_current_ip()
        print(f"Your IP is: {current_ip} || User Agent is: {headers1['User-Agent']}")
        write_ip_to_file(current_ip)


def generate_random_text(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_cookie():
    common_prefix = 'GA1.2.'
    random_suffix = ''.join(str(random.randint(1000000000, 1999999999)) for _ in range(3))
    unique_suffix = str(random.randint(1000000000, 1999999999))


while True:
    TOR_PROXY = "socks5://127.0.0.1:9050"
    session = requests.Session()
    session.proxies = {'http': TOR_PROXY, 'https': TOR_PROXY}
    print(session.proxies)

    text_length = 16
    user = generate_random_text(text_length)
    password = secrets.token_hex(16)

    try:

        payload_registration = {
            'registration[nickname]': user,
            'registration[password]': password,
            'registration[acceptTerms]': '1',
            'registration[email]': f'{user}@yahoo.com',
            'registration[accepted3rdPartyPixels]': '0'
        }
        payload_json = json.dumps(payload_registration)
        content_length = len(payload_json)
        response = session.post(url, data=payload_registration)
        TOKEN = response.cookies.get("XSRF-TOKEN")
        PHP = response.cookies.get("PHPSESSID")  #
        device_view = response.cookies.get("device_view")
        metricsUvId = str(uuid.uuid4())
        metrics = metricsUvId
        prefix_random_part = random.randint(10 ** 12, 10 ** 13 - 1)
        portal_tid_random_part = random.randint(10000, 99999)
        portal_tid = f"{prefix_random_part}-{portal_tid_random_part}"
        portal_data = f"{portal_tid}={portal_tid}"
        CookieNotification = "0"
        town_id = None
        # ress=None
        player_id = None
        # hash_value=None
        world_id_value='ro101'
        # redirect_url = None
        csrf_token = None

        headers1 = {
            "authority": f'{tara}.grepolis.com',
            "method": 'POST',
            "path": '/glps/registration',
            "scheme": 'https',
            "Accept": 'application/json, text/plain, */*',
            "Accept-Encoding": 'gzip, deflate, br',
            "Accept-Language": 'en-GB,en;q=0.8',
            "Content-Length": str(content_length),
            "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
            "Cookie": f'PHPSESSID={PHP}; XSRF-TOKEN={TOKEN}; device_view={device_view}; metricsUvId={metricsUvId}; portal_tid={portal_tid}; portal_data={portal_data}; CookieNotification={CookieNotification}',
            "Origin": 'https://ro.grepolis.com/',
            "Referer": 'https://ro.grepolis.com',
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "firefox";v="120"',
            "Sec-Ch-Ua-Mobile": '?0',
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": 'empty',
            "Sec-Fetch-Mode": 'cors',
            "Sec-Fetch-Site": 'same-origin',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Requested-With": 'XMLHttpRequest',
            "X-Xsrf-Token": TOKEN,
        }
        response1 = session.post(url, data=payload_registration, headers=headers1)

        if response1.status_code == 200:
            print("Cerere reușită!")
        else:
            print(f"Eroare în timpul cererii: {response1.status_code}")
            tor_process.terminate()
            tor_process.wait()
            tor_process = subprocess.Popen([PATH_TOR])
            with open(file_path, "r") as file:
                lines = file.readlines()

            if lines:
                lines.pop()

                with open(file_path, "w") as file:
                    file.writelines(lines)
            else:
                print("Fișierul este gol.")
            renew_tor_ip()
        try:
            parsed_response = json.loads(response1.text)
            redirect_url = parsed_response.get("redirect_url", "")
            print("REDIRECT URL",redirect_url)
            # print("URL-ul de redirecționare este:", redirect_url)
            ress = session.get(redirect_url)

            pattern = r'"townId":(\d+)'
            matches = re.findall(pattern, ress.text)
            # Verificați dacă există potriviri și afișați rezultatul
            if matches:
                town_id = matches[0]
                # print("townId:", town_id)
            else:
                print("townID nu a fost găsit în text.")

            pattern_player_id = r'"player_id":(\d+)'
            matches_player_id = re.findall(pattern_player_id, ress.text)
            if matches_player_id:
                player_id = matches_player_id[0]
                # print("Player ID:", player_id)
            else:
                print("Player ID nu a fost găsit în text.")

            # Extrageți hash

            hash_value = parsed_response.get('redirect_url', '').split('&hash=')[1].split('&')[
                0] if 'redirect_url' in parsed_response else None
            print(hash_value)
            # Verifică dacă hash-ul a fost găsit și afișează rezultatul
            # if hash_value:
            #     print("Hash:", hash_value)
            # else:
            #     print("Hash nu a fost găsit în răspuns.")

            world_id_value = parsed_response.get('redirect_url', '').split('&world_id=')[1].split('&')[
                0] if 'redirect_url' in parsed_response else None
            print("World_id_value",world_id_value)
            # Verifică dacă world_id a fost găsit și afișează rezultatul
            # if world_id_value:
            #     print("World ID:", world_id_value)
            # else:
            #     print("World ID nu a fost găsit în răspuns.")
            world_id_value='ro101'
            payload_loghin = {
                'action': 'login_from_glps',
                'player_id': player_id,
                'hash': f'{hash_value}',
                'world_id': f'{world_id_value}'
            }
            with open(file_path, "a") as file:
                file.write(f"{country} User: {user}, Password: {password}, player_id: {player_id}, hash: {hash_value}, world_id: {world_id_value}\n")
            headers_loghin = {
                "authority": f'{tara}.grepolis.com',
                "method": 'POST',
                "path": f'/?action=login_from_glps&player_id={player_id}&hash={hash_value}&world_id={world_id_value}',
                "scheme": 'https',
                "Accept": 'application/json, text/plain, */*',
                "Accept-Encoding": 'gzip, deflate, br',
                "Accept-Language": 'en-GB,en;q=0.8',
                "Content-Length": str(content_length),
                "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                "Cookie": f'PHPSESSID={PHP}; XSRF-TOKEN={TOKEN}; device_view={device_view}; metricsUvId={metricsUvId}; portal_tid={portal_tid}; portal_data={portal_data}; CookieNotification={CookieNotification}',
                "Origin": f'https://{tara}.grepolis.com',
                "Referer": f'https://{tara}.grepolis.com/',
                "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "firefox";v="120"',
                "Sec-Ch-Ua-Mobile": '?0',
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "X-Requested-With": 'XMLHttpRequest',
                "X-Xsrf-Token": TOKEN,
            }
            response_login = session.post(redirect_url, payload_loghin, headers_loghin)
            # print("RESPONSE_LOGIN",response_login.text)

            session.get(redirect_url)
            sid = str(session.cookies['sid'])
            # print("COOOK:",session.cookies)
            login_startup_time = str(session.cookies['login_startup_time'])
            pid = session.cookies.get('pid', 'default_value')
            toid = session.cookies.get('toid', 'default_value')

            # print("LOGIN_STARTUP_TIME", login_startup_time)
            # print('PID', pid)
            # print("TOID",toid)
            # print("SID",sid)

            csrf_token_pattern = re.compile(r'"csrfToken":"([^"]+)"')
            match = csrf_token_pattern.search(response_login.text)

            if match:
                csrf_token = match.group(1)
                # print("csrfToken:", csrf_token)
            else:
                print("csrfToken nu a fost găsit în script.")

            current_timestamp = int(time.time())

            # print("Timestamp curent:", current_timestamp)

            PAYLOAD_TOVARAS2 = {
                'login': 1,
                'p': player_id,
                'ts': current_timestamp,
            }

            TOVARAS2 = {
                "authority": f'{tara}.grepolis.com',
                "method": 'POST',
                "path": f'/game/index?login=1&p={player_id}&ts={current_timestamp}',
                "scheme": 'https',
                "Accept": 'application/json, text/plain, */*',
                "Accept-Encoding": 'gzip, deflate, br',
                "Accept-Language": 'en-GB,en;q=0.8',
                "Content-Length": '50',
                "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                "Cookie": f'metricsUvId={metrics};_gid={"GA1.2." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}; toid={toid};cid={generate_cid_with_10_numbers()}; logged_in=false; ig_conv_last_site=https://{world_id_value}.grepolis.com/game/index; _ga={"GA1.2." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}; _gat_UA-6635454-10=1; _ga_6WS52Q38JB={"GS1.1." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))};login_startup_time={login_startup_time};sid={sid};',
                "Origin": f'https://{world_id_value}.grepolis.com',
                "Referer": f'https://{world_id_value}.grepolis.com',
                "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "firefox";v="120"',
                "Sec-Ch-Ua-Mobile": '?0',
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "X-Requested-With": 'XMLHttpRequest',
            }

            current_timestamp = int(time.time())
            url5 = f"https://{world_id_value}.grepolis.com/game/index?login=1&p={player_id}&ts={current_timestamp}"
            response5 = session.get(url5, data=PAYLOAD_TOVARAS2, headers=TOVARAS2)
            # print("RESPONSE5:", response5.text)

            csrf_token_pattern = re.compile(r'"csrfToken":"([^"]+)"')
            match = csrf_token_pattern.search(response5.text)

            if response5.status_code == 200:
                print("RESPONSE5 CU 200!!!!!")
            else:
                print("Nu e raspuns 200!")

            if match:
                csrf_token = match.group(1)
                # print("csrfToken 5:", csrf_token)
            else:
                print("csrfToken nu a fost găsit în script.")

            payload_vacantion = {
                'town_id': town_id,
                'action': 'start_vacation',
                'h': f'{csrf_token}',
            }

            headers_vacantion = {
                "authority": f'{tara}.grepolis.com',
                "method": 'POST',
                "path": f'/game/player?town_id={town_id}&action=start_vacation&h={csrf_token}',
                "scheme": 'https',
                "Accept": 'application/json, text/plain, */*',
                "Accept-Encoding": 'gzip, deflate, br',
                "Accept-Language": 'en-GB,en;q=0.8',
                "Content-Length": str(content_length),
                "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                "Cookie": f'cid={generate_cid_with_10_numbers()}; metricsUvId={metrics}; toid={toid}; ig_conv_last_site=https://{world_id_value}.grepolis.com/game/index; _gid={"GA1.2." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}; sid={sid}; logged_in=false; _ga={"GA1.2." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}; _gat_UA-6635454-10=1; _ga_6WS52Q38JB={"GS1.1." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}',
                "Origin": f'https://{world_id_value}.grepolis.com',
                "Referer": f'https:/{world_id_value}.grepolis.com',
                "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "firefox";v="120"',
                "Sec-Ch-Ua-Mobile": '?0',
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "X-Requested-With": 'XMLHttpRequest',
            }

            url2 = f"https://{world_id_value}.grepolis.com/game/player?town_id={town_id}&action=start_vacation&h={csrf_token}"
            response2 = session.post(url2, data=payload_vacantion, headers=headers_vacantion)
            print("RESPONSE2:", response2.text)
            response_json = response2.text

            parsed_response = json.loads(response_json)
            verification_code = parsed_response['json']['gpVerificationRequest']
            parsed_response = json.loads(verification_code)
            verification_code1 = parsed_response['code']

            payload_vacantion_confirmation = {
                'town_id': town_id,
                'action': 'start_vacation',
                'h': f'{csrf_token}',
                'json': json.dumps({"town_id": town_id, "nl_init": True, 'verification_code': verification_code1})}

            response3 = session.post(url2, data=payload_vacantion_confirmation, headers=headers_vacantion)
            print("RESPONSE3:", response3.text)

            ###################################################BUILD###################################################################

            PAYLOAD_BUILD = {
                'town_id': town_id,
                'action': 'execute',
                'h': f'{csrf_token}',
                'json': json.dumps(
                    {"model_url": "BuildingOrder", "action_name": "buildUp", "arguments": {"building_id": "stoner"},
                     "town_id": town_id, "nl_init": True})
            }

            HEADER_BUILD = {
                "authority": f'{tara}.grepolis.com',
                "method": 'POST',
                "path": f'/game/frontend_bridge?town_id={town_id}&action=execute&h={csrf_token}',
                "scheme": 'https',
                "Accept": 'application/json, text/plain, */*',
                "Accept-Encoding": 'gzip, deflate, br',
                "Accept-Language": 'en-GB,en;q=0.8',
                "Content-Length": str(content_length),
                "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                "Cookie": f'metricsUvId={metrics}; _gid={"GA1.2." + str(random.randint(1000000000, 1999999999)) + "." + str(random.randint(1000000000, 1999999999))}; cid={generate_cid_with_10_numbers()}; toid={toid}; logged_in=false; ig_conv_last_site=https://{world_id_value}.grepolis.com/game/index; sid={sid}; _ga=GA1.1.1535526168.1649862981; _ga_6WS52Q38JB=GS1.1.1704470030.36.1.1704470584.0.0.0',
                "Origin": f'https://{world_id_value}.grepolis.com',
                "Referer": f'https://{world_id_value}.grepolis.com',
                "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "firefox";v="120"',
                "Sec-Ch-Ua-Mobile": '?0',
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "X-Requested-With": 'XMLHttpRequest',
            }
            URL_BUILD = f"https://{world_id_value}.grepolis.com/game/frontend_bridge?town_id={town_id}&action=execute&h={csrf_token}"
            response_build = session.post(URL_BUILD, data=PAYLOAD_BUILD, headers=HEADER_BUILD)
            print("RESPONSE BUILD:", response_build.text)

        except:
            print("EROARE 500!")
    except:
        print("Inchide fisierul in 15 secunde pentru ca incerc sa-mi fac TREABA!")
        time.sleep(15)
    finally:
        print("Bye")
