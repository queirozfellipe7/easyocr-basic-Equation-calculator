# easyocr-basic-calculator
PT-BR
O programa ler formulas de equacoes de 1º grau básicos de uma imagem e o resolve.
O código faz a utilização da biblioteca easyocr para fazer a leitura  dos dados da imagem e com funções simples da linguagem
python, diferencia as operações matemáticas e as executa.
Passos para execução:
1-instalar a biblioteca easyocr:
 pip install easyocr
2 - Especificar a imagem que será lida:
 resultado = reader.readtext('NOME-DA-IMAGEM.png',paragraph=False)
3 - executar o código.

EN
The program reads basic equation degree 1 from an image and solves them.
The code makes use of the easyocr library to read the image data and with simple language functions
python, differentiates the mathematical operations and executes them.
Steps for implementation:
1-install the easyocr library:
  pip install easyocr
2 - Specify the image to be read:
 resultado = reader.readtext('IMAGE-NAME.png',paragraph=False)
3 - run the code.
