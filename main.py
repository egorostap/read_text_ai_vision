import easyocr

def file_write_dec(fn):
    def wrapped(file_name="result.txt", *args, **kwargs):
        result = fn(*args, **kwargs)
        with open(file_name, "w", encoding='utf-8') as f:
            for line in result:
                f.write(f"{line}\n")
    return wrapped


@file_write_dec
def text_recognition(file_path=''):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    print(result)
    return result


if __name__ == '__main__':
    text_recognition(file_path='1.jpg')