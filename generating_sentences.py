import random


adjectives = ["large", "small", "tiny", "huge", "massive", "compact", "black", "white", "gray", "bright",
              "fast", "slow", "quick", "sluggish", "happy", "sad", "cheerful", "gloomy", "clean", "dirty",
              "old", "new", "modern", "ancient", "hot", "cold", "warm", "chilly"]

nouns = ["stapler", "coffee mug", "raccoon", "coyote", "office chair", "pencil", "car", "motorcycle",
         "window", "desk", "fox", "notebook", "wet floor sign", "printer", "keyboard", "monitor",
         "door", "lamp", "trash bin", "file cabinet"]

verbs1 = ["resting", "running", "floating", "moving", "walking", "falling", "tripping", "slipping",
          "rolling", "lamenting", "grazing", "standing", "leaning", "hanging", "balancing"]

adverbs = ["graciously", "menacingly", "intently", "ferociously", "gently", "aggressively",
           "meaningfully", "intentionally", "maleficently", "calmly", "quietly", "boldly", "carefully"]

locations = ["parking lot", "washroom", "warehouse", "cafeteria", "office space", "cubicle", "meeting room",
             "first floor", "second floor", "third floor", "stairwell", "loading dock", "reception area"]

verbs2 = ["apprehended", "arrested", "stopped", "moved", "circumvented", "avoided", "ameliorated",
          "fixed", "approached", "rectified", "addressed", "resolved", "corrected", "handled"]


def indefinite_article(noun):
    return "an" if noun[0] in "aeiou" else "a"
    
def generate_observation():

    sent_subject = random.choice(nouns)
    subject_adj = random.choice(adjectives)
    sent_loc = random.choice(locations)

    obs = f"I observed {indefinite_article(subject_adj)} {subject_adj} {sent_subject} {random.choice(verbs1)} {random.choice(adverbs)} in the {sent_loc}."
    action = f"I successfully {random.choice(verbs2)} the {subject_adj} {sent_subject} to resolve the issue."
    
    return sent_loc, obs, action

