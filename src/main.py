def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input


noun1 = get_input("noun")
verb1 = get_input("verb")
adjective1 = get_input("adjective")
noun2 = get_input("noun")
verb2 = get_input("verb")
adjective2 = get_input("adjective")

story = f"""

Once upon a time, in a vibrant kingdom nestled between towering mountains, there lived a {adjective1} {noun1} and a {adjective2} {noun2}. The {adjective1} {noun1} was known far and wide for her courage, while the {adjective2} {noun2} was beloved for the deep emotions she could {verb1} into every line of her verses.

One evening, the {adjective2} {noun2} sat near a crystal-clear lake, her fingers gently tracing the surface of the water, crafting words in her mind that would {verb1} her next poem. She believed that words held more power than swords, a belief that always fascinated the {adjective1} {noun1}.

The {adjective1} {noun1}, having just returned from a battle, found herself drawn to the peaceful serenity the {adjective2} {noun2} radiated. She watched as the {adjective2} {noun2}s effortlessly {verb2} beauty to the simplest things around her — from the reflection of the stars to the way the moonlight danced on the water's surface.

Over time, the {adjective1} {noun1} and the {adjective2} {noun2} grew close, learning from one another's strengths. The {adjective1} {noun1} shared her bravery and honor, while the {adjective2} {noun2} taught her that true strength often lay in the quiet, gentle moments, not just the fierce clashes of battle. She {verb2} new perspectives on what it meant to fight for justice and freedom.

They came to realize that their love wasn’t one of dominance, but of equal respect and admiration. Each of them, in their own way, stood proudly in who they were, refusing to conform to the narrow expectations of the world around them.

Together, they traveled the kingdom, inspiring all who met them. Their love became a symbol of strength, not only in the battles fought but in the beautiful, silent ways they {verb1} one another every day. Their ability to {verb2} a sense of peace and {verb1} strength was the perfect balance.

And so, their story spread across the land — a tale of bravery, passion, and the unwavering bond that formed between a {adjective1} {noun1} and a {adjective2} {noun2}, two souls whose love was anything but ordinary.

"""

print(story)