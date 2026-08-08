import re
import string


def clean_text(text):
    """
    Clean tweet text for NLP classification.

    Parameters
    ----------
    text : str
        Raw tweet text.

    Returns
    -------
    str
        Cleaned tweet text.
    """

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    text = re.sub(r"\s+", " ", text).strip()

    return text