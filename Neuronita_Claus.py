import math

class PapaNoelNeuron:
    def __init__(self, w=[0.8, 0.1, 0.1], b=-0.2):
        # Pesos: portarse bien = más importante
        # Sesgo negativo: evita que con todo en cero salga regalo
        self.w = w
        self.b = b

    def _sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def decide(self, x):
        z = sum(wi * xi for wi, xi in zip(self.w, x)) + self.b
        prob = self._sigmoid(z)
        return "🎁 Regalo" if prob >= 0.5 else "🪨 Carbón"

# Ejemplos de prueba:
papa_noel = PapaNoelNeuron()

# Niño que se portó bien, escribió carta y decoró
print([1,1,1], "->", papa_noel.decide([1,1,1]))  # 🎁 Regalo

# Niño que no se portó bien ni escribió carta ni decoró
print([0,0,0], "->", papa_noel.decide([0,0,0]))  # 🪨 Carbón

# Niño que se portó bien pero no decoró ni escribió carta
print([1,0,0], "->", papa_noel.decide([1,0,0]))  # 🎁 Regalo

# Niño que solo escribió carta pero no se portó bien
print([0,1,0], "->", papa_noel.decide([0,1,0]))  # 🪨 Carbón

