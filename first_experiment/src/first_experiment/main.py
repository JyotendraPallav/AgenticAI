# #!/usr/bin/env python
# import sys
# import warnings

# from datetime import datetime

# from first_experiment.crew import FirstExperiment

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs',
#         'current_year': str(datetime.now().year)
#     }
    
#     try:
#         FirstExperiment().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         FirstExperiment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         FirstExperiment().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
    
#     try:
#         FirstExperiment().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from first_experiment.crew import SorterTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A simple file sorting system that allows users to sort files based on their extensions.
The system should allow users to specify a directory and a list of file extensions to sort.
The system should create subdirectories for each file extension and move the files into the corresponding subdirectory.
# The system should handle cases where the specified directory does not exist or is empty.
# The system should be able to report the number of files sorted and the number of files that could not be sorted.
# The system should be able to handle files with no extension and move them to a separate "no_extension" subdirectory.
# The system should be able to handle files with multiple extensions and move them to the subdirectory corresponding to the last extension.
# The system should be able to handle files with uppercase extensions and move them to the subdirectory corresponding to the lowercase version of the extension.
# The system should be able to handle files with special characters in their names and move them to the corresponding subdirectory.
# The system should be able to handle files with spaces in their names and move them to the corresponding subdirectory.
# The system should be able to handle files with long names and move them to the corresponding subdirectory.
# The system should be able to handle files with hidden extensions and move them to the corresponding subdirectory.
# The system should be able to handle files with no name and move them to the corresponding subdirectory.
"""
module_name = "Sorter.py"
class_name = "Sorter"




def run():
    """
    Run the Sorter crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    print("Starting the Sorter crew...")
    result = SorterTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()