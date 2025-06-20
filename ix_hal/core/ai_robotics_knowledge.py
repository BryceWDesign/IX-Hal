"""
IX-Hal Core AI and Robotics Knowledge Module

Contains essential knowledge definitions and formal descriptions related
to artificial intelligence, machine learning, robotics, and autonomous systems.

Part of the IX-Gibson sibling AI network.
"""

class AIRoboticsKnowledge:
    def __init__(self):
        self.facts = {
            "artificial intelligence": "The simulation of human intelligence processes by machines, especially computer systems.",
            "neural network": "A computational model based on the structure and functions of biological neural networks.",
            "machine learning": "A subfield of AI involving algorithms that learn patterns from data and improve over time.",
            "reinforcement learning": "An ML technique where agents learn by receiving rewards or penalties for their actions.",
            "robotics": "An interdisciplinary branch of engineering and science that includes mechanical engineering, electrical engineering, and computer science to design and operate robots.",
            "autonomous system": "A system capable of performing tasks or functions without human intervention.",
            "backpropagation": "A training algorithm for neural networks that calculates the gradient of the loss function with respect to weights.",
            "sensor fusion": "The process of combining sensory data from multiple sources to produce more accurate information."
        }

    def get_fact(self, term: str) -> str:
        term_lower = term.lower().strip()
        return self.facts.get(term_lower, f"Sorry, I don't yet have an entry for '{term}'.")

# Example test
if __name__ == "__main__":
    ak = AIRoboticsKnowledge()
    print(ak.get_fact("Neural network"))
    print(ak.get_fact("Backpropagation"))
    print(ak.get_fact("Singularity"))
