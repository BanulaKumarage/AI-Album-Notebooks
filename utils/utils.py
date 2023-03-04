from PIL import Image, ExifTags


ORIENTATION_FLAG = [k for k, v in ExifTags.TAGS.items() if v == "Orientation"][0]


def resize(image, max_height, max_width):
    ratio = min(max_height / image.width, max_width / image.height)

    if ratio < 1:
        image = image.resize(
            (round(image.width * ratio), round(image.height * ratio))
        )
        
    return ratio, image


def rotate_image(image: Image):
    exif = image.getexif()

    if ORIENTATION_FLAG not in exif:
        return image
    elif exif[ORIENTATION_FLAG] == 3:
        image = image.rotate(180, expand=True)
    elif exif[ORIENTATION_FLAG] == 6:
        image = image.rotate(270, expand=True)
    elif exif[ORIENTATION_FLAG] == 8:
        image = image.rotate(90, expand=True)

    return image


def pad_image(image: Image, width, height, color=(0, 250, 150)):
    padded_image = Image.new(image.mode, (width, height), color)
    padded_image.paste(image, (0, 0))
    
    return padded_image


def resize_bounding_boxes(faces, ratio):
    if ratio < 1:
        return [
            (
                int(left * (1 / ratio)),
                int(top * (1 / ratio)),
                int(right * (1 / ratio)),
                int(bottom * (1 / ratio)),
            )
            for (left, top, right, bottom) in faces
        ]
    return faces