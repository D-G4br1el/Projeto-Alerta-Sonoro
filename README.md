<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Ativo-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Plataforma-Windows-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

# 🔔 Sistema de Alerta Visual Automatizado

## 📌 Visão Geral  
Este projeto implementa um **sistema automatizado de monitoramento visual**, capaz de detectar imagens específicas exibidas na tela — como ícones, textos ou alertas gráficos.  
Quando alguma das imagens cadastradas é encontrada, o sistema executa automaticamente:

- Uma **marcação visual** destacando o item identificado  
- Um **alerta sonoro** para chamar atenção imediata  

A ferramenta pode ser aplicada em diversos cenários, como:  
- Monitoramento de painéis operacionais  
- Detecção de eventos críticos em dashboards  
- Alertas automáticos em sistemas sem notificações nativas  
- Observação de informações relevantes exibidas apenas visualmente  

---

## 🎯 Motivação  
Este projeto nasceu de uma demanda real:  
Garantir que eventos visuais importantes não passem despercebidos durante o atendimento, especialmente quando o sistema monitorado não possui alertas nativos.

O objetivo foi criar uma solução simples, eficiente e totalmente independente da aplicação monitorada — usando apenas recursos visuais.

---

## ✅ Funcionalidades Principais  
- 🔍 **Monitoramento contínuo da tela** em busca das imagens cadastradas  
- 🔊 **Alerta sonoro** automático quando uma correspondência é encontrada  
- 🖼️ **Marcação visual temporária** sobre o item detectado  
- 🧵 **Thread dedicada (daemon)** para execução em background  
- ⚙️ **Parâmetros configuráveis**, como:
  - Tempo de monitoramento  
  - Intervalo entre ciclos  
  - Tempo de pausa após detecção  
  - Confiança da detecção (via OpenCV)  
- 📁 **Compatível com qualquer sistema exibido visualmente**, sem necessidade de APIs ou integrações  

---

## 🧩 Como Funciona  

1. Adicione as imagens a serem monitoradas na pasta **`assets/icones/`**  
2. Insira os caminhos dessas imagens na lista `icone_paths`  
3. O script usa `pyautogui.locateOnScreen()` para identificar visualmente a presença desses itens  
4. Caso um ícone seja encontrado:
   - Um alerta sonoro é acionado  
   - Um retângulo vermelho é exibido ao redor do item detectado  
5. Todo o monitoramento roda em uma thread separada  
6. A execução é encerrada pelo usuário via **CTRL + C**  
7. O parâmetro `confidence` depende do pacote `opencv-python`  

> **Observações importantes:**  
> • Por se tratar de automação visual, a detecção funciona independentemente do tipo de sistema sendo monitorado.  
> • Pode ser adaptado para qualquer resolução ou ambiente.  
> • A marcação é um overlay simples.  
> • Em sistemas operacionais não-Windows, a reprodução sonora pode ser adaptada para outras bibliotecas como `playsound` ou `simpleaudio`.  
> • Para usar o parâmetro `confidence`, o pacote `opencv-python` é necessário.  


---

## 🛠️ Pré-requisitos  
- **Windows** (recomendado pela biblioteca `winsound`)  
- **Python 3.8+**

---

## 📦 Dependências  
Instale tudo com:

```bash
pip install -r requirements.txt
