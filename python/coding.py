import random

def acak_kata(kata):
    return ''.join(random.sample(kata, len(kata)))

def main():
    daftar_kata = ["python", "komputer", "data", "jaringan", "algoritma"]
    kata_asli = random.choice(daftar_kata)
    kata_acak = acak_kata(kata_asli)

    print("Tebak kata yang sudah diacak ini:")
    print(f"👉 {kata_acak}")

    tebakan = input("Jawaban kamu: ").lower()

    if tebakan == kata_asli:
        print("✅ Benar! Kamu hebat!")
    else:
        print(f"❌ Salah. Jawabannya adalah: {kata_asli}")

if __name__ == "__main__":
    main()
