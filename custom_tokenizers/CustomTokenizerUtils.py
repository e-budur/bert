from unicode_tr import unicode_tr
import string
import six

def align_cases(input_word_form, parsed_word_form):

    input_word_form = unicode_tr(input_word_form)
    parsed_word_form = unicode_tr(parsed_word_form)

    i = 0
    j = 0
    resulting_word_characters = []
    subword_unit = []
    while i < len(input_word_form) and j < len(parsed_word_form):
        if input_word_form[i] == parsed_word_form[j] or input_word_form[i] == unicode_tr(parsed_word_form[j]).upper():
            subword_unit.append(input_word_form[i])
            i += 1
            j += 1
            continue

        if input_word_form[i] in string.punctuation:
            i += 1

        if parsed_word_form[j] == ' ':
            j += 1 #skip delimiter in parsed word
            resulting_word_characters.append(''.join(subword_unit))
            subword_unit = []
            continue

        #token with a non-conventional pattern will reach here. Will skip aligning their cases.
        return parsed_word_form

    if len(subword_unit)>0:
        resulting_word_characters.append(''.join(subword_unit))

    resulting_word = ' '.join(resulting_word_characters)
    return resulting_word

def convert_to_unicode(text):
  """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
  if six.PY3:
    if isinstance(text, str):
      return text
    elif isinstance(text, bytes):
      return text.decode("utf-8", "ignore")
    else:
      raise ValueError("Unsupported string type: %s" % (type(text)))
  elif six.PY2:
    if isinstance(text, str):
      return text.decode("utf-8", "ignore")
    elif isinstance(text, unicode):
      return text
    else:
      raise ValueError("Unsupported string type: %s" % (type(text)))
  else:
    raise ValueError("Not running on Python2 or Python 3?")