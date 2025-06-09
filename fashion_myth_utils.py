import random

def get_myth_theme_suggestions(myth):
    ideas = {
        "Greek": ["Toga dress with metallic gladiator boots", "Olive leaf motif on jacket sleeves"],
        "Indian": ["Saree-gown fusion with gold embroidery", "Veena-inspired handbag"],
        "Norse": ["Valkyrie armor coat with fur trim", "Runestone-print leggings"],
        "Egyptian": ["Anubis hoodie with glowing eyes", "Scarab brooch accessories"],
        "Celtic": ["Knotwork cape with glowing embroidery", "Tunic dress with forest tones"]
    }
    return "\n".join(f"- {idea}" for idea in ideas.get(myth, []))

def match_image_to_myth(image):
    myths = ["Greek", "Indian", "Norse", "Egyptian", "Celtic"]
    return random.choice(myths)
