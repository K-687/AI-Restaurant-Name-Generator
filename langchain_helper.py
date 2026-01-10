from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
import os
load_dotenv()

CEREBRAS_API_KEY=os.getenv("CEREBRAS_API_KEY")

#repo_id="Norquinal/Mistral-7B-claude-instruct"
#repo_id="DeepMount00/Mistral-Ita-7b"
# noinspection PyArgumentList
#llm=HuggingFaceEndpoint(repo_id=repo_id,temperature=0.9,max_new_tokens=50)

# noinspection PyTypeChecker
llm = ChatOpenAI(
    api_key=CEREBRAS_API_KEY,
    base_url="https://api.cerebras.ai/v1",
    model="gpt-oss-120b"
)

# noinspection PyTypeChecker
def generate_restaurant_name_and_items(cuisine):
    # Chain 1:Restaurant Name
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest exactly ONE fancy restaurant name."
                 "Return ONLY the restaurant name as plain text."
                 "Do NOT include explanations, descriptions, newlines, or additional words."
    )

    name_chain = (prompt_name | llm | RunnableLambda(lambda x: {"restaurant_name": x}))

    # chain 2:Menu Items lambda x: {"restaurant_name": x}
    prompt_menu = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest menu items for the restaurant named '{restaurant_name}'."
                 "Return ONLY the menu items as a comma-separated list in one single line."
                 "Do NOT add bullets, numbering, extra text, headings, or newlines."
    )

    menu_chain = (prompt_menu | llm | RunnableLambda(lambda x: {"menu_items": x}))

    full_chain = (
            name_chain
            | RunnablePassthrough.assign(
        menu_items=lambda out: menu_chain.invoke(
            {"restaurant_name": out["restaurant_name"]}
        )["menu_items"]
    )
    )

    response = full_chain.invoke({"cuisine": cuisine })
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Chinese"))