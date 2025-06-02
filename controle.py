import cv2
import mediapipe as mp
import pyautogui
import math

mp_hands = mp.solutions.hands
mp_drawning = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

def calculate_distance(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

# Loop para processar os frames da tela
while True:
    ret, frame = cap.read()
    if not ret:    
        break

    # Convertando a imagem para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processando a imagem para detectação de mão
    result = hands.process(frame_rgb)

    # Obtendo a dimensão da captura (frame)
    frame_height, frame_width, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extrair as coordenadas do ponto 8 (dedo indicador) e 
            index_flinger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            # Calculando a distância entre o mata-piolho e o fura-bolo
            distance = calculate_distance(index_flinger_tip, thumb_tip)

            # Mover cursor do mouse
            x = int(index_flinger_tip.x * frame_width)
            y = int(thumb_tip.y * frame_height)

            screen_x = screen_width - (screen_width / frame_width * x)
            screen_y =  screen_height / frame_width * y 

            pyautogui.moveTo(screen_x, screen_y)

            if distance < 0.05:
                pyautogui.click()

            mp_drawning.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Pegou a mão", frame)
    
cap.release()
cv2.destroyAllWindows()
