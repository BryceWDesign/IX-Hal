"""
IX-Hal CLI Entry Point

Allows command-line querying of IX-Hal AI and robotics knowledge.
Prints responses directly to terminal.
"""

import sys
from core.query_processor import IXHalQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your AI or robotics question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXHalQueryProcessor()
    response = processor.process_query(query)

    print("\n🤖 IX-Hal Response 🤖")
    print(response)

if __name__ == "__main__":
    main()
