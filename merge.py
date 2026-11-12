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
seen_bundles = set()
default_icon = "https://raw.githubusercontent.com/RadhityaOG/IPA-Libary/main/IMG_6762.jpeg"

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            apps = data.get('apps', [])
            if not isinstance(apps, list):
                continue
            for app in apps:
                if not isinstance(app, dict):
                    continue
                bundle_id = str(app.get('bundleIdentifier') or '').strip()
                version = str(app.get('version') or '').strip()
                download_url = str(app.get('downloadURL') or '').strip()
                name = str(app.get('name') or '').strip()

                if not (bundle_id and version and name and download_url.startswith('http')):
                    continue
                if ' ' in download_url:
                    continue

                uid = f"{bundle_id}_{version}"
                if uid in seen_bundles:
                    continue
                seen_bundles.add(uid)

                icon_url = str(app.get('iconURL') or '').strip()
                if not icon_url.startswith('http') or ' ' in icon_url:
                    icon_url = default_icon

                raw_size = app.get('size', 0)
                try:
                    size = int(float(raw_size)) if raw_size is not None else 0
                except (ValueError, TypeError):
                    size = 0

                clean_app = {
                    "name": name,
                    "bundleIdentifier": bundle_id,
                    "developerName": str(app.get('developerName') or 'Unknown').strip() or 'Unknown',
                    "version": version,
                    "versionDate": str(app.get('versionDate') or '2025-01-
