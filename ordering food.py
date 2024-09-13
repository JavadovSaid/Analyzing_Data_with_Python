import pyautogui
import time

# Wait for 40 seconds before starting
time.sleep(30)

# Define stop counter
stop_count = 0

# List of messages for your mom
messages = [
    "Ana, mən artıq böyümüşəm, bunu hiss edirsənmi?",
    "Mənə hər zaman dəstək olduğun üçün təşəkkür edirəm, ana!",
    "İndi qərarlarımı özüm verirəm, amma sənin məsləhətlərin mənimlədir.",
    "Artıq daha çox məsuliyyət daşıyıram, və bu hiss mənə çox şey öyrədir.",
    "Həyatın çətinliklərini öz gözlərimlə görürəm, ana, və sənin dediklərini daha yaxşı başa düşürəm.",
    "Mən artıq uşaq deyiləm, amma hələ də sənin qayğına ehtiyacım var.",
    "Düşünürəm ki, səninlə daha çox vaxt keçirməliyik, ana.",
    "Hər zaman mənə güvəndiyin üçün minnətdaram.",
    "İndi öz ayaqlarım üstündə durmağa çalışıram, amma hər zaman sənin dəstəyinə arxalanıram.",
    "Ana, mənim böyüdüyümü qəbul etmək çətin ola bilər, amma bu, həyatın təbii bir hissəsidir."
]

# Function to type and press 'enter'
def main(message):
    pyautogui.write(message)  # Type the message
    pyautogui.press('enter')  # Press 'enter' key

# Loop to execute the function 30 times
while stop_count < 50\
        :
    # Select a message based on the current stop_count (cycling through the list)
    message_to_send = messages[stop_count % len(messages)]
    main(message_to_send)  # Call the function with the selected message
    time.sleep(1)  # Wait for 2 seconds
    stop_count += 1  # Increment the counter
