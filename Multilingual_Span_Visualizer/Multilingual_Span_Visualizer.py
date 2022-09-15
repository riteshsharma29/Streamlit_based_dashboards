from typing import List, Sequence, Tuple, Optional, Dict, Union, Callable
import streamlit as st
import spacy
from spacy import displacy
import pandas as pd

NER_ATTRS = ["text", "label_", "start", "end", "start_char", "end_char"]

# this function is used from spacy-streamlit module
def get_html(html: str):
    """Convert HTML so it can be rendered."""
    WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    return WRAPPER.format(html)

# this function is used and modified from spacy-streamlit module
def visualize_ner(
    doc: Union[spacy.tokens.Doc, List[Dict[str, str]]],
    *,
    labels: Sequence[str] = tuple(),
    attrs: List[str] = NER_ATTRS,
    show_table: bool = True,
    title: Optional[str] = "Named Entities",
    colors: Dict[str, str] = {},
    key: Optional[str] = None,
    manual: bool = False,
    displacy_options: Optional[Dict] = None,
):
    if not displacy_options:
        displacy_options = dict()
    if colors:
        displacy_options["colors"] = colors

    if title:
        st.header(title)

    if manual:
        if show_table:
            st.warning(
                "When the parameter 'manual' is set to True, the parameter 'show_table' must be set to False."
            )
        if not isinstance(doc, list):
            st.warning(
                "When the parameter 'manual' is set to True, the parameter 'doc' must be of type 'list', not 'spacy.tokens.Doc'."
            )
    else:
        labels = labels or [ent.label_ for ent in doc.ents]

    if not labels:
        st.warning("The parameter 'labels' should not be empty or None.")
    else:
        exp = st.sidebar.expander("Select entity labels")
        label_select = exp.multiselect(
            "Entity labels",
            options=labels,
            default=list(labels),
            key=f"{key}_ner_label_select",
        )
        displacy_options["ents"] = label_select
        html = displacy.render(
            doc,
            style="ent",
            options=displacy_options,
            manual=manual,
        )
        style = "<style>mark.entity { display: inline-block }</style>"
        st.write(f"{style}{get_html(html)}", unsafe_allow_html=True)
        if show_table:
            data = [
                [str(getattr(ent, attr)) for attr in attrs]
                for ent in doc.ents
                if ent.label_ in label_select
            ]
            if data:
                df = pd.DataFrame(data, columns=attrs)
                st.dataframe(df)


st.title("Multilingual Span Visualization")
language = st.sidebar.radio(
    "Select Language",
    ('Dutch','English', 'French', 'German', 'Italian','Spanish', 'Swedish'))

if language == "Dutch":
    nlp = spacy.load("nl_core_news_sm")
elif language == "English":
    nlp = spacy.load("en_core_web_sm")
elif language == "French":
    nlp = spacy.load("fr_core_news_sm")
elif language == "German":
    nlp = spacy.load("de_core_news_sm")
elif language == "Italian":
    nlp = spacy.load("it_core_news_sm")
elif language == "Spanish":
    nlp = spacy.load("es_core_news_sm")
elif language == "Swedish":
    nlp = spacy.load("sv_core_news_sm")

inputtext = st.text_input("Enter text to analyze below")
doc = nlp(inputtext)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels)