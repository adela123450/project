# importar la libreria NLTK
import nltk

#desde NLTK, importamos las stopword que son las palabras comunes en un idioma
from nltk.corpus import stopwords

#descargamos la lista de palabras vacias stopwords
nltk.download("stopwords")

#guardar en una variable la lista de stopwords en español
lista_de_stopwords = stopwords.words("spanish")

#Imprimir la lista de stopwords
print(lista_de_stopwords)

