
from book.models import *


class BuildBookData:

    def build_all(self):
        self.build_stories()
        self.build_tones()
        self.build_settings()
        self.build_characters()

    @staticmethod
    def build_stories():
        stories = [
            Story(
                title="Test Under the Rainbow",
                message="Greed will contaminate your",
            )
        ]
        Story.objects.bulk_Create(stories)

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

        Character.objects.bulk_Create(characters)

    @staticmethod
    def build_settings():
        settings = [
            Setting(
                description="Another world on the dark side of the rainbow, accessible only through the shadow of a "
                                "rainbow when it's at a specific location. The world is chaotic and terrorized by the "
                                "Wicked Witch. Many citizens of the main kingdom are poor and the kingdom has just "
                                "executed half of the population for the 3rd time in 20 years.",
                story=Story.objects.first()
            )
        ]

        Setting.objects.bulk_Create(settings)

    @staticmethod
    def build_tones():
        tones = [
            Tone(name="Dark and eerie", story=Story.objects.first()),
            Tone(name="Epic", story=Story.objects.first()),
            Tone(name="Adventurous", story=Story.objects.first()),
        ]
        Tone.objects.bulk_create(tones)





