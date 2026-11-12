import json
import urllib.request

urls = [
    "https://apps.altstore.io",
    "https://apps.sidestore.io/",
    "https://connect.sidestore.io/apps.json",
    "https://qnblackcat.github.io/AltStore/apps.json",
    "https://repository.apptesters.org",
    "https://ipa.cypwn.xyz/cypwn.json",
    "https://ipa.cypwn.xyz/cypwn_ts.json",
    "https://wuxu1.github.io/wuxu-complete.json",
    "https://wuxu1.github.io/wuxu-complete-plus.json",
    "https://fastsign.dev/repo.json",
    "https://raw.githubusercontent.com/khcrysalis/Feather/raw/main/app-repo.json",
    "https://raw.githubusercontent.com/Neoncat-OG/TrollStore-IPAs/main/apps_esign.json",
    "https://raw.githubusercontent.com/swaggyP36000/TrollStore-IPAs/main/apps_esign.json",
    "https://binnichtaktiv.signapp.me/repo/esign.json",
    "https://esign.yyyue.xyz/app.json",
    "https://repo.whoeevee.com/esign",
    "https://repo.zsign.app/repo.json",
    "https://aio.yippee.rip/repo.json",
    "https://balackburn.github.io/Apollo/apps.json",
    "https://cranci.tech/repo.json",
    "https://flyinghead.github.io/flycast-builds/altstore.json",
    "https://raw.githubusercontent.com/lo-cafe/winston-altstore/main/apps.json",
    "https://madari.media/nightly/repo.json",
    "https://raw.githubusercontent.com/AntonP29/AntonP29-Repo/refs/heads/main/repo.json",
    "https://raw.githubusercontent.com/Balackburn/YTLitePlusAltstore/main/apps.json",
    "https://raw.githubusercontent.com/vizunchik/AltStoreRus/master/apps.json",
    "https://repo.starfiles.co",
    "https://repos.yattee.stream/alt/apps.json",
    "https://xitrix.github.io/iTorrent/AltStore.json",
    "https://raw.githubusercontent.com/arichorn/arichorn.github.io/main/apps.json",
    "https://raw.githubusercontent.com/arichornlover/arichornlover.github.io/main/apps.json",
    "https://raw.githubusercontent.com/burrito-software/altstore/main/apps.json",
    "https://raw.githubusercontent.com/therealFoxster/altsource-viewer/main/apps.json",
    "https://raw.githubusercontent.com/BandarHL/BHTwitter/main/altstore.json",
    "https://raw.githubusercontent.com/FouadRaheb/Watusi-for-WhatsApp/main/altstore.json",
    "https://raw.githubusercontent.com/Mila432/BHTwitter/main/altstore.json",
    "https://raw.githubusercontent.com/level3tjg/BHTwitter/main/altstore.json",
    "https://github.com/hieplpvip/BHTwitter/raw/main/altstore.json",
    "https://raw.githubusercontent.com/EamonTracey/EamonTracey.github.io/master/altstore.json",
    "https://raw.githubusercontent.com/drbh/altstore-repo/master/apps.json",
    "https://raw.githubusercontent.com/SnailiOS/SnailiOS.github.io/main/apps.json",
    "https://raw.githubusercontent.com/LukeZGD/LukeZGD.github.io/main/apps.json",
    "https://quarksources.github.io/quarksources.json",
    "https://raw.githubusercontent.com/CokePokes/CokePokes.github.io/master/apps.json"
]

merged_apps = []
seen_bundles = set()

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            apps = data.get('apps', [])
            for app in apps:
                # Filter biar gak duplikat berdasarkan bundleIdentifier + version
                uid = f"{app.get('bundleIdentifier')}_{app.get('version')}"
                if uid not in seen_bundles and app.get('downloadURL'):
                    seen_bundles.add(uid)
                    merged_apps.append(app)
    except Exception as e:
        print(f"Skip {url}: {e}")

mega_repo = {
    "name": "Ghan Mega IPA Repo",
    "identifier": "com.ghan.megarepo",
    "subtitle": "All-in-One Merged Repo",
    "description": "Auto-merged IPA repository",
    "apps": merged_apps
}

with open("repo.json", "w", encoding="utf-8") as f:
    json.dump(mega_repo, f, indent=2)

print(f"Total apps merged: {len(merged_apps)}")
