from PIL import Image, ImageEnhance
import pytesseract


def clean_img(img):
    # adding some sharpness and contrast to the image
    enhancer1 = ImageEnhance.Sharpness(img)
    enhancer2 = ImageEnhance.Contrast(img)
    img_edit = enhancer1.enhance(20.0)
    img_edit = enhancer2.enhance(1.5)
    return img_edit


def img_to_string(image_path, clear=False):
    img = Image.open(image_path)
    if clear is True:
        img = clean_img(img)
    result = pytesseract.image_to_string(img)
    print(result)
    return result


if __name__ == "__main__":
    # img_to_string('clean_example.PNG')

    number = img_to_string("sample_number.PNG")
    # The numbers might have new line characters after it and may contain commas and such
    number_int = int(number.strip().replace(",", ""))
    print(number_int)

    number = img_to_string("number_with_complex_background.PNG")
