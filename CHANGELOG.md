# 📝 Changelog

Todas as mudanças importantes deste projeto serão documentadas aqui!

---

## [v1.1.0] - 2025-11-30
### 🔧 Melhorias de Otimização
- Redução de `sleep` desnecessários para tornar o monitoramento mais eficiente.
- Pequeno ajuste do ciclo de monitoramento para manter performance estável.
- Limpeza de trechos redundantes.

### 🎯 Detecção e Marcação
- A precisão da detecção foi levemente ajustada para reduzir falsos positivos.
- A marcação do ícone agora é mais clara, com tamanho proporcional ao elemento encontrado.

---

## [v1.0.0] - 2025-11-15
### 🚀 Primeira Versão Funcional
- Detecção de ícone utilizando OpenCV (template matching).
- Alerta sonoro sempre que o elemento é encontrado.
- Loop contínuo de monitoramento em background.
- Captura de tela com PyAutoGUI.
- Uso de Threads para evitar travamento da interface.
