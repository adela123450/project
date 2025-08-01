#vamos a importar NLTK que nos va a ayudar a trabajar con lenguaje natural
import nltk
nltk.download('punkt_tab')
#definir la ruta donde se almacenaran los datos descargados
nltk.data.path.append(r'C:\Users\adela\AppData\Roaming\nltk_data')
#descargamos la lista de palabras vacias stopwords que son palabras comunes
nltk.download("stopwords")

#importar  la funcion que divide un texto en palabras
from nltk.tokenize import word_tokenize
#importar la lista de palabras vacias stopwords en español
from nltk.corpus import stopwords
#importar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

#definimos un texto en español que queremos analizar
texto = """

hola, soy Adela Silva, me gusta la programacion, 
vivo en villeta cundinamarca
Mi compañero es Jheyson, el es profesor de talento tech
"""
#tokenizacion, convertimos el texto en una lista d epalbra sindividuales
palabras = word_tokenize(texto, language= "spanish")

#mostamos la lista de palbaras obtenidas
print(palabras)
