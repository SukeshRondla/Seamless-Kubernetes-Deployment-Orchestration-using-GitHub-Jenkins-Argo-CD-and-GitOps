#!/usr/bin/env python
"""
Django management script for running administrative tasks.
"""

import os
import sys
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoApp.settings')
    
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH. Did you forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()
