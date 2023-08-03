import pytesseract
from PIL import Image

def extrair_texto_da_imagem(caminho_da_imagem):
    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Extrair texto usando pytesseract
    texto = pytesseract.image_to_string(imagem)

    # Exibir o texto extraído
    print("Texto na imagem:")
    print(texto)

    # Retornar o texto (opcional)
    return texto

if __name__ == "__main__":
    caminho_da_imagem = "E:/Python/Projetos/imagem\155832.jpg"  # Substitua pelo caminho correto da sua imagem
    texto_extraido = extrair_texto_da_imagem(caminho_da_imagem)
