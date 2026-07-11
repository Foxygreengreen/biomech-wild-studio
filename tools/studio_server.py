#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
BACKUP_DIR = DATA_DIR / ".backups"
HOST = "127.0.0.1"
PORT = 8788

READY_STATUS = "🟢 готово к публикации"
ACTIVE_STATUS = "💡 идея"
PUBLISHED_STATUS = "✅ опубликовано"

MAIN_SUBJECTS = [
    ("Monsoon Pangolin", "rainforest floor", "overlapping titanium scales and soft organic eyes"),
    ("Reef Moray", "coral reef cave", "servo jaw hinges and flexible cable muscles"),
    ("Boreal Lynx", "snowy pine edge", "exposed shoulder pistons and quiet paw stabilizers"),
    ("Emerald Scarab", "humid mossy log", "polished green shell plates with tiny brass actuators"),
    ("Copper Seahorse", "seagrass meadow", "curled mechanical tail and translucent organic fins"),
    ("Clouded Macaw", "upper jungle canopy", "feather-like carbon plates and micro gear joints"),
    ("Granite Tortoise", "dry volcanic plain", "stone-like armor shell with visible hydraulic seams"),
    ("Tidepool Anemone", "rocky tidepool", "soft tentacles threaded with fine chrome filaments"),
    ("Glasswing Dragonfly", "river reeds", "transparent wing membranes with visible micro servos"),
    ("Desert Jerboa", "moonlit sand burrow", "spring-loaded hind legs and delicate whisker sensors"),
    ("Neon Reef Cuttlefish", "coral sand channel", "skin-like adaptive plates with soft cyan signal lines"),
    ("Aurora Jellyfish", "cold dark water column", "transparent bell threaded with chrome filaments and pale inner glow"),
    ("Ember Salamander", "humid moss and stone", "black wet skin with warm orange mechanical breathing vents"),
    ("Moonlit Snow Owl", "winter forest clearing", "white feather-plates with faint blue sensor lines near the wings"),
    ("Prismatic Beetle", "rainforest leaf surface", "iridescent shell with microscopic servo seams and low internal glow"),
    ("Opal Koi", "clear garden pond", "ceramic scales with visible pearl-lit hydraulic channels"),
    ("Lumen Gecko", "wet jungle bark", "translucent toes with tiny glowing grip actuators"),
    ("Tideglass Horseshoe Crab", "shallow tidal sand flat", "domed copper-black shell with visible underside servo legs and wet organic joints"),
    ("Mangrove Mudskipper Unit", "muddy mangrove root bank", "amphibious skin with tiny brass gill vents and articulated pectoral fin supports"),
    ("Frostline Arctic Fox", "windy tundra ridge", "white winter coat parted by stable graphite shoulder plates and fine sensor whiskers"),
    ("Amber Leafcutter Ant", "rainforest leaf trail", "tiny segmented body with amber carapace plates and precise micro-hydraulic legs"),
    ("River Otter Frame", "clear river stone edge", "sleek wet body with flexible spine-side alloy rails integrated under dark fur"),
    ("Desert Viper Coil", "warm red sand hollow", "scales interlocked with matte bronze micro-plates and a stable jaw hinge"),
    ("Alpine Ibex Mechanism", "high rocky mountain ledge", "curved horn cores with layered ceramic ridges and visible knee stabilizers"),
    ("Glass Reef Shrimp", "clear coral lagoon", "transparent shell revealing tiny chrome organs, cable tendons, and living tissue"),
    ("Bamboo Chameleon Array", "green bamboo branch", "color-shifting skin plates with slow mechanical iris rings and delicate grip actuators"),
    ("Abyss Angler Relay", "deep black ocean slope", "organic head and fins integrated with pressure-safe titanium ribs and a dim biological lure"),
    ("Savanna Secretarybird Unit", "dry golden grassland", "long legs with elegant piston tendons and feather-plates integrated into the wings"),
    ("Cave Axolotl Mechanism", "clear limestone cave pool", "pale amphibian skin with visible gill-side ceramic micro-filters and soft joint cables"),
]

