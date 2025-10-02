"""
Tests for the Dark Matter Module
"""

import math
from darkmatter import (
    DarkMatterParticle,
    DarkMatterHalo,
    calculate_dark_matter_percentage,
    wimps_properties
)


def test_dark_matter_particle():
    """Test DarkMatterParticle creation and methods."""
    print("Testing DarkMatterParticle...")
    
    # Test initialization
    particle = DarkMatterParticle(mass=100, position=(1, 2, 3), velocity=(10, 20, 15))
    assert particle.mass == 100
    assert particle.position == (1, 2, 3)
    assert particle.velocity == (10, 20, 15)
    
    # Test kinetic energy calculation
    # KE = 0.5 * m * v² = 0.5 * 100 * (10² + 20² + 15²) = 0.5 * 100 * 725 = 36250
    expected_ke = 36250.0
    assert particle.kinetic_energy() == expected_ke
    
    # Test particle with zero velocity
    stationary_particle = DarkMatterParticle(mass=50)
    assert stationary_particle.kinetic_energy() == 0
    
    print("✓ DarkMatterParticle tests passed")


def test_dark_matter_halo():
    """Test DarkMatterHalo creation and methods."""
    print("Testing DarkMatterHalo...")
    
    # Test initialization
    halo = DarkMatterHalo(total_mass=1e12, scale_radius=20)
    assert halo.total_mass == 1e12
    assert halo.scale_radius == 20
    
    # Test density profile
    # At very small radius, density should be high
    density_near = halo.density_profile(1)
    density_far = halo.density_profile(100)
    assert density_near > density_far, "Density should decrease with radius"
    
    # Test rotation curve
    # Rotation velocity should be positive and reasonable
    v1 = halo.rotation_curve(10)
    v2 = halo.rotation_curve(20)
    assert v1 > 0
    assert v2 > 0
    
    # Test zero radius
    v_zero = halo.rotation_curve(0)
    assert v_zero == 0
    
    print("✓ DarkMatterHalo tests passed")


def test_calculate_dark_matter_percentage():
    """Test universe composition calculation."""
    print("Testing calculate_dark_matter_percentage...")
    
    composition = calculate_dark_matter_percentage()
    
    # Check that all components are present
    assert "dark_energy" in composition
    assert "dark_matter" in composition
    assert "ordinary_matter" in composition
    
    # Check reasonable values
    assert composition["dark_matter"] == 26.8
    assert composition["dark_energy"] == 68.3
    assert composition["ordinary_matter"] == 4.9
    
    # Check that total is approximately 100%
    total = sum(composition.values())
    assert abs(total - 100.0) < 0.1
    
    print("✓ calculate_dark_matter_percentage tests passed")


def test_wimps_properties():
    """Test WIMP properties function."""
    print("Testing wimps_properties...")
    
    props = wimps_properties()
    
    # Check that all expected properties are present
    assert "mass_range" in props
    assert "interaction" in props
    assert "stability" in props
    assert "detection" in props
    
    # Check that values are strings and not empty
    for key, value in props.items():
        assert isinstance(value, str)
        assert len(value) > 0
    
    print("✓ wimps_properties tests passed")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("Running Dark Matter Module Tests")
    print("=" * 60)
    print()
    
    test_dark_matter_particle()
    test_dark_matter_halo()
    test_calculate_dark_matter_percentage()
    test_wimps_properties()
    
    print()
    print("=" * 60)
    print("All tests passed successfully! ✓")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
