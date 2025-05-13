# 🎯 Aim Analyzer – Analisador de Mira para Valorant com YOLOv8

> 📄 Este README também está disponível em inglês:  
> 🇺🇸 [Read in English](README.md)

Este projeto é um **analisador de alinhamento de mira em tempo real** para o jogo de FPS **Valorant**. Ele utiliza um modelo de detecção de objetos **YOLOv8** treinado com dados personalizados para detectar **cabeças de inimigos** em gravações de gameplay e avaliar se a **mira está alinhada**, **acima** ou **abaixo** da cabeça do alvo.

---

## 🤖 Detecção de Objetos com YOLOv8

**YOLO (You Only Look Once)** é uma arquitetura de detecção de objetos em tempo real.  
Ela prevê caixas delimitadoras (bounding boxes) e as classes dos objetos **diretamente das imagens em uma única passada**, sendo extremamente rápida e ideal para tarefas relacionadas a jogos.

O modelo foi treinado com frames anotados de partidas de Valorant, usando o Roboflow, onde foram marcadas as áreas da **cabeça dos inimigos**.

---

## 🧠 Pipeline de Inferência

- Cada frame do vídeo é passado para o modelo YOLOv8
- O modelo retorna as coordenadas das cabeças detectadas
- Calculamos o centro vertical da cabeça detectada
- Comparamos com a posição da **mira (crosshair)**, que é assumida como o centro vertical da tela
- Com base nessa comparação, o frame é classificado como:
  - `"aligned"`: mira está próxima o suficiente (dentro de uma margem em pixels)
  - `"above"`: mira está abaixo da cabeça
  - `"below"`: mira está acima da cabeça

---

## ⚙️ Ferramentas e Bibliotecas Utilizadas

- [Ultralytics](https://github.com/ultralytics/ultralytics): para treinar e executar modelos YOLOv8
- [OpenCV](https://opencv.org/): para leitura e manipulação de vídeo em tempo real
- **Python**: linguagem principal para processar, integrar e exibir os resultados

---

## 🚀 Como Usar

1. **Instale as dependências** (em um ambiente virtual):

```bash
pip install ultralytics opencv-python
````

2. **Grave ou baixe** um vídeo de gameplay do Valorant como `valorant.mp4`

3. **Execute o script principal**:

```bash
python src/analyze_aim.py
```

---

## 🎥 Algumas imagens do treinamento

![val\_batch0\_pred](https://github.com/user-attachments/assets/69ecf833-8e88-4447-9a85-b09c5d53f172)

---

## 🎥 Exemplo de saída em vídeo

[https://github.com/user-attachments/assets/56acffe3-87e1-4389-a1e7-df7a0293aeb3](https://github.com/user-attachments/assets/56acffe3-87e1-4389-a1e7-df7a0293aeb3)

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.
