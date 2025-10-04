"""
Gerador de QR Code Moderno para o Site de Casamento
Gera um QR Code clean com bordas arredondadas
"""

import qrcode
from PIL import Image, ImageDraw

def criar_qrcode_moderno(url, nome_arquivo='qrcode_casamento.png'):
    """
    Cria um QR Code moderno com bordas arredondadas
    
    Args:
        url: URL do site
        nome_arquivo: Nome do arquivo de saída
    """
    
    # Configuração do QR Code
    qr = qrcode.QRCode(
        version=1,  # Tamanho automático
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta correção de erros
        box_size=15,  # Tamanho de cada "quadradinho"
        border=2,  # Borda mínima (vamos adicionar nossa própria borda depois)
    )
    
    # Adiciona os dados
    qr.add_data(url)
    qr.make(fit=True)
    
    # Cria a imagem do QR Code
    img = qr.make_image(
        fill_color="#000000",  # Cor marrom (cor secundária do site)
        back_color="white"
    )
    
    # Converte para RGB
    img = img.convert('RGB')
    
    # Adiciona margem branca ao redor
    margem = 40
    largura_total = img.width + (margem * 2)
    altura_total = img.height + (margem * 2)
    
    # Cria uma nova imagem com margem
    img_final = Image.new('RGB', (largura_total, altura_total), 'white')
    
    # CORREÇÃO: Define a área de colagem corretamente
    area_colagem = (margem, margem, margem + img.width, margem + img.height)
    img_final.paste(img, area_colagem)
    
    # Cria uma máscara com bordas arredondadas
    mask = Image.new('L', (largura_total, altura_total), 0)
    draw = ImageDraw.Draw(mask)
    
    # Desenha um retângulo com cantos arredondados
    raio = 50  # Raio dos cantos arredondados
    draw.rounded_rectangle(
        [(0, 0), (largura_total, altura_total)],
        radius=raio,
        fill=255
    )
    
    # Cria imagem final com fundo arredondado
    resultado = Image.new('RGB', (largura_total, altura_total), 'white')
    resultado.paste(img_final, (0, 0), mask)
    
    # Salva a imagem
    resultado.save(nome_arquivo, quality=95, optimize=True)
    print(f"✅ QR Code criado com sucesso: {nome_arquivo}")
    print(f"📱 Tamanho: {largura_total}x{altura_total} pixels")
    print(f"🔗 URL: {url}")
    
    return resultado


# Execução
if __name__ == "__main__":
    url_site = 'https://vinisoarescastro.github.io/sara-e-lucas/'
    
    print("🎨 Gerando QR Code moderno...")
    print("─" * 50)
    
    criar_qrcode_moderno(url_site, 'qrcode_site_casamento.png')
    
    print("─" * 50)
    print("🎉 Pronto! Agora é só usar a imagem gerada!")