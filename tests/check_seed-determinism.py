from fastn import noise
from random import Random

rand = Random(1)

seeds = [rand.randint(0, i) * i * i for i in range(128)]
samplePositions = [(x / 0.17865, y * 0.189652) for x in range(128) for y in range(128)]

for seed in seeds:
    np1 = noise.PerlinNoise(seed)
    np2 = noise.PerlinNoise(seed)
    for samplePos in samplePositions:
        assert np1.Sample(*samplePos) == np2.Sample(*samplePos)
        assert np1.Sample(*samplePos) == np1.Sample(*samplePos)