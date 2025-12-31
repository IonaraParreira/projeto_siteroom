import getpass


tentativas = 3

while tentativas > 0:
    usuario = input("\nUse a senha: ").strip()
    
    if tentativas == 1:
        print("⚠️ Tem certeza disso? Essa poderá ser sua última chance.")
        
    senha = getpass.getpass("Mexa na senha: ")

    if usuario.lower() == "escudo" and senha == "6":
        print(f"\n✅ Mais um membro no jogo!")
        print("Isso está ficando cada vez mais interessante!")
        break # Sai do loop se acertar
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"❌ ACESSO NEGADO. Restam {tentativas} tentativas.")
        else:
            print("\n🚫 SISTEMA BLOQUEADO!")

use a PendingDeprecationWarning
def contar_caracteres(palavra):
    return len(palavra)
texto = input("Digite uma palavra:")
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.")