"""
Dark Matter Module
==================

This module provides tools and simulations related to dark matter physics.
Dark matter is a hypothetical form of matter that does not interact with 
electromagnetic radiation, making it invisible to the entire electromagnetic spectrum.
"""

import math


class DarkMatterParticle:
    """
    Represents a hypothetical dark matter particle.
    
    Attributes:
        mass (float): Mass of the particle in GeV/c²
        position (tuple): 3D position coordinates (x, y, z)
        velocity (tuple): 3D velocity components (vx, vy, vz)
    """
    
    def __init__(self, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        """
        Initialize a dark matter particle.
        
        Args:
            mass (float): Mass of the particle in GeV/c²
            position (tuple): Initial 3D position (x, y, z)
            velocity (tuple): Initial 3D velocity (vx, vy, vz)
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity
    
    def kinetic_energy(self):
        """
        Calculate kinetic energy of the particle.
        
        Returns:
            float: Kinetic energy in GeV
        """
        v_squared = sum(v**2 for v in self.velocity)
        return 0.5 * self.mass * v_squared
    
    def __repr__(self):
        return f"DarkMatterParticle(mass={self.mass}, pos={self.position}, vel={self.velocity})"


class DarkMatterHalo:
    """
    Represents a dark matter halo around a galaxy.
    
    Dark matter halos are theoretical distributions of dark matter that 
    extend beyond the visible edges of galaxies.
    """
    
    def __init__(self, total_mass, scale_radius):
        """
        Initialize a dark matter halo.
        
        Args:
            total_mass (float): Total mass of the halo in solar masses
            scale_radius (float): Scale radius in kiloparsecs
        """
        self.total_mass = total_mass
        self.scale_radius = scale_radius
    
    def density_profile(self, radius):
        """
        Calculate density at a given radius using NFW profile.
        
        The Navarro-Frenk-White (NFW) profile is commonly used to describe
        the distribution of dark matter in halos.
        
        Args:
            radius (float): Distance from halo center in kiloparsecs
            
        Returns:
            float: Density at the given radius
        """
        if radius <= 0:
            return float('inf')
        
        x = radius / self.scale_radius
        rho_0 = self.total_mass / (4 * math.pi * self.scale_radius**3)
        return rho_0 / (x * (1 + x)**2)
    
    def rotation_curve(self, radius):
        """
        Calculate rotation velocity at a given radius.
        
        Args:
            radius (float): Distance from halo center in kiloparsecs
            
        Returns:
            float: Rotation velocity in km/s
        """
        if radius <= 0:
            return 0
        
        # Simplified rotation curve calculation
        G = 4.302e-6  # Gravitational constant in kpc * (km/s)^2 / solar mass
        x = radius / self.scale_radius
        
        # Mass enclosed within radius
        mass_enclosed = self.total_mass * (math.log(1 + x) - x / (1 + x))
        
        return math.sqrt(G * mass_enclosed / radius)
    
    def __repr__(self):
        return f"DarkMatterHalo(total_mass={self.total_mass} M☉, scale_radius={self.scale_radius} kpc)"


def calculate_dark_matter_percentage():
    """
    Returns the estimated percentage of dark matter in the universe.
    
    Returns:
        dict: Dictionary containing percentages of universe components
    """
    return {
        "dark_energy": 68.3,
        "dark_matter": 26.8,
        "ordinary_matter": 4.9
    }


def wimps_properties():
    """
    Returns properties of WIMPs (Weakly Interacting Massive Particles).
    
    WIMPs are hypothetical particles that are candidates for dark matter.
    
    Returns:
        dict: Dictionary containing WIMP properties
    """
    return {
        "mass_range": "10 GeV/c² to 10 TeV/c²",
        "interaction": "Weak nuclear force",
        "stability": "Stable or very long-lived",
        "detection": "Direct detection experiments, indirect detection, collider searches"
    }


if __name__ == "__main__":
    # Example usage
    print("=" * 60)
    print("Dark Matter Simulation")
    print("=" * 60)
    
    # Create a dark matter particle
    particle = DarkMatterParticle(
        mass=100,  # GeV/c²
        position=(1, 2, 3),
        velocity=(10, 20, 15)
    )
    print(f"\n{particle}")
    print(f"Kinetic Energy: {particle.kinetic_energy():.2f} GeV")
    
    # Create a dark matter halo
    print("\n" + "-" * 60)
    halo = DarkMatterHalo(
        total_mass=1e12,  # Solar masses
        scale_radius=20   # kiloparsecs
    )
    print(f"\n{halo}")
    
    # Calculate rotation curve at different radii
    print("\nRotation Curve:")
    radii = [5, 10, 20, 40, 80]
    for r in radii:
        v = halo.rotation_curve(r)
        print(f"  r = {r:3d} kpc: v = {v:.2f} km/s")
    
    # Display universe composition
    print("\n" + "-" * 60)
    print("\nUniverse Composition:")
    composition = calculate_dark_matter_percentage()
    for component, percentage in composition.items():
        print(f"  {component.replace('_', ' ').title()}: {percentage}%")
    
    # Display WIMP properties
    print("\n" + "-" * 60)
    print("\nWIMP Properties:")
    wimp_props = wimps_properties()
    for prop, value in wimp_props.items():
        print(f"  {prop.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 60)
