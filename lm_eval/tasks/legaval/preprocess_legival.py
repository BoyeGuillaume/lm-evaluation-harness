def doc_to_text(doc) -> str:
    option_choices = doc["options"]
    answers = "".join((f"{k}. {v}\n") for k, v in option_choices.items())
    return f"Question: {doc['question']}\n{answers}Answer:"

def doc_to_target(doc) -> int:
    return ord(doc["correct_options_idx"]) - 0x41