def word_counter(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = input("Voer een zin in: ")
    word_count = word_counter(sentence)
    print("Aantal woorden:", word_count)

if __name__ == "__main__":
    main()
