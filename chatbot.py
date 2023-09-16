import speech_recognition as sr
import sympy

r = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Please speak your calculation:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError as e:
            print(f"Error fetching result: {e}")
            return None
        except sr.RequestError as e:
            print("Could not understand audio")
            return None

def calculate(expression):
    try:
        result = sympy.sympify(expression)
        return result
    except Exception as e:
        return str(e)

def main():
    while True:
        text = speech_to_text()
        if text is None:
            continue
        if text.lower() == "exit":
            break
        else:
            print("You said:", text)
            result = calculate(text)
            print("Result:", result)

if __name__ == "__main__":
    main()
