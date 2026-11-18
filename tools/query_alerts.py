#!/usr/bin/env python3
"""Fetch bounded Wazuh indexer alerts or inspect an offline synthetic response."""
import argparse
import base64
import json
import os
from pathlib import Path
import ssl
import sys
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture', type=Path, help='Read a local JSON response instead of connecting')
    args = parser.parse_args()
    try:
        if args.fixture:
            data = json.loads(args.fixture.read_text(encoding='utf-8'))
        else:
            required = ('WAZUH_INDEXER_URL', 'WAZUH_INDEXER_USER', 'WAZUH_INDEXER_PASSWORD', 'WAZUH_CA_FILE')
            missing = [key for key in required if not os.environ.get(key)]
            if missing:
                parser.error('Missing environment variables: ' + ', '.join(missing))
            url = os.environ['WAZUH_INDEXER_URL'].rstrip('/')
            if not url.startswith('https://'):
                parser.error('WAZUH_INDEXER_URL must use HTTPS')
            token = base64.b64encode((os.environ['WAZUH_INDEXER_USER'] + ':' + os.environ['WAZUH_INDEXER_PASSWORD']).encode()).decode()
            request = urllib.request.Request(url + '/wazuh-alerts-*/_search', data=(ROOT / 'queries/recent-alerts.json').read_bytes(), headers={'Authorization': 'Basic ' + token, 'Content-Type': 'application/json'}, method='POST')
            context = ssl.create_default_context(cafile=os.environ['WAZUH_CA_FILE'])
            with urllib.request.urlopen(request, context=context, timeout=20) as response:
                data = json.load(response)
        hits = data['hits']['hits']
        print('Returned alerts:', len(hits))
        for hit in hits:
            source = hit.get('_source', {})
            rule = source.get('rule', {})
            print('{} | {} | level {} | {}'.format(source.get('timestamp', '?'), source.get('agent', {}).get('name', '?'), rule.get('level', '?'), rule.get('description', '?')))
        return 0
    except (OSError, ValueError, KeyError, urllib.error.URLError) as exc:
        print('Unable to retrieve or parse alerts: {}'.format(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
