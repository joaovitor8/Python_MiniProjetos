import pyautogui
import time

# --- CONFIGURAÇÃO ---
# Remove a pausa de segurança para clicar na velocidade máxima
pyautogui.PAUSE = 0.1

tempo = int(input("Digite o tempo em segundos para o auto-clicker: "))


print("--- AUTO-CLICKER TEMPORIZADO ---")
print("Posicione o mouse onde você quer clicar AGORA!")

# Contagem regressiva de 5 segundos
for i in range(5, 0, -1):
  print(f"Começando em {i}...")
  time.sleep(1)

print("!!! CLICANDO !!!")

# Marca o horário de agora e calcula quando deve parar
tempo_parada = time.time() + tempo

# Loop que continua rodando enquanto o tempo atual for menor que o tempo de parada
while time.time() < tempo_parada:
  pyautogui.click()

print("--- TEMPO ESGOTADO. FIM. ---")
