




def GetLastNumTextFromText(TextToGet, WholeTextWithText):


    TextLenGetFROMLENMinus = len(WholeTextWithText) - len(TextToGet)

    EndText = WholeTextWithText[TextLenGetFROMLENMinus:]

    return EndText





TextToGet =  'are the same file'

WholeTextWithText = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerFiles\\Temp\\temp_PASSOS PARA ATIVAÇÃO DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) '+"(1) (1) (4) (1) (1).pdf' and 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerFiles\\Temp\\temp_PASSOS PARA ATIVAÇÃO DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1).pdf' are the same file"

print(GetLastNumTextFromText(TextToGet, WholeTextWithText))

