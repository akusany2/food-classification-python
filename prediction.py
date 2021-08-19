import os

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image


category = {
    0: ["burger", "Burger"],
    1: ["butter_naan", "Butter Naan"],
    2: ["chai", "Chai"],
    3: ["chapati", "Chapati"],
    4: ["chole_bhature", "Chole Bhature"],
    5: ["dal_makhani", "Dal Makhani"],
    6: ["dhokla", "Dhokla"],
    7: ["fried_rice", "Fried Rice"],
    8: ["idli", "Idli"],
    9: ["jalegi", "Jalebi"],
    10: ["kathi_rolls", "Kaathi Rolls"],
    11: ["kadai_paneer", "Kadai Paneer"],
    12: ["kulfi", "Kulfi"],
    13: ["masala_dosa", "Masala Dosa"],
    14: ["momos", "Momos"],
    15: ["paani_puri", "Paani Puri"],
    16: ["pakode", "Pakode"],
    17: ["pav_bhaji", "Pav Bhaji"],
    18: ["pizza", "Pizza"],
    19: ["samosa", "Samosa"],
}


def predict_image(filename, model):
    img_ = image.load_img(filename, target_size=(299, 299))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.0

    prediction = model.predict(img_processed)

    index = np.argmax(prediction)

    # plt.title("Prediction - {}".format(category[index][1]))
    # plt.imshow(img_array)
    return format(category[index][1])


def predict_dir(filedir, model):
    cols = 5
    pos = 0
    images = []
    total_images = len(os.listdir(filedir))
    rows = total_images // cols + 1

    true = filedir.split("/")[-1]

    fig = plt.figure(1, figsize=(25, 25))

    for i in sorted(os.listdir(filedir)):
        images.append(os.path.join(filedir, i))

    for subplot, imggg in enumerate(images):
        img_ = image.load_img(imggg, target_size=(299, 299))
        img_array = image.img_to_array(img_)

        img_processed = np.expand_dims(img_array, axis=0)

        img_processed /= 255.0
        prediction = model.predict(img_processed)
        index = np.argmax(prediction)

        pred = category.get(index)[0]
        if pred == true:
            pos += 1

        fig = plt.subplot(rows, cols, subplot + 1)
        fig.set_title(category.get(index)[1], pad=10, size=18)
        plt.imshow(img_array)

    acc = pos / total_images
    print(
        "Accuracy of Test : {:.2f} ({pos}/{total})".format(
            acc, pos=pos, total=total_images
        )
    )
    plt.tight_layout()
