import os
import math
import numpy as np
import tensorflow as tf


def load_and_pred(model, filename, class_names, img_shape=224):
    img = tf.io.read_file(filename)

    img = tf.image.decode_image(img, channels=3)

    img = tf.image.resize(img, size=[img_shape, img_shape])

    img = img/255.
    
    img = tf.expand_dims(img, axis=0)
    pred = model.predict(img)
    prob = f'{math.ceil(pred.max()*100)}%'
    pred_class = class_names[int(np.argmax(pred))]
    
    return pred_class, prob
