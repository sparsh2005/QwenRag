import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from agents.query_rewriter import decompose_query
from agents.planning_agent import plan_retrieval_strategy
from agents.response_generator import synthesize_responses
from main import main

class TestRAGSystem(unittest.TestCase):
    def setUp(self):
        # Sample test queries of varying complexity
        self.simple_query = "What is Qwen?"
        self.complex_query = "How does Qwen compare to other LLMs in terms of performance and multilingual capabilities?"
        self.multi_part_query = "What are the key features of Qwen and how does it integrate with vector databases?"

    def test_query_decomposition(self):
        """Test if complex queries are properly decomposed"""
        sub_queries = decompose_query(self.complex_query)
        self.assertIsInstance(sub_queries, list)
        self.assertGreater(len(sub_queries), 1)
        print("\n✅ Query Decomposition Test:")
        print(f"Original query: {self.complex_query}")
        print(f"Decomposed into: {sub_queries}")

    def test_retrieval_planning(self):
        """Test if retrieval strategies are properly planned"""
        sub_queries = decompose_query(self.complex_query)
        strategy = plan_retrieval_strategy(sub_queries)
        self.assertIsInstance(strategy, dict)
        self.assertEqual(len(strategy), len(sub_queries))
        print("\n✅ Retrieval Planning Test:")
        print(f"Strategy for queries: {strategy}")

    def test_response_synthesis(self):
        """Test if responses are properly synthesized"""
        sample_responses = [
            {"query": "What is Qwen?", "response": "Qwen is a multilingual LLM by Alibaba."},
            {"query": "What are its capabilities?", "response": "It supports multiple languages and can be run locally."}
        ]
        final_response = synthesize_responses(sample_responses)
        self.assertIsInstance(final_response, str)
        self.assertGreater(len(final_response), 0)
        print("\n✅ Response Synthesis Test:")
        print(f"Synthesized response: {final_response}")

    def test_full_pipeline(self):
        """Test the complete RAG pipeline with a complex query"""
        with patch('builtins.input', return_value=self.complex_query):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                self.assertIn("Final Answer", output)
                print("\n✅ Full Pipeline Test:")
                print(f"Pipeline output: {output}")

def run_tests():
    """Run all tests with detailed output"""
    print("\n🧪 Starting RAG System Tests...")
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests() 