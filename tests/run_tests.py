import sys
import os
import unittest
from dotenv import load_dotenv

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from tests.test_rag_system import TestRAGSystem

load_dotenv()

def main():
    print("\n🔍 Testing the Agentic RAG System")
    print("=================================")
    
    # Create a test suite and add the test cases
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRAGSystem))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    print("\n📝 Example Queries to Try:")
    print("-------------------------")
    example_queries = [
        "What is Qwen and how does it compare to other LLMs?",
        "Explain how Qwen integrates with vector databases and what are its key features?",
        "What are the advantages of using Qwen for multilingual tasks?",
        "How does the Agentic RAG system work with Qwen and what makes it different from traditional RAG?",
    ]
    
    for i, query in enumerate(example_queries, 1):
        print(f"\n{i}. {query}")
    
    print("\nTo test the system with these queries:")
    print("1. Run 'python main.py'")
    print("2. Enter any of the example queries when prompted")
    print("3. Observe how the system decomposes, retrieves, and synthesizes the response")

if __name__ == "__main__":
    main() 