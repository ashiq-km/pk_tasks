# 🧞Model Explanation🧞

## Overview

This project uses a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10 dataset** for multi-class image classification. The model is designed to be simple, interpretable, and suitable for deployment as a REST API using FastAPI.

CIFAR-10 contains **60,000 color images (32×32 pixels)** across **10 object classes**, making it a standard benchmark for evaluating image classification models.

---

## Model Architecture

The deployed model (`best_model.keras`) follows a straightforward CNN architecture:

1. **Input Layer**

   * Image shape: `32 × 32 × 3` (RGB)

2. **Convolution Block 1**

   * `Conv2D(32, 3×3, ReLU)`
   * `MaxPooling2D(2×2)`
   * Purpose: Capture low-level features such as edges and textures

3. **Convolution Block 2**

   * `Conv2D(64, 3×3, ReLU)`
   * `MaxPooling2D(2×2)`
   * Purpose: Capture higher-level patterns and shapes

4. **Classification Head**

   * `Flatten`
   * `Dense(128, ReLU)`
   * `Dense(10, Softmax)`
   * Purpose: Convert extracted features into class probabilities

---

## Output & Class Labels

The model outputs a **probability distribution** across the following classes:

```
['Aeroplane', 'Automobile', 'Bird', 'Cat', 'Deer',
 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
```

The predicted class is selected using:

* `argmax` over the softmax probabilities
* Confidence score = maximum probability

---

## Prediction Confidence & Misclassifications

The **softmax confidence score** provides insight into prediction reliability:

* **High confidence (> 0.80)**

  * Model is usually correct
  * Input image closely resembles training distribution

* **Medium confidence (0.50 – 0.80)**

  * Possible ambiguity between visually similar classes
  * Example: Cat vs Dog, Deer vs Horse

* **Low confidence (< 0.50)**

  * Higher likelihood of incorrect prediction
  * Often caused by:

    * Blurry or low-resolution images
    * Unusual angles or backgrounds
    * Objects partially visible

This behavior was observed during manual testing via the FastAPI `/predict` endpoint.

---

## Known Limitations

* Trained on **small (32×32)** images — fine details are lost
* Sensitive to:

  * Image orientation
  * Background clutter
  * Poor lighting conditions
* No data augmentation used during inference

These limitations are expected for a lightweight CNN and align with the assignment scope.

---

## Why This Model Was Chosen

* Simple and explainable architecture
* Fast inference suitable for API deployment
* Demonstrates end-to-end ML workflow:

  * Training
  * Evaluation
  * Serialization
  * Deployment

---

## Future Improvements

* Data augmentation during training
* Deeper CNN or transfer learning (ResNet, MobileNet)
* Confidence-based rejection ("unknown" class)
* Batch prediction support in API

---

## Conclusion

This CNN model effectively demonstrates **core deep learning concepts**, **model explainability**, and **production readiness**. The inclusion of confidence-based interpretation helps explain both correct and incorrect predictions, making the system more transparent and practical for real-world usage.
