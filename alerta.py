import pyautogui
import time
import threading
import winsound

executando = True

def monitorar_icones_na_tela(icones_paths, tempo_monitoramento=1000, tempo_pausa=5):
    """
    Monitora a tela por um tempo determinado em busca de chamados prioridade e emite um som quando qualquer um é encontrado.

    Args:
        icones_paths (list): Lista de caminhos das imagens dos ícones.
        tempo_monitoramento (int): Tempo de monitoramento antes da pausa (em segundos).
        tempo_pausa (int): Tempo de espera antes de retomar o monitoramento (em segundos).
    """
    global executando
    print(f"Iniciando monitoramento...")

    while executando:
        start_time = time.time()
        while time.time() - start_time < tempo_monitoramento:
            for icone_path in icones_paths:
                try:
                    localizacao = pyautogui.locateOnScreen(icone_path, confidence=0.8)
                    if localizacao:
                        print(f"Ícone localizado! ")
                        winsound.PlaySound(r"assets\audio\notificacao_vip.wav", winsound.SND_FILENAME)
                        time.sleep(40)  # Pausa após encontrar um ícone(em segundos)
                except Exception:
                    print(f"Nada no momento")

            time.sleep(4)  # Tempo de aguardo entre verificações(em segundos)

        print(f"Pausa de {tempo_pausa} segundos antes de reiniciar o monitoramento...\n")
        time.sleep(tempo_pausa)


def iniciar_monitoramento():
    icones_paths = [
        r"assets\icones\teste_icon.png",
        r"assets\icones\icon_test_2.png"
              
    ]

    # Verifica se os arquivos dos ícones existem
    for icone_path in icones_paths:
        try:
            with open(icone_path, 'r') as f:
                pass
        except FileNotFoundError:
            print(f"Erro: O arquivo do ícone '{icone_path}' não foi encontrado.")

    # Inicia a thread de monitoramento
    monitoramento_thread = threading.Thread(
        target=monitorar_icones_na_tela,
        args=(icones_paths, 300, 5),  # 300 segundos (5 minutos) de monitoramento, 5 segundos de pausa
        daemon=True
    )
    monitoramento_thread.start()

    print("Monitoramento iniciado. Pressione Ctrl + C no Terminal para interromper.")
    try:
        while True:
            time.sleep(5)  # Mantém o script ativo


    except KeyboardInterrupt:
        print("Monitoramento encerrado manualmente.")
        global executando
        executando = False


if __name__ == "__main__":
    iniciar_monitoramento()


        
        
        