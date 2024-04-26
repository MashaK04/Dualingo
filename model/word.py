class Word:
    def __init__(self, word='', translation='', part_of_speech=''):
        self.word = word
        self.translation = translation
        self.part_of_speech = part_of_speech

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word

    def get_translation(self):
        return self.translation

    def set_translation(self, translation):
        self.translation = translation

    def get_part_of_speech(self):
        return self.part_of_speech

    def set_part_of_speech(self, part_of_speech):
        self.part_of_speech = part_of_speech

    def __eq__(self, other):
        if isinstance(other, Word):
            return (
                    self.get_word() == other.get_word() and
                    self.get_part_of_speech() == other.get_part_of_speech()
            )
        return False
