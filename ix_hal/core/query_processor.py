"""
IX-Hal Domain-Specific Query Processor

Handles user queries related to AI, machine learning, robotics,
and autonomous system concepts.
"""

from ai_robotics_knowledge import AIRoboticsKnowledge

class IXHalQueryProcessor:
    def __init__(self):
        self.knowledge = AIRoboticsKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        # Recognize and extract the requested term
        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-Hal, your AI and Robotics specialist. "
                "Ask me to define or explain any concept from artificial intelligence, machine learning, or robotics."
            )

# Example usage
if __name__ == "__main__":
    processor = IXHalQueryProcessor()
    print(processor.process_query("What is artificial intelligence?"))
    print(processor.process_query("Define reinforcement learning"))
    print(processor.process_query("Explain robotics"))
