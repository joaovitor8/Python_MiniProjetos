import pyautogui
import time

# --- CONFIGURAÇÃO ---
# Remove a pausa de segurança para clicar na velocidade máxima
pyautogui.PAUSE = 0.1


print("--- AUTO-CLICKER TEMPORIZADO ---")
print("Posicione o mouse onde você quer clicar AGORA!")

# Contagem regressiva de 5 segundos
for i in range(5, 0, -1):
  print(f"Começando em {i}...")
  time.sleep(1)

print("!!! CLICANDO (Duração: 30 segundos) !!!")

# Marca o horário de agora e calcula quando deve parar (daqui a 30s)
tempo_parada = time.time() + 40

# Loop que continua rodando enquanto o tempo atual for menor que o tempo de parada
while time.time() < tempo_parada:
  pyautogui.click()

print("--- TEMPO ESGOTADO. FIM. ---")
