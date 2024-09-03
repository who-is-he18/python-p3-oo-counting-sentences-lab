#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the setter to initialize

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print ("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        sentences = re.findall(r'[^.!?]+[.!?]', self._value)
        return len(sentences)