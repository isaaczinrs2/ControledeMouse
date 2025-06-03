
# 🖐️ Controle do Mouse com Gestos usando OpenCV e MediaPipe

Este projeto foi desenvolvido durante o **Intensivão de Python da Ctrl+Play (2024)**. O objetivo é controlar o cursor do mouse e realizar cliques apenas com movimentos da mão capturados pela webcam, utilizando **MediaPipe**, **OpenCV**, e **PyAutoGUI**.

## ✨ Funcionalidades

- 📸 Captura da mão em tempo real usando a webcam.
- 🖱️ Controle do cursor do mouse com a ponta do dedo indicador.
- 👆 Clique automático quando o dedo polegar se aproxima do indicador.
- 🎯 Detecção precisa com apenas uma mão.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

## 🚀 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
````

2. **Instale as dependências:**

```bash
pip install opencv-python mediapipe pyautogui
```

3. **Execute o programa:**

```bash
python main.py
```

> Certifique-se de que sua webcam esteja funcionando corretamente.

## 📄 Explicação do funcionamento

* O programa utiliza o **MediaPipe Hands** para detectar pontos de referência na mão.
* Ele acompanha principalmente os pontos:

  * `8` → ponta do dedo **indicador**.
  * `4` → ponta do **polegar**.
* A posição do dedo indicador controla o cursor do mouse na tela.
* Quando o polegar se aproxima do indicador (distância < 0.05), um **clique do mouse** é executado.

## 🔧 Ajustes que podem ser feitos

* Ajustar o mapeamento das coordenadas para melhor precisão.
* Adicionar funcionalidades como scroll, duplo clique, ou gestos personalizados.
* Melhorar a detecção com duas mãos.


