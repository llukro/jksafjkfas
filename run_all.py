import subprocess
import sys

scrobblers = [
    "scrobblers/1okktubre.py",
    "scrobblers/2slimey.py",
    "scrobblers/christ_blunt.py",
    "scrobblers/corpsekyo.py",
    "scrobblers/elek.py",
    "scrobblers/giuliano.py",
    "scrobblers/helabrokeangel.py",
    "scrobblers/hellsing_glock_boyz.py",
    "scrobblers/kk.py",
    "scrobblers/knsevenkay.py",
    "scrobblers/moneynumb.py",
    "scrobblers/my_little_pony.py",
    "scrobblers/naxowo.py",
    "scrobblers/nekkropsy.py",
    "scrobblers/ocelot.py",
    "scrobblers/pistolero2k.py",
    "scrobblers/putrid.py",
    "scrobblers/sexadlibs.py",
    "scrobblers/slattuhs.py",
    "scrobblers/suban.py",
    "scrobblers/tnnn.py",
    "scrobblers/unixzo.py",
    "scrobblers/vampireosamagang666.py",
    "scrobblers/vritni.py",
    "scrobblers/war6aw.py",
    "scrobblers/xartinreligion.py",
    "scrobblers/xoly.py",
    "scrobblers/xtendo.py",
    "scrobblers/yoi.py",
    "scrobblers/young_piri.py",
    "scrobblers/zatru.py",
]

processes = []

print("🚀 Lanzando todos los scrobblers...")

for path in scrobblers:
    p = subprocess.Popen(
        ["python3", path],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    processes.append(p)
    print(f"▶️ {path} iniciado")

for p in processes:
    p.wait()

print("✅ Todos los scrobblers terminaron")
sys.exit(0)