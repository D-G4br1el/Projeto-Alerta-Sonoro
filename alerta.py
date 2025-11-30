import pyautogui
import time
import threading
import winsound
import win32gui
import win32con
import win32api

executando = True


# ============================
# MARCAÇÃO DOS ÍCONES
# ============================
def marcar_icone(x, y, w, h, duracao=15.0):
    """Desenha um retângulo vermelho na área detectada."""

    def desenhar_retangulo():
        hwnd = win32gui.GetDesktopWindow()
        hdc = win32gui.GetWindowDC(hwnd)

        pen = win32gui.CreatePen(win32con.PS_SOLID, 4, win32api.RGB(255, 0, 0))
        brush = win32gui.GetStockObject(win32con.NULL_BRUSH)

        old_pen = win32gui.SelectObject(hdc, pen)
        old_brush = win32gui.SelectObject(hdc, brush)

        # Desenha o retângulo
        win32gui.Rectangle(hdc, x, y, x + w, y + h)

        # Espera o tempo definido
        time.sleep(duracao)

        # Retira a marcação após o tempo
        win32gui.InvalidateRect(hwnd, (x, y, x + w, y + h), True)

        win32gui.SelectObject(hdc, old_pen)
        win32gui.SelectObject(hdc, old_brush)
        win32gui.ReleaseDC(hwnd, hdc)

    # Cria thread separada para não travar o monitoramento
    threading.Thread(target=desenhar_retangulo, daemon=True).start()


# ============================
# MONITORAMENTO DOS ÍCONES
# ============================
def monitorar_icones_na_tela(icones_paths, tempo_monitoramento=300, tempo_pausa=5):
    """
    Monitora a tela por em busca dos ícones. 
    """
    global executando
    print("Iniciando monitoramento...\n")

    heartbeat = 0  # reduzir o spam de mensagens no terminal

    while executando:
        start_time = time.time()
        alerta_emitido = False  # controla o alerta por ciclo

        while time.time() - start_time < tempo_monitoramento:
            encontrou_algo = False

            for icone_path in icones_paths:
                try:
                    localizacao = pyautogui.locateOnScreen(icone_path, confidence=0.8)

                    if localizacao:
                        encontrou_algo = True
                        

                        # Marca o ícone detectado
                        x, y, w, h = (
                            localizacao.left,
                            localizacao.top,
                            localizacao.width,
                            localizacao.height,
                        )
                        marcar_icone(x, y, w, h, duracao=20.0)

                        # Toca alerta apenas uma vez por ciclo
                        if not alerta_emitido:
                            winsound.PlaySound(
                                r"assets/audio/notificacao_vip.wav",
                                winsound.SND_FILENAME,
                            )
                            alerta_emitido = True

                except Exception:
                    pass

            # heartbeat a cada 5 ciclos
            heartbeat += 1
            if heartbeat >= 5:
                print("Monitorando...")
                heartbeat = 0

            time.sleep(4)

        print(f"Pausa de {tempo_pausa}s antes de reiniciar o monitoramento...\n")
        time.sleep(tempo_pausa)


# ============================
# PRINCIPAL
# ============================
def iniciar_monitoramento():
    icones_paths = [
        r"assets/icones/teste_icon.png",
        r"assets/icones/icon_test_2.png",
    ]

    # Valida se o ícone existe ou está com o caminho correto
    for icone in icones_paths:
        try:
            open(icone, "rb").close()
        except FileNotFoundError:
            print(f"⚠ Arquivo não encontrado: {icone}")

    # Thread de monitoramento
    monitoramento_thread = threading.Thread(
        target=monitorar_icones_na_tela,
        args=(icones_paths, 300, 5),
        daemon=True,
    )
    monitoramento_thread.start()

    print("Monitoramento iniciado. Pressione Ctrl + C no terminal para encerrar.\n")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoramento encerrado manualmente.")
        global executando
        executando = False


if __name__ == "__main__":
    iniciar_monitoramento()
