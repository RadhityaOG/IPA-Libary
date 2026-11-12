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
    "https://raw.githubusercontent.com/CokePokes/CokePokes.github.io/master/apps.json",
    "https://apps.nabzclan.vip/repos/altstore.php",
    "https://driftywinds.github.io/repos/esign.json",
    "https://dvntm0.github.io/AltStore/raw/refs/heads/main/esign.json",
    "https://raw.githubusercontent.com/Omni-Development/The-Omni-Repository/refs/heads/main/app-repo.json",
    "https://randomblock1.com/altstore/apps.json",
    "https://tweakrain.pages.dev/ios/altstore.json",
    "https://gbox.run/Public/Source.json",
    "https://raw.githubusercontent.com/Dan1elTheMan1el/Dan1elTheMan1el.github.io/main/repo.json",
    "https://raw.githubusercontent.com/ichitaso/ichitaso.github.io/master/altstore.json",
    "https://raw.githubusercontent.com/julioverne/julioverne.github.io/master/altstore.json",
    "https://raw.githubusercontent.com/yandevelop/yandevelop.github.io/main/apps.json",
    "https://ipa.aspy.dev/repo.json",
    "https://alt.getutm.app",
    "https://raw.githubusercontent.com/SpotC-Plus/SpotC-Plus.github.io/main/repo.json"
]

merged_apps = []
seen = set()
repo_base = "https://raw.githubusercontent.com/RadhityaOG/IPA-Libary/main"
default_icon = f"{repo_base}/IMG_6762.jpeg"

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            apps = data.get('apps', [])
            if not isinstance(apps, list):
                continue
            for app in apps:
                if not isinstance(app, dict):
                    continue
                bid = str(app.get('bundleIdentifier') or '').strip()
                ver = str(app.get('version') or '').strip()
                dl = str(app.get('downloadURL') or '').strip()
                name = str(app.get('name') or '').strip()

                if not (bid and ver and name and dl.startswith('http')):
                    continue
                if ' ' in dl:
                    continue

                uid = f"{bid}_{ver}"
                if uid in seen:
                    continue
                seen.add(uid)

                icon = str(app.get('iconURL') or '').strip()
                if not icon.startswith('http') or ' ' in icon:
                    icon = default_icon

                dev = str(app.get('developerName') or '').strip()
                if not dev:
                    dev = "Unknown"

                vdate = str(app.get('versionDate') or '').strip()
                if not vdate:
                    vdate = "2025-01-01"

                desc = str(app.get('localizedDescription') or '').strip()
                if not desc:
                    desc = "No description."

                raw_size = app.get('size', 0)
                try:
                    size = int(float(raw_size)) if raw_size else 0
                except Exception:
                    size = 0

                merged_apps.append({
                    "name": name,
                    "bundleIdentifier": bid,
                    "developerName": dev,
                    "version": ver,
                    "versionDate": vdate,
                    "downloadURL": dl,
                    "localizedDescription": desc,
                    "iconURL": icon,
                    "size": size
                })
    except Exception as e:
        print(f"Skip {url}: {e}")

mega_repo = {
    "name": "GHN - IPA Library",
    "identifier": "com.ghn.ipalibrary",
    "subtitle": "All-in-One Merged Repo",
    "description": "Auto-merged IPA repository",
    "iconURL": default_icon,
    "apps": merged_apps
}

with open("repo.json", "w", encoding="utf-8") as f:
    json.dump(mega_repo, f, separators=(',', ':'))

print(f"Total apps merged: {len(merged_apps)}")
