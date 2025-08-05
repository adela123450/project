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
texto = (
    "Hola, mi nombre es Adela Silva Gaitan, tengo 29 años, soy instructora SENA del programa de articulación con la media, en el programa Recursos humanos en el municipio de Villeta Cundinamarca. En mis tiempos libres me gusta leer, dormir y compartir con mis seres queridos."
    "Hola, mi nombre es Mauricio Vélez, tengo 48 años y soy Ingeniero de Sistemas.  Actualmente, me desempeño como instructor del programa de Articulación del SENA con la Educación Media, del Centro de la Innovación, la Agroindustria y la Aviación.  Dentro de mis pasatiempos favoritos está la Fotografía y los VideoJuegos."
    "Hola, mi nombre es Harold Marin, tengo 29 años y soy Ingeniero de Software.  Actualmente, me desempeño como instructor del programa de Articulación del SENA con la Educación Media, del Centro de la Innovación, la Agroindustria y la Aviación.  Dentro de mis pasatiempos favoritos estálos VideoJuegos."
    "Hola soy Haddy Moreno, tengo la edad de Cristo, soy ingeniera de sistemas, actualmente me desempeño como instructora Sena en el tecnólogo en Adso, mi hobby es bailar en especial Danza afrocolombiana"
)
#tokenizacion, convertimos el texto en una lista d epalbra sindividuales
palabras = word_tokenize(texto, language= "spanish")

#mostamos la lista de palbaras obtenidas
print(palabras)
