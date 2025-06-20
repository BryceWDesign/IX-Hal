"""
IX-Hal CLI Interface

Command-line access to the IX-Hal reflexive logic engine for
real-time diagnostics and AGI safety checks.
"""

import sys
from core.query_processor import IXHalQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<Your input command or query>\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXHalQueryProcessor()
    result = processor.process_query(query)

    print("\n🤖 IX-Hal Reflexive Evaluation")
    print(f"Input: {result['input']}")
    print(f"Directive Type: {result['directive_type']}")
    print(f"Risk Score: {result['risk_score']}")
    print(f"System Action: {result['system_action']}")

if __name__ == "__main__":
    main()
