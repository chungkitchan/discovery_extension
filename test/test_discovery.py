#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test
"""

import os
from pathlib import Path

import pytest

import discovery_extension

from discovery_extension.discovery import DiscoveryV2Ext
from discovery_extensions.discovery import ingest_documents
from discovery_extensions.discovery import download_all_documents
