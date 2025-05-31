from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

llm = Ollama(model="mistral")  # or "llama2", "gemma", etc.

# Step 1: Refine the idea
refine_prompt = PromptTemplate(
    input_variables=["idea"],
    template="Refine this project idea into a clear, detailed description:\n{idea}"
)
refine_chain = LLMChain(llm=llm, prompt=refine_prompt)

# Step 2: Summarize the project
summary_prompt = PromptTemplate(
    input_variables=["description"],
    template="Summarize this project in one sentence:\n{description}"
)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

# Step 3: Generate a project name
name_prompt = PromptTemplate(
    input_variables=["description"],
    template="Suggest a catchy, creative name for this project:\n{description}"
)
name_chain = LLMChain(llm=llm, prompt=name_prompt)

# Step 4: Write an elevator pitch
pitch_prompt = PromptTemplate(
    input_variables=["name", "summary"],
    template="Write a short, compelling elevator pitch for a project called '{name}':\n{summary}"
)
pitch_chain = LLMChain(llm=llm, prompt=pitch_prompt)

def main():
    idea = input("Enter your project idea: ")

    description = refine_chain.run(idea=idea)
    print("\nRefined Description:\n", description)

    summary = summary_chain.run(description=description)
    print("\nOne-Sentence Summary:\n", summary)

    name = name_chain.run(description=description)
    print("\nProject Name:\n", name)

    pitch = pitch_chain.run(name=name, summary=summary)
    print("\nElevator Pitch:\n", pitch)

if __name__ == "__main__":
    main()