CARD_VARIANTS = [
    {
        "name": "documentary texture",
        "image": "Emphasize tactile surface detail, real skin or shell texture, and readable mechanical seams.",
        "video": "Movement is observational and restrained, like a real wildlife camera waiting for behavior.",
    },
    {
        "name": "luminescent biology",
        "image": "Use natural bioluminescence as part of the creature anatomy: dim living glow inside membranes, pores, or channels, never as external light effects.",
        "video": "Bioluminescent details pulse very subtly as a stable biological mechanism, with no flashes, no magic glow, and no decorative light show.",
    },
    {
        "name": "macro biomechanics",
        "image": "Frame close enough to see micro pistons, flexible cable tendons, layered plates, and organic tissue integration.",
        "video": "Show small mechanical articulation during breathing, stepping, fin movement, or posture changes.",
    },
]

PET_SUBJECTS = [
    ("Black Servo Cat", "quiet apartment window ledge", "sleek black fur parted by visible spine-side micro servos"),
    ("Copper House Dog", "sunlit kitchen floor", "warm organic muzzle with stable copper shoulder mechanics"),
    ("Silver Chinchilla", "soft indoor wooden shelf", "dense fur integrated around visible ribbed alloy joints"),
    ("Ferret Cable Runner", "narrow blanket tunnel", "long flexible body with exposed cable tendons along the sides"),
    ("Maine Coon Frame", "warm living room rug", "large soft body with visible titanium shoulder frame under parted long fur"),
    ("Siamese Sensor Cat", "quiet hallway at night", "cream fur and dark face with delicate optical sensor whisker roots"),
    ("Corgi Ground Unit", "sunlit wooden floor", "short legs with compact stabilizer joints and soft organic expression"),
    ("Guardian Shepherd", "backyard grass near a fence", "muscular organic body with exposed chest-side hydraulic supports"),
    ("Poodle Precision Unit", "clean grooming table", "curled fur shaped around visible chrome elbow and knee mechanics"),
    ("Dust Bath Chinchilla", "ceramic dust bath bowl", "round dense fur with tiny visible cooling vents along the spine"),
    ("Sable Sneak Ferret", "folded blanket tunnel", "dark flexible body with cable-like side tendons and small brass joints"),
    ("White Tunnel Ferret", "soft fabric play tube", "white fur integrated with pale ceramic vertebrae and micro servos"),
    ("Lumen Collar Cat", "dim apartment bookshelf", "subtle bioluminescent neck-side sensor line integrated under short fur"),
    ("Porcelain Toy Dog", "small sofa cushion", "tiny organic body with porcelain-like biomech paw stabilizers"),
    ("Velvet Chinchilla Unit", "wooden pet house", "velvet grey fur with visible pearl-lit breathing vents"),
    ("Copper Mask Ferret", "narrow kitchen shadow", "masked ferret face with copper jaw hinge and flexible torso mechanics"),
    ("Tuxedo Servo Cat", "apartment doorway", "black and white fur parted around stable shoulder micro-pistons"),
    ("Dachshund Spine Unit", "low hallway carpet", "long body with visible flexible vertebral support rails"),
    ("Blue Chinchilla Rotor", "quiet cage platform", "blue-grey fur with tiny silent cooling rotors near the hips"),
    ("Albino Ferret Relay", "white blanket fold", "pale body with translucent cable tendons along the torso"),
    ("Tabby Window Cat", "rainy windowsill", "striped fur integrated with brass paw stabilizers and sensor whiskers"),
    ("Retriever Hearth Dog", "warm living room floor", "golden organic coat with visible chest-side hydraulic breathing supports"),
]


