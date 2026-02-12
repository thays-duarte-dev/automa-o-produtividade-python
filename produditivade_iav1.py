from openai import OpenAI
import matplotlib.pyplot as plt

# 1. MINHA CHAVE DO CHATGPT (Já está aqui, Thays!)
minha_chave = ""

client = OpenAI(api_key=minha_chave)

print("--- THAYS, ESTOU A FALAR COM O MEU CHATGPT... ---")

try:
    # Eu a falar com a IA do meu jeito
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Chat, sou a Thays! Reduzi meu trabalho de 55h para 10h com Python. Comemora comigo e avisa que o MEU GRÁFICO está pronto!"}
        ]
    )
    
    print("\n[O CHATGPT ME DISSE]:")
    print(response.choices[0].message.content)
    print("-" * 30)

except Exception as e:
    # Se der erro de cota, a gente ignora e abre o gráfico!
    print(f"\nO ChatGPT teve um problema (será a falta de créditos?), mas o MEU GRÁFICO abre igual!")

# 3. O MEU GRÁFICO (Minha Automação de Sucesso)
tarefas = ['Triagem', 'Análise', 'Relatórios', 'Suporte']
antes = [12, 18, 10, 15] 
depois = [2, 4, 1, 3] 

print("\nThays, a abrir o MEU GRÁFICO de sucesso agora...")

plt.figure(figsize=(10, 6))
plt.bar(tarefas, antes, label='Antes (55h)', color='gray', alpha=0.5)
plt.bar(tarefas, depois, label='Depois com MEU Python (10h)', color='green')

plt.title('Minha Automação: Thays + IA')
plt.ylabel('Horas que eu gastava')
plt.legend()

# Comando para abrir a janela do gráfico
plt.show()