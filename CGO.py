import json
import platform

def detect_hardware():
    return {
        "os": platform.system(),
        "cpu": platform.processor(),
        "ram": "16GB (voorbeeld)",
        "gpu": "NVIDIA RTX 3070 (voorbeeld)"
    }

def load_mod_profiles():
    with open("mod_profiles.json", "r") as f:
        return json.load(f)

def apply_settings(profile):
    print(f"[CGO] Instellingen toegepast voor profiel: {profile}")

def main():
    print("=== Cyberpunk Graphics Optimizer (CGO) ===")
    hw = detect_hardware()
    print("Hardware gedetecteerd:", hw)

    mods = load_mod_profiles()
    print("Beschikbare mod-profielen:", list(mods.keys()))

    # test: kies UltraPlus
    apply_settings("UltraPlus")

if __name__ == "__main__":
    main()