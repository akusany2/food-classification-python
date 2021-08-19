import numpy as np

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

    return format(category[index][1])
