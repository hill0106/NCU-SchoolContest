#!/usr/bin/env python3
"""
Test Runner for NCU Alumni Employment Analysis

This script provides an easy way to run different types of tests
and generate comprehensive test reports.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ SUCCESS")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ FAILED")
        print(f"Error: {e}")
        if e.stdout:
            print("Output:")
            print(e.stdout)
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False

def run_unit_tests():
    """Run unit tests"""
    return run_command(
        "python -m pytest test_main.py -v --tb=short",
        "Unit Tests"
    )

def run_integration_tests():
    """Run integration tests"""
    return run_command(
        "python -m pytest test_main.py -v -m integration --tb=short",
        "Integration Tests"
    )

def run_all_tests():
    """Run all tests with coverage"""
    return run_command(
        "python -m pytest test_main.py -v --cov=main --cov-report=html --cov-report=term-missing",
        "All Tests with Coverage"
    )

def run_visualization_tests():
    """Run visualization tests"""
    return run_command(
        "python -m pytest test_main.py -v -m visualization --tb=short",
        "Visualization Tests"
    )

def run_data_tests():
    """Run data integrity tests"""
    return run_command(
        "python -m pytest test_main.py -v -m data --tb=short",
        "Data Integrity Tests"
    )

def run_performance_tests():
    """Run performance tests"""
    return run_command(
        "python -m pytest test_main.py -v -m slow --tb=short",
        "Performance Tests"
    )

def run_linting():
    """Run code linting"""
    return run_command(
        "python -m flake8 main.py test_main.py --max-line-length=100",
        "Code Linting"
    )

def run_formatting_check():
    """Check code formatting"""
    return run_command(
        "python -m black --check main.py test_main.py",
        "Code Formatting Check"
    )

def install_test_dependencies():
    """Install test dependencies"""
    return run_command(
        "pip install -r requirements-test.txt",
        "Installing Test Dependencies"
    )

def generate_test_report():
    """Generate comprehensive test report"""
    print("\n" + "="*60)
    print("GENERATING TEST REPORT")
    print("="*60)
    
    # Check if HTML coverage report exists
    if os.path.exists("htmlcov/index.html"):
        print("📊 Coverage report available at: htmlcov/index.html")
    
    # Check if test results XML exists
    if os.path.exists("test-results.xml"):
        print("📋 Test results XML available at: test-results.xml")
    
    print("\nTest Summary:")
    print("- Unit tests: Basic functionality testing")
    print("- Integration tests: Component interaction testing")
    print("- Data tests: Data integrity and validation")
    print("- Visualization tests: Plot generation testing")
    print("- Performance tests: Speed and memory usage")

def main():
    """Main test runner function"""
    parser = argparse.ArgumentParser(description="NCU Alumni Employment Analysis Test Runner")
    parser.add_argument("--type", choices=[
        "unit", "integration", "all", "visualization", "data", "performance", "lint", "format", "install"
    ], default="all", help="Type of tests to run")
    parser.add_argument("--install-deps", action="store_true", help="Install test dependencies first")
    
    args = parser.parse_args()
    
    print("🧪 NCU Alumni Employment Analysis Test Runner")
    print("="*60)
    
    # Install dependencies if requested
    if args.install_deps or args.type == "install":
        if not install_test_dependencies():
            print("❌ Failed to install dependencies. Exiting.")
            sys.exit(1)
        if args.type == "install":
            return
    
    # Run tests based on type
    success = True
    
    if args.type == "unit":
        success = run_unit_tests()
    elif args.type == "integration":
        success = run_integration_tests()
    elif args.type == "all":
        success = run_all_tests()
    elif args.type == "visualization":
        success = run_visualization_tests()
    elif args.type == "data":
        success = run_data_tests()
    elif args.type == "performance":
        success = run_performance_tests()
    elif args.type == "lint":
        success = run_linting()
    elif args.type == "format":
        success = run_formatting_check()
    
    # Generate report
    generate_test_report()
    
    # Exit with appropriate code
    if success:
        print("\n✅ All tests completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
