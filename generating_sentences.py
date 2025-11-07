import random

adjectives = ["large", "small", "black", "white", "fast", "slow", "happy", "sad", "clean", "dirty", "old", "new", "hot", "cold"]
nouns = ["stapler", "coffee mug", "raccoon", "coyote", "office chair", "pencil", "car", "motorcycle", "window", "desk"]
verbs1 = ["resting", "running", "floating", "moving", "walking", "falling", "tripping", "slipping", "rolling", "lamenting"]
adverbs = ["graciously", "menacingly", "intently", "ferociously", "gently", "aggressively", "meaningfully", "intentionally"]
locations = ["parking lot", "washroom", "warehouse", "cafeteria", "office space", "cubicle", "meeting room"]
verbs2 = ["apprehended", "arrested", "stopped", "moved", "circumvented", "avoided", "ameliorated", "fixed", "approached"]

def indefinite_article(noun):
    return "an" if noun[0] in "aeiou" else "a"
    
def generate_observation():
    sent_subject = random.choice(nouns)
    subject_adj = random.choice(adjectives)
    obs = f"I observed {indefinite_article(subject_adj)} {subject_adj} {sent_subject} {random.choice(verbs1)} {random.choice(adverbs)} in the {random.choice(locations)}."
    action = f"I successfully {random.choice(verbs2)} the {subject_adj} {sent_subject} to resolve the issue."
    return obs, action


observation, action = generate_observation()
print(observation)
print(action)
