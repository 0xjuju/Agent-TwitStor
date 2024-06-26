
from book.models import *


class BuildBookData:

    def build_all(self):
        self.build_stories()
        self.build_tones()
        self.build_characters()

    @staticmethod
    def build_stories():
        stories = [
            Story(
                title="Test Under the Rainbow",
                theme="Greed will contaminate your",
                setting="Another world on the dark side of the rainbow, accessible only through the shadow of a "
                        "rainbow when it's at a specific location. The world is chaotic and terrorized by the "
                        "Wicked Witch. Many citizens of the main kingdom are poor and the kingdom has just "
                        "executed half of the population for the 3rd time in 20 years.",
                conflict="After the the kingdom executed half its population for the third time in 20 years, the "
                         "protagonists decide to craft a clever plan to attack the capital in rebellion"
            )
        ]
        Story.objects.bulk_create(stories)

    @staticmethod
    def build_characters():
        characters = [
            Character(
                name="Tyrion",
                role="Main Character",
                background="Mysterious person who has a dark past. His parent were killed in front of him as a child",
                story=Story.objects.first()
            ),

            Character(
                name="Misa",
                role="Side Character",
                background="Princess of the royal family. Very selfish and has little empathy for normal citizens",
                story=Story.objects.first()
            )
        ]

        Character.objects.bulk_create(characters)

    @staticmethod
    def build_tones():
        tones = [
            Tone(name="Dark and eerie", story=Story.objects.first()),
            Tone(name="Epic", story=Story.objects.first()),
            Tone(name="Adventurous", story=Story.objects.first()),
        ]
        Tone.objects.bulk_create(tones)





