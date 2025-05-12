#!/usr/bin/env python
import os
import sys
import warnings
import argparse
from datetime import datetime

from crew import AiPocCrewAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(company_name: str):
    """
    Run the crew.
    """
    inputs = {
        'company_name': company_name,
        'current_year': str(datetime.now().year),
        'current_date': str(datetime.now().strftime("%Y%m%d"))
    }
    
    try:
        crew_instance = AiPocCrewAi().build_crew(inputs)
        crew_instance.kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(company_name: str):
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_name': company_name,
        'current_year': str(datetime.now().year),
        'current_date': str(datetime.now().strftime("%Y%m%d"))
    }
    try:
        AiPocCrewAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiPocCrewAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'company_name': company_name,
        "current_year": str(datetime.now().year)
    }
    
    try:
        AiPocCrewAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run CrewAI workflow for a given company.")
    parser.add_argument("--company_name", required=True, help="Name of the company to analyze")

    args = parser.parse_args()
    run(args.company_name)