
from django.test import TestCase
from agents.clean_data import *


class TestCleanData(TestCase):
    def setUp(self):
        pass

    def test_start_text_at_word(self):
        word = "langton"

        text = """while ago there was a young man dwelling in a great and goodly city by
the sea which had to name Langton on Holm.   He was but of five and
twenty winters, a fair-faced man, yellow-haired, tall and strong; rather
wiser than foolisher than young men are mostly wont; a valiant youth, and
a kind; not of many words but courteous of speech; no roisterer, nought
masterful, but peaceable and knowing how to forbear: in a fray a perilous
foe, and a trusty war-fellow.   His father, with whom he was dwelling
when this tale begins, was a great merchant, richer than a baron of the
land, a head-man of the greatest of the Lineages of Langton, and a
captain of the Porte; he was of the Lineage of the Goldings, therefore
was he called Bartholomew Golden, and his son Golden Walter."""

        new_text = start_text_at_word(text, word)
        self.assertEqual(new_text[0:16], "Langton on Holm.")

s