def load_cards(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data.setdefault("cards", [])


def save_cards(path: Path, cards: list[dict]) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(path, BACKUP_DIR / f"{path.stem}.{stamp}.json")
    tmp = path.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump({"cards": cards}, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    tmp.replace(path)


def data_path_for(handler: SimpleHTTPRequestHandler) -> Path:
    referer = handler.headers.get("Referer", "")
    if "pets.html" in referer:
        return DATA_DIR / "pets_cards.json"
    return DATA_DIR / "cards.json"


def read_json_body(handler: SimpleHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length", "0") or "0")
    if not length:
        return {}
    raw = handler.rfile.read(length).decode("utf-8")
    return json.loads(raw or "{}")


def write_json(handler: SimpleHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def find_card(cards: list[dict], num: int) -> dict:
    for card in cards:
        if int(card.get("num", -1)) == num:
            return card
    raise ValueError(f"Card #{num} not found")


def set_group(card: dict, group: str) -> None:
    labels = {
        "active": ("Новые", ACTIVE_STATUS),
        "ready": ("Готово", READY_STATUS),
        "published": ("Опубликовано", PUBLISHED_STATUS),
    }
    group_label, status = labels[group]
    card["group"] = group
    card["groupLabel"] = group_label
    card["status"] = status


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "card"


def hashtag(value: str) -> str:
    return "#" + re.sub(r"[^a-z0-9]+", "", value.lower())


def seo_caption(name: str, habitat: str, signature: str, pets: bool) -> str:
    if pets:
        body = (
            f"Biomechanical pet concept: {name} in a natural {habitat}. "
            f"This parallel-universe animal keeps its warm domestic identity while visible biomechanical anatomy "
            f"becomes part of the body: {signature}. Designed for AI creature design, cinematic pet content, "
            "and realistic biomechanical character continuity."
        )
        tags = ["#biomechpets", "#biomechanical", "#aipets", "#creaturedesign", hashtag(name)]
    else:
        body = (
            f"Biomechanical wildlife concept: {name} in a natural {habitat}. "
            f"This parallel-universe creature combines organic animal behavior with visible integrated mechanisms: "
            f"{signature}. Created for AI wildlife video, cinematic creature design, and realistic biomechanical "
            "worldbuilding."
        )
        tags = ["#biomechwild", "#biomechanical", "#aicreatures", "#wildlifeart", hashtag(name)]
    return body + "\n\n" + " ".join(tags)


def next_subject(cards: list[dict], pets: bool) -> tuple[str, str, str]:
    pool = PET_SUBJECTS if pets else MAIN_SUBJECTS
    names = {card.get("name") for card in cards}
    for item in pool:
        if item[0] not in names:
            return item
    return pool[len(cards) % len(pool)]


def make_card(cards: list[dict], pets: bool) -> dict:
    next_num = max((int(card.get("num", 0)) for card in cards), default=0) + 1
    name, habitat, signature = next_subject(cards, pets)
    variant = CARD_VARIANTS[next_num % len(CARD_VARIANTS)]
    file_slug = f"{next_num:03d}_{slugify(name)}.md"
    video_slug = f"{next_num:03d}_{slugify(name)}.mp4"
    hook = "A real animal from a parallel biomechanical world"
    if pets:
        hook = "A domestic companion with visible stable biomechanics"

    image_prompt = (
        f"Vertical 9:16 premium documentary wildlife portrait of {name}, "
        f"in a natural {habitat}. The creature is biologically alive but structurally biomechanical: "
        f"{signature}. The biomechanics are integrated into anatomy and remain clearly visible, "
        "not decorative, not skeletal horror, not hidden under fur. Realistic texture, tactile materials, "
        "calm documentary framing, natural light, no fantasy glow, no visual effects, no text, "
        f"no logo, no watermark, no captions, no letters anywhere in the image. {variant['image']}"
    )

    video_prompt = (
        f"Vertical cinematic wildlife video of {name} in a single continuous {habitat} location. "
        f"The creature makes small natural movements, breathes, shifts weight, and briefly looks toward camera. "
        f"Biomechanical details stay stable and visible: {signature}. Smooth controlled camera, no cuts, "
        "no sudden transformation, no fur growing or shedding, no location change, no decorative light effects, "
        f"no falling trees. {variant['video']}"
    )

    natgeo = (
        f"Premium documentary wildlife encounter variant: {name} observes another biomechanical species from the same {habitat}. "
        "Both creatures are biomechanical and anatomically consistent. The interaction is cautious and natural, "
        "with stalking, retreat, or territorial tension, not fantasy combat. No text, no logo, no watermark, "
        "no captions, no letters anywhere in the image or video."
    )

    caption = seo_caption(name, habitat, signature, pets)

    return {
        "num": next_num,
        "name": name,
        "hook": hook,
        "file": file_slug,
        "videoFile": video_slug,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "group": "active",
        "groupLabel": "Новые",
        "status": ACTIVE_STATUS,
        "imagePrompt": image_prompt,
        "videoPrompt": video_prompt,
        "videoPromptVeo": video_prompt + " Optimized for Veo: coherent motion, stable subject identity, one shot.",
        "videoPromptSeedance": video_prompt + " Optimized for Seedance: smooth natural action, clean subject silhouette.",
        "videoPromptKling": video_prompt + " Optimized for Kling: realistic creature motion and stable anatomy.",
        "scene8s": f"8 seconds: {name} pauses in the {habitat}, breathes, shifts posture, and looks toward camera.",
        "scene15s": f"15 seconds: {name} moves slowly through the {habitat}, revealing stable integrated mechanisms.",
        "storyboard30s": (
            f"0-10s establish {habitat}; 10-20s close wildlife observation of {name}; "
            "20-30s subtle behavior hook and loopable ending."
        ),
        "natgeoEncounter": natgeo,
        "overlay": name,
        "caption": caption,
        "notes": f"Generated by local Studio backend refill logic. Variant: {variant['name']}.",
        "platforms": ["image", "veo", "seedance", "kling", "instagram"],
    }


def ensure_active(cards: list[dict], target: int, pets: bool) -> int:
    created = 0
    while sum(1 for card in cards if card.get("group") == "active") < target:
        cards.append(make_card(cards, pets))
        created += 1
    return created


class StudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self) -> None:
        endpoint = urlparse(self.path).path
        if not endpoint.startswith("/api/"):
            self.send_error(404)
            return

        try:
            payload = read_json_body(self)
            path = data_path_for(self)
            pets = path.name == "pets_cards.json"
            cards = load_cards(path)

            if endpoint == "/api/mark-ready":
                card = find_card(cards, int(payload["num"]))
                set_group(card, "ready")
                created = ensure_active(cards, int(payload.get("target", 10)), pets)
                save_cards(path, cards)
                write_json(self, 200, {"ok": True, "created": created})
                return

            if endpoint == "/api/mark-ready-only":
                card = find_card(cards, int(payload["num"]))
                set_group(card, "ready")
                save_cards(path, cards)
                write_json(self, 200, {"ok": True})
                return

            if endpoint == "/api/mark-active":
                card = find_card(cards, int(payload["num"]))
                set_group(card, "active")
                save_cards(path, cards)
                write_json(self, 200, {"ok": True})
                return

            if endpoint == "/api/mark-published":
                card = find_card(cards, int(payload["num"]))
                set_group(card, "published")
                save_cards(path, cards)
                write_json(self, 200, {"ok": True})
                return

            if endpoint == "/api/ensure-active":
                created = ensure_active(cards, int(payload.get("target", 10)), pets)
                save_cards(path, cards)
                write_json(self, 200, {"ok": True, "created": created})
                return

            self.send_error(404)
        except Exception as exc:
            write_json(self, 500, {"ok": False, "error": str(exc)})


def main() -> int:
    server = ThreadingHTTPServer((HOST, PORT), StudioHandler)
    print(f"Biomech Wild Studio backend running at http://{HOST}:{PORT}/")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
