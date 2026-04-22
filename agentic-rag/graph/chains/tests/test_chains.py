from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from graph.chains.generation import generation_chain
from ingestion import retriever
from graph.chains.hallucination_grader import GradeHallucinations, hallucination_grader

def test_retrieval_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"

def test_retrieval_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content


    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "how to make pizza", "document": doc_txt}
    )

    assert res.binary_score == "no"

def test_generation_chain() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    generation = generation_chain.invoke({"question": question, "context": docs})

def test_hallucination_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)

    generation = generation_chain.invoke({"question": question, "context": docs})

    res: GradeHallucinations = hallucination_grader.invoke(
        {"documents": docs, "generation": generation}
    )

    assert res.binary_score

def test_hallucination_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)

    generation = generation_chain.invoke({"question": question, "context": docs})

    res: GradeHallucinations = hallucination_grader.invoke(
        {"documents": docs, "generation": "in order to make pizza you need to first start with the dough"}
    )

    assert not res.binary_score
