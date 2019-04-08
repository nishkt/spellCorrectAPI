# spellCorrectAPI

To use this, first spellChecker would need to be installed using :

    pip install pyspellchecker

If you are using virtual environments, it is recommended to use ``pipenv`` to
combine pip and virtual environments:

    pipenv install pyspellchecker
    
Run the flask app. On the url, it should end with /spellCorrect/<word> where the <word> is the word that you would like to get spell checked and receive alternate word suggestions.
