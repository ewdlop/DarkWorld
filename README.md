# DarkWorld

A comprehensive exploration of dark matter physics and simulations.

## Overview

Dark matter is one of the most intriguing mysteries in modern physics. Despite making up approximately 26.8% of the universe's total mass-energy content, it remains invisible and interacts primarily through gravity. This repository provides tools and simulations to explore dark matter concepts.

## Features

- **Dark Matter Particle Simulation**: Model hypothetical dark matter particles with mass, position, and velocity
- **Dark Matter Halo**: Simulate dark matter halos around galaxies using the NFW (Navarro-Frenk-White) profile
- **Rotation Curves**: Calculate galactic rotation curves influenced by dark matter
- **Universe Composition**: Explore the distribution of matter and energy in the universe
- **WIMP Properties**: Information about Weakly Interacting Massive Particles, a leading dark matter candidate

## Installation

```bash
git clone https://github.com/ewdlop/DarkWorld.git
cd DarkWorld
```

No additional dependencies required - uses only Python standard library.

## Usage

### Running the Dark Matter Simulation

```bash
python darkmatter.py
```

### Using the Module in Your Code

```python
from darkmatter import DarkMatterParticle, DarkMatterHalo

# Create a dark matter particle
particle = DarkMatterParticle(
    mass=100,  # GeV/c²
    position=(1, 2, 3),
    velocity=(10, 20, 15)
)
print(f"Kinetic Energy: {particle.kinetic_energy()} GeV")

# Create a dark matter halo
halo = DarkMatterHalo(
    total_mass=1e12,  # Solar masses
    scale_radius=20   # kiloparsecs
)

# Calculate rotation velocity at 40 kpc from center
velocity = halo.rotation_curve(40)
print(f"Rotation velocity at 40 kpc: {velocity:.2f} km/s")
```

## Dark Matter Facts

- **Composition**: Dark matter makes up ~26.8% of the universe, while ordinary matter is only ~4.9%
- **Detection**: Cannot be directly observed but inferred through gravitational effects
- **Candidates**: WIMPs (Weakly Interacting Massive Particles), Axions, and other exotic particles
- **Evidence**: Galactic rotation curves, gravitational lensing, cosmic microwave background

## Scientific Background

### What is Dark Matter?

Dark matter is a form of matter that doesn't interact with electromagnetic radiation, making it invisible to telescopes. However, its presence is inferred through:

1. **Galactic Rotation Curves**: Stars at the edges of galaxies move faster than expected based on visible matter alone
2. **Gravitational Lensing**: Light from distant objects is bent by invisible mass
3. **Cosmic Microwave Background**: Patterns in the CMB suggest significant non-baryonic matter

### The NFW Profile

The Navarro-Frenk-White (NFW) profile describes the density distribution of dark matter in halos:

```
ρ(r) = ρ₀ / (r/rₛ(1 + r/rₛ)²)
```

Where:
- ρ(r) is the density at radius r
- ρ₀ is the characteristic density
- rₛ is the scale radius

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available for educational purposes.

## References

- Navarro, J. F., Frenk, C. S., & White, S. D. M. (1996). "The Structure of Cold Dark Matter Halos"
- Bertone, G., Hooper, D., & Silk, J. (2005). "Particle dark matter: evidence, candidates and constraints"
- Planck Collaboration (2018). "Planck 2018 results"