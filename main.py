from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Elon Reeve Musk (Pretoria, 28 giugno 1971) è un imprenditore e politico sudafricano con cittadinanza canadese naturalizzato statunitense.

    Ricopre i ruoli di fondatore, amministratore delegato e direttore tecnico della compagnia aerospaziale SpaceX,[2] fondatore di The Boring Company,[3] cofondatore di Neuralink e OpenAI,[4] amministratore delegato e product architect della multinazionale automobilistica Tesla,[5] proprietario e presidente di X (ex Twitter).[6] Ha inoltre proposto un sistema di trasporto superveloce conosciuto come Hyperloop One, che è stata posta in liquidazione il 21 dicembre 2023.[7] Tramite SpaceX gestisce Starlink, una costellazione di satelliti che ha l'obiettivo di fornire Internet ad alta velocità e bassa latenza a tutto il pianeta.[8]

    Secondo Forbes, al 7 febbraio 2026, con un patrimonio stimato di 849,3 miliardi di dollari, risulta essere la persona più ricca del mondo.[9][10][11]

    Dal 20 gennaio al 29 maggio 2025 è stato a capo del Dipartimento dell'Efficienza Governativa statunitense.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template = summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
