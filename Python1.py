class MusicalInstrument:
    def __init__(self, name, type_, material, volume):
        self.name = name
        self.type = type_
        self.material = material
        self._volume = self._validate_volume(volume)

    def __str__(self):
        return f"{self.name} - {self.type}, материал: {self.material}, громкость: {self._volume}"

    @staticmethod
    def _validate_volume(volume):
        return max(0, min(10, volume))

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, change):
        self._volume = self._validate_volume(change)

    def play(self, notes):
        if self._volume == 0:
            return ""
        interpretation = {
        "струнный": lambda n: "-".join(n),
        "духовой": lambda n: " ".join(n) + "~",
        "ударный": lambda n: " ".join([f"Б{note}" for note in n]),
    }
        note_interpretation = interpretation.get(self.type, lambda n: " ".join(n))
        return f"{self.name} играет: {note_interpretation(notes)}"


    def adjust_volume(self, change):
        self.volume += change
        print(f"Громкость {self.name} установлена на {self._volume}")

    def repair(self):
        print(f"{self.name} отремонтирован и готов к игре!")

    def get_sound(self):
        sounds = {"струнный": "Дзынь", "духовой": "Ду-ду", "ударный": "Бах!"}
        return sounds.get(self.type, "Неизвестный звук")


class ElectricGuitar(MusicalInstrument):
    def __init__(self, name, material, volume, distortion):
        super().__init__(name, "струнный", material, volume)
        self._distortion = self._validate_distortion(distortion)

    @staticmethod
    def _validate_distortion(distortion):
        return max(0.0, min(1.0, distortion))

    @property
    def distortion(self):
        return self._distortion

    @distortion.setter
    def distortion(self, value):
        self._distortion = self._validate_distortion(value)

    def play(self, notes):
        if self._volume == 0:
            return ""
        effect = "ВЖЖЖЖ" if self._distortion > 0.5 else "Бррр"
        return f"{self.name} играет с дисторшном ({self._distortion}): {effect} {' '.join(notes)}"


guitar = MusicalInstrument("Гитара", "струнный", "дерево", 5)
flute = MusicalInstrument("Флейта", "духовой", "металл", 7)
drum = MusicalInstrument("Барабан", "ударный", "пластик", 8)

print(guitar.play("CDEFGAB"))  # Тут будет C-D-E-F-G-A-B
print(flute.play("CDEFGAB"))   # Тут будет C D E F G A B~
print(drum.play("CDEFGAB"))    # Тут будет БC БD БE БF БG БA БB

print(guitar)
print(flute)
print(drum)

flute.adjust_volume(-3)
print(flute.get_sound())
print(drum.get_sound())

guitar.repair()
guitar.distortion = 0.3
print(guitar.play("EFG"))
