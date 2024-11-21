from src.model import TextGenerator
from src.utils import print_welcome_message, print_generated_text

def main():
    generator = TextGenerator()
    print_welcome_message()

    while True:
        user_input = input("\nYour question: ")

        if user_input.lower() == 'stop':
            print("Exiting... Goodbye!")
            break

        try:
            generated_text = generator.generate(user_input)
            print_generated_text(generated_text)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()