import os
import argparse
from dotenv import load_dotenv

# Import the correct OpenAI class
from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


def main():
    # Load environment variables
    load_dotenv()

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="return a list of numbers", help="Specify the task for the code to perform")
    parser.add_argument("--language", default="python", help="Specify the programming language")
    args = parser.parse_args()

    # Create the OpenAI client instance
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Assuming you have the API key in a .env file

    # Define the code prompt template
    code_prompt = PromptTemplate(
        input_variables=["task", "language"],
        template="Write a very short {language} function that will {task}."
    )

    # Define the test prompt template
    test_prompt = PromptTemplate(
        input_variables=["language", "code"],
        template="Write a test for the following {language} code:\n {code}"
    )

    # Create the code generation chain
    code_chain = LLMChain(
        llm=llm,
        prompt=code_prompt,
        output_key="code"
    )

    # Create the test generation chain
    test_chain = LLMChain(
        llm=llm,
        prompt=test_prompt,
        output_key="test"
    )

    # Create the sequential chain
    chain = SequentialChain(
        chains=[code_chain, test_chain],
        input_variables=["task", "language"],
        output_variables=["test", "code"]
    )

    # Run the chain with user-provided arguments
    result = chain({
        "language": args.language,
        "task": args.task
    })

    # Print the generated code and test
    print(">>>>>> GENERATED CODE")
    print(result["code"])

    print(">>>>>> GENERATED TEST")
    print(result["test"])


if __name__ == "__main__":
    main()
















## This is the first stategy where will i will get some error message in that case the openai api  will not working

# import os
# from dotenv import load_dotenv
# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# from dotenv import load_dotenv
# import argparse



# load_dotenv()

# parser = argparse.ArgumentParser()
# parser.add_argument("--task", default="return a list of numbers")
# parser.add_argument("--language", default="python")
# args = parser.parse_args()

# llm = OpenAI()

# code_prompt = PromptTemplate(
#     input_variables=["task", "language"],
#     template="Write a very short {language} function that will {task}."
# )

# # Chain with series in seqentialchain

# test_prompt = PromptTemplate(
#     input_variables = ["language", "code"],
#     template = "Write a test for the following {language} code:\n {code}"
# )
# code_chain = LLMChain(
#     llm=llm,
#     prompt=code_prompt,
#     output_key = "code"
# )

# test_chain = LLMChain(
#     llm = llm,
#     prompt = test_prompt,
#     output_key = "test"
# )

# chain = SequentialChain(
#     chains = [code_chain, test_chain],
#     input_variables = ["task", "language"],
#     output_variables = ["test", "code"]

# )

# result = chain({
#     "language": args.language,
#     "task": args.task
# })

# print(">>>>>> GENERATED CODE")
# print(result["code"])


# print(">>>>>> GENERATED TEST")
# print(result["test"])



