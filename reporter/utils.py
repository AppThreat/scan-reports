def auto_text_highlight(text):
    """
    Automatically highlight interesting parts in the text
    :param text:
    :return:
    """
    text = text.replace("In class", "<span class='bg-dark chip'>Class</span>")
    text = text.replace("In method", "<span class='bg-dark chip'>Method</span>")
    text = text.replace("At ", "<span class='bg-dark chip'>File</span>")
    text = text.replace("line ", "<span class='bg-dark chip'>line</span>")
    text = text.replace("\n", "<br/>")
    return text
