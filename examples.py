"""
Dark Matter Examples
====================

This file contains various examples demonstrating the use of the darkmatter module.
"""

from darkmatter import (
    DarkMatterParticle,
    DarkMatterHalo,
    calculate_dark_matter_percentage,
    wimps_properties
)
import math


def example_particle_system():
    """
    Example: Create a system of dark matter particles.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Dark Matter Particle System")
    print("=" * 70)
    
    particles = [
        DarkMatterParticle(mass=100, position=(0, 0, 0), velocity=(10, 0, 0)),
        DarkMatterParticle(mass=150, position=(5, 5, 0), velocity=(0, 15, 0)),
        DarkMatterParticle(mass=120, position=(10, 0, 5), velocity=(0, 0, 20)),
    ]
    
    total_energy = 0
    print("\nParticle System:")
    for i, particle in enumerate(particles, 1):
        energy = particle.kinetic_energy()
        total_energy += energy
        print(f"  Particle {i}: mass={particle.mass} GeV/c², KE={energy:.2f} GeV")
    
    print(f"\nTotal System Energy: {total_energy:.2f} GeV")


def example_milky_way_halo():
    """
    Example: Simulate the Milky Way's dark matter halo.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Milky Way Dark Matter Halo")
    print("=" * 70)
    
    # Estimated parameters for Milky Way dark matter halo
    milky_way_halo = DarkMatterHalo(
        total_mass=1.5e12,  # Approximately 1.5 trillion solar masses
        scale_radius=25      # Approximately 25 kiloparsecs
    )
    
    print(f"\n{milky_way_halo}")
    print("\nRotation Curve Analysis:")
    print("-" * 70)
    
    # Calculate rotation curve at various galactic radii
    test_radii = [2, 5, 8.5, 15, 30, 50, 100]  # kpc, 8.5 is solar position
    
    print(f"{'Radius (kpc)':<15} {'Velocity (km/s)':<20} {'Note'}")
    print("-" * 70)
    
    for r in test_radii:
        v = milky_way_halo.rotation_curve(r)
        note = ""
        if r == 8.5:
            note = "← Solar System position"
        elif r < 8.5:
            note = "Inner galaxy"
        elif r > 30:
            note = "Outer halo"
        
        print(f"{r:<15.1f} {v:<20.2f} {note}")


def example_compare_halos():
    """
    Example: Compare dark matter halos of different galaxy types.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Comparing Different Galaxy Halos")
    print("=" * 70)
    
    # Define different types of galaxies
    galaxies = {
        "Dwarf Galaxy": DarkMatterHalo(total_mass=1e9, scale_radius=5),
        "Spiral Galaxy (Milky Way-like)": DarkMatterHalo(total_mass=1.5e12, scale_radius=25),
        "Giant Elliptical": DarkMatterHalo(total_mass=1e13, scale_radius=50),
    }
    
    test_radius = 20  # kpc
    
    print(f"\nRotation velocity at {test_radius} kpc from center:")
    print("-" * 70)
    
    for galaxy_type, halo in galaxies.items():
        v = halo.rotation_curve(test_radius)
        print(f"{galaxy_type:<35} {v:>8.2f} km/s")


def example_density_profile():
    """
    Example: Analyze density distribution in a dark matter halo.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Dark Matter Density Profile")
    print("=" * 70)
    
    halo = DarkMatterHalo(total_mass=1e12, scale_radius=20)
    
    print(f"\n{halo}")
    print("\nDensity vs Radius (NFW Profile):")
    print("-" * 70)
    print(f"{'Radius (kpc)':<15} {'Relative Density':<20} {'Visualization'}")
    print("-" * 70)
    
    radii = [1, 5, 10, 20, 40, 80, 160]
    densities = [halo.density_profile(r) for r in radii]
    max_density = max(densities)
    
    for r, density in zip(radii, densities):
        relative_density = density / max_density
        bar_length = int(relative_density * 40)
        bar = "█" * bar_length
        print(f"{r:<15.0f} {relative_density:<20.6f} {bar}")


def example_universe_composition():
    """
    Example: Visualize the composition of the universe.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Universe Composition")
    print("=" * 70)
    
    composition = calculate_dark_matter_percentage()
    
    print("\nEnergy/Matter Distribution in the Universe:")
    print("-" * 70)
    
    total = sum(composition.values())
    for component, percentage in composition.items():
        bar_length = int(percentage * 0.5)  # Scale for display
        bar = "█" * bar_length
        print(f"{component.replace('_', ' ').title():<20} {percentage:>5.1f}%  {bar}")
    
    print(f"\n{'Total':<20} {total:>5.1f}%")
    
    print("\nKey Insights:")
    print("  • Dark energy dominates the universe, causing accelerated expansion")
    print("  • Dark matter is 5.5 times more abundant than ordinary matter")
    print("  • Only ~5% of the universe is made of atoms (stars, planets, us)")


def example_wimp_detection():
    """
    Example: Display information about WIMP detection methods.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 6: WIMP Detection Methods")
    print("=" * 70)
    
    props = wimps_properties()
    
    print("\nWeakly Interacting Massive Particles (WIMPs):")
    print("-" * 70)
    
    for prop, value in props.items():
        print(f"\n{prop.replace('_', ' ').title()}:")
        print(f"  {value}")
    
    print("\n\nDetection Challenges:")
    print("  • Very weak interaction cross-section (10^-36 cm²)")
    print("  • Requires massive detectors deep underground")
    print("  • Must distinguish signal from background radiation")
    print("  • Decades of searching with no confirmed detection yet")


def main():
    """Run all examples."""
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + " " * 20 + "DARK MATTER EXAMPLES" + " " * 28 + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)
    
    example_particle_system()
    example_milky_way_halo()
    example_compare_halos()
    example_density_profile()
    example_universe_composition()
    example_wimp_detection()
    
    print("\n" + "=" * 70)
    print("Examples completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
