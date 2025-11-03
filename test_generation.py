#!/usr/bin/env python3
"""Test if data generation works"""

from elasticsearch import Elasticsearch
from generator_advanced import ObservabilityDataGenerator

# Replace with your credentials
CLOUD_ID = "your-cloud-id-here"
API_KEY = "your-api-key-here"

print("Testing Elasticsearch connection...")
es = Elasticsearch(cloud_id=CLOUD_ID, api_key=API_KEY)

try:
    info = es.info()
    print(f"✅ Connected to: {info['cluster_name']}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

print("\nTesting data generation...")
generator = ObservabilityDataGenerator(es, 'gaming')

print("Generating 1 trace...")
try:
    generator.generate_trace()
    print("✅ Trace generated")
except Exception as e:
    print(f"❌ Trace generation failed: {e}")

print("\nGenerating 1 log...")
try:
    generator.generate_log()
    print("✅ Log generated")
except Exception as e:
    print(f"❌ Log generation failed: {e}")

print("\nChecking stats...")
stats = generator.get_stats()
print(f"Stats: {stats}")

print("\nChecking indices...")
try:
    indices = es.cat.indices(index="apm*,logs*,synthetics*", format="json")
    for idx in indices:
        print(f"  {idx['index']}: {idx['docs.count']} docs")
except Exception as e:
    print(f"Error checking indices: {e}")