from translate import Translator


def main():
    # Not the best translator
    translator = Translator('es')
    try:
        with open('test.txt', mode='r') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            with open('test-es.txt', mode='w') as my_translated_file:
                my_translated_file.write(translation)
    except (FileNotFoundError, IOError) as err:
        print(err)


if __name__ == '__main__':
    main()
