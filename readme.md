# Este arquivo está **DESATUALIZADO** e só está sendo mantido por questões de legado.
Esse programa requer instalação de algum Visual Studio pois a header "io.h" de c++ é exclusiva da Microsoft, ao que parece. 
O resto o g++ deve tomar conta. Ainda NÃO adaptado à RaspberryPi, que vai utilizar a header "WiringPi.h"

Python precisa de nltk e pyphen. No ambiente do python, rode o seguinte código:
#
import nltk
nltk.download()
#
E baixe o arquivo "floresta" de lá.
