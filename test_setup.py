#!/usr/bin/env python3
"""
Test script to verify the pkg_resources fix
"""
import sys
import subprocess

def test_pkg_resources():
    """Test if pkg_resources can be imported"""
    try:
        import pkg_resources
        print("✓ pkg_resources is available")
        return True
    except ImportError as e:
        print(f"✗ pkg_resources failed: {e}")
        return False

def test_setuptools():
    """Test if setuptools is available"""
    try:
        import setuptools
        print(f"✓ setuptools version: {setuptools.__version__}")
        return True
    except ImportError as e:
        print(f"✗ setuptools failed: {e}")
        return False

def install_requirements():
    """Install requirements using pip"""
    print("Installing required packages...")
    packages = [
        'setuptools>=68.0.0',
        'crewai==0.28.8', 
        'crewai_tools==0.1.6',
        'langchain_community==0.0.29'
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            return False
    return True

def test_crewai():
    """Test if CrewAI can be imported"""
    try:
        from crewai import Agent, Task, Crew
        print("✓ CrewAI imported successfully!")
        return True
    except ImportError as e:
        print(f"✗ CrewAI import failed: {e}")
        return False

def main():
    print("Testing Multi-Agent Researcher Setup...\n")
    
    # Test 1: Check pkg_resources
    print("1. Testing pkg_resources...")
    pkg_resources_ok = test_pkg_resources()
    
    # Test 2: Check setuptools
    print("\n2. Testing setuptools...")
    setuptools_ok = test_setuptools()
    
    # If pkg_resources fails, try to install setuptools
    if not pkg_resources_ok:
        print("\n3. Installing/upgrading setuptools...")
        if install_requirements():
            print("Retesting pkg_resources...")
            pkg_resources_ok = test_pkg_resources()
    
    # Test 3: Try to install and import CrewAI
    print("\n4. Testing CrewAI...")
    crewai_ok = test_crewai()
    
    if not crewai_ok:
        print("Installing CrewAI packages...")
        if install_requirements():
            print("Retesting CrewAI...")
            crewai_ok = test_crewai()
    
    # Summary
    print(f"\n{'='*50}")
    print("SETUP VERIFICATION SUMMARY:")
    print(f"pkg_resources: {'✓ PASS' if pkg_resources_ok else '✗ FAIL'}")
    print(f"setuptools: {'✓ PASS' if setuptools_ok else '✗ FAIL'}")
    print(f"CrewAI: {'✓ PASS' if crewai_ok else '✗ FAIL'}")
    
    if pkg_resources_ok and crewai_ok:
        print("\n🎉 ALL TESTS PASSED! The setup is working correctly.")
        print("You can now run the Jupyter notebook without pkg_resources errors.")
    else:
        print("\n⚠️  Some tests failed. Please check the error messages above.")

if __name__ == "__main__":
    main()