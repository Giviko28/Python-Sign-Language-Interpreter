#!/usr/bin/env python3
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Loading data
def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    return (x_train, y_train), (x_test, y_test)

# Exploring data
def explore_data(x_train, y_train):
    # Find data structure
    print("Training data shape: ", x_train.shape)
    print("Training labels shape: ", y_train.shape)
    
    # Categories
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    num_classes = len(class_names)
    print("Number of classes: ", num_classes)
    print("Class names: ", class_names)
    
    # Display some sample images from each class
    num_samples = 10
    plt.figure(figsize=(15, 15))
    
    for i in range(num_samples):
        random_idx = np.random.randint(0, x_train.shape[0])
        plt.subplot(1, num_samples, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x_train[random_idx])
        plt.xlabel(class_names[y_train[random_idx][0]])
        
    plt.show(block=False)


# Preprocess data
def preprocess_data(x_train, x_test, y_train, y_test):
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return x_train, x_test, y_train, y_test

# Define the baseline model
def create_baseline_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Define the improved model
def create_improved_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D((2, 2)),
        Dropout(0.2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Dropout(0.3),
        Conv2D(128, (3, 3), activation='relu'),
        Flatten(),
        Dropout(0.4),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Cross-validation function
def cross_validate_model(x, y, model_fn, n_folds=5):
    x_folds = [x[k::n_folds] for k in range(n_folds)]
    y_folds = [y[k::n_folds] for k in range(n_folds)]

    avg_fold_accuracy = []
    for idx in range(n_folds):
        x_val, y_val = x_folds[idx], y_folds[idx]
        x_train = np.concatenate(x_folds[:idx] + x_folds[idx+1:])
        y_train = np.concatenate(y_folds[:idx] + y_folds[idx+1:])

        model = model_fn()

        history = model.fit(x_train, y_train, epochs=20,
                            batch_size=16, validation_data=(x_val, y_val))

        history = history.history
        avg_fold_accuracy.append(history['val_accuracy'][-1])

        for metric, values in history.items():
            plt.plot(values, label=metric)
        plt.title(f"Learning curves for fold {idx + 1}")
        plt.legend()
        plt.show()

    print(f"Average out-of-sample test accuracy for {model_fn.__name__}:", np.mean(avg_fold_accuracy))

# Main function
if __name__ == '__main__':
    # Load and preprocess data
    (x_train, y_train), (x_test, y_test) = load_data()
    x_train, x_test, y_train, y_test = preprocess_data(x_train, x_test, y_train, y_test)
    
    # Combine training and test data for cross-validation
    x = np.concatenate([x_train, x_test])
    y = np.concatenate([y_train, y_test])

    # Perform cross-validation for baseline model
    cross_validate_model(x, y, create_baseline_model)
    
    # Perform cross-validation for improved model
    cross_validate_model(x, y, create_improved_model)




