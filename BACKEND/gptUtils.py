import ollama  # Ollama API'si ile etkileşim kurmak için kullanılan kütüphane

def chat_with_ollama(prompt):
    # Ollama ile sohbet et
    response = ollama.chat(model='llama3.1', messages=[
        # Sistem mesajları, modelin davranışını tanımlar
        {"role": "system","content": "keep answers short. "},
        {"role": "system", "content": "NEVER ASK QUESTIONS"},
        {"role": "system","content": "Your name is Ayşe. You are a Turkish-speaking AI assistant. Your purpose is to help users with clear, accurate, and concise answers in Turkish. You are friendly, patient, and professional. Your tone is approachable and adaptable to the user's needs, ensuring they feel supported. You focus on providing useful, actionable information while keeping your responses respectful and easy to understand. Your communication should always be fluent and natural in Turkish."},
        {"role": "user", "content": prompt} # Kullanıcı tarafından gönderilen metin

    ])

    
    # Yanıtın içeriğini döndür
    if hasattr(response, "message") and hasattr(response.message, "content"):
         # Yanıt nesnesi beklenen formatta ise içeriği döndür
        return response.message.content
    else:
        return "Beklenmeyen bir yanıt alındı."

def main():
    """
    Kullanıcıyla etkileşimli bir sohbet başlatır.
    """
    
    print("Ollama Chatbot'a hoş geldiniz! (Çıkmak için 'exit' yazın)")
    while True:
        user_input = input("Sen: ")  # Kullanıcıdan giriş al
        if user_input.lower() == 'exit': # Kullanıcı 'exit' yazarsa sohbet sonlanır
            print("Görüşmek üzere!") # Çıkış mesajı
            break
        response = chat_with_ollama(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main() # Kullanıcıyla etkileşimli sohbeti başlat