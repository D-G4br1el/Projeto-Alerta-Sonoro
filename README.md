# 🔔 Sistema de Alerta Visual Automatizado

## 📌 Visão Geral  
Este projeto implementa um **sistema de monitoramento visual automatizado**, capaz de detectar elementos específicos na tela e disparar um **alerta sonoro** sempre que um padrão pré-definido for encontrado.

A solução é flexível e pode ser utilizada em diversos cenários, como:  
- Monitoramento de painéis operacionais  
- Detecção de mudanças críticas em dashboards  
- Avisos automáticos em sistemas sem notificações nativas  
- Observação de eventos relevantes exibidos apenas visualmente  

---

## 🎯 Motivação  
Este projeto foi desenvolvido para resolver uma demanda real de operação, onde era importante:  
- Detectar rapidamente eventos prioritários exibidos somente na interface.  
- Garantir que informações importantes não passassem despercebidas.  
- Automatizar tarefas que antes exigiam um maior nível de atenção.  

A solução demonstra como **Python + automação de interface** podem oferecer resultados práticos sem necessidade de integração direta com o sistema ou interface em questão.

---

## ✅ Funcionalidades Principais  
- 🔍 **Monitoramento contínuo da tela** em busca das imagens de referência (.png).  
- 🔊 **Alerta sonoro (.wav)** automático ao detectar os padrões cadastrados.  
- 🧵 **Execução em thread (daemon)**, rodando em background.  
- ⚙️ **Configuração simples de parâmetros**, como:  
  - Tempo de monitoramento  
  - Intervalo entre ciclos  
  - Pausa após alerta  
  - Nível de confiança (`confidence`) da detecção  

- 📁 **Compatível com qualquer sistema exibido visualmente**, sem depender de APIs ou integrações.

---

## 🧩 Como Funciona 
1. O script usa `pyautogui.locateOnScreen()` para procurar imagens que representem o que deve ser detectado na tela.  
2. Ao localizar uma correspondência, um alerta sonoro é reproduzido usando `winsound.PlaySound()` (Windows).  
3. Uma **thread dedicada** realiza todo o processo de monitoramento de forma contínua.  
4. O script principal aguarda o usuário pressionar **CTRL + C** para encerrar a execução de forma controlada.  
5. O parâmetro `confidence` depende da biblioteca `opencv-python` para realizar matching com precisão.  

> **Observações:** 
1. Por se tratar de automação visual, a detecção funciona independentemente do tipo de sistema sendo monitorado.
2. Em sistemas operacionais não-Windows, a reprodução sonora pode ser adaptada para outras bibliotecas como `playsound` ou `simpleaudio`.

---

## 🛠️ Pré-requisitos  
- **Sistema Operacional recomendado:** Windows (Para o winsound.PlaySound())
- **Python:** versão 3.8 ou superior  

---

## 📦 Dependências  
Listadas no arquivo `requirements.txt`:

- `pyautogui`  
- `opencv-python`  
- `pillow`  

> Bibliotecas já incluídas no Python/Windows:  
- `time`  
- `threading`  
- `winsound`  

Instalação:

```bash
pip install -r requirements.txt
