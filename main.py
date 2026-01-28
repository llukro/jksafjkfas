import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent

SCROBBLERS = [
    "1okktubre.py",
    "2slimey.py",
    "christ_blunt.py",
    "corpsekyo.py",
    "elek.py",
    "giuliano.py",
    "helabrokeangel.py",
    "hellsing_glock_boyz.py",
    "kk.py",
    "knsevenkay.py",
    "moneynumb.py",
    "my_little_pony.py",
    "naxowo.py",
    "nekkropsy.py",
    "ocelot.py",
    "pistolero2k.py",
    "putrid.py",
    "sexadlibs.py",
    "slattuhs.py",
    "suban.py",
    "tnnn.py",
    "unixzo.py",
    "vampireosamagang666.py",
    "vritni.py",
    "war6aw.py",
    "xartinreligion.py",
    "xoly.py",
    "xtendo.py",
    "yoi.py",
    "young_piri.py",
    "zatru.py",
]

print("🚀 Launcher de scrobblers iniciado")

while True:
    for script in SCROBBLERS:
        path = BASE_DIR / script

        if not path.exists():
            print(f"❌ No existe: {script}")
            continue

        print(f"▶ Ejecutando {script}")
        try:
            subprocess.run([sys.executable, path], check=False)
        except Exception as e:
            print(f"💥 Error en {script}: {e}")

        print(f"✔ Finalizó {script}")
        time.sleep(5)

    print("🔁 Lista completa ejecutada. Reintentando en 60s")
    time.sleep(60)
