# Image Grayscale Converter & Histogram

Este projeto é uma ferramenta simples em Python que utiliza processamento de imagem para converter fotos coloridas em escala de cinza e gerar um histograma de intensidade de pixels.

## 🚀 Funcionalidades

*   **Carregamento de Imagem:** Leitura robusta de arquivos de imagem via OpenCV.
*   **Conversão de Cores:** Transformação do espaço de cores BGR para tons de cinza.
*   **Visualização:** Exibição da imagem processada utilizando Matplotlib.
*   **Análise de Dados:** Geração de um histograma para análise da distribuição de intensidade dos pixels.

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **OpenCV (`cv2`):** Biblioteca principal para manipulação e processamento de visão computacional.
*   **Matplotlib:** Utilizada para a plotagem de gráficos e exibição de imagens.

## 📋 Pré-requisitos

Antes de executar o script, você precisará instalar as dependências necessárias:
```bash
pip install opencv-python matplotlib
```

## 📂 Como Usar

Certifique-se de que a imagem que deseja processar (ex: goat.jpg) esteja na mesma pasta do script ou ajuste o caminho no código.

Execute o arquivo principal:
python nome_do_seu_arquivo.py

## 🏗️ Estrutura do Código

O script está organizado em quatro etapas principais:

load_image: Carrega o arquivo e trata possíveis erros de caminho.

convert_gray: Realiza a conversão técnica para escala de cinza.

show_image: Renderiza a imagem na tela de forma limpa.

histograma: Calcula e exibe a frequência de brilho (0-255) da imagem.
