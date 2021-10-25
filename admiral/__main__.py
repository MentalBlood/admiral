import sys
import json
from admiral import Parsers



p = Parsers(description='CLI for testing only')
p.load(['test'])

result = p.run()
sys.stdout.write(json.dumps(result))