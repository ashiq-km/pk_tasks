<!-- ============================= -->
<!--        TASK 3 DOCUMENT       -->
<!-- ============================= -->

<h1 style="color:#4CAF50; text-align:center;">
👽 Task 3: AI Logic & Explanation
</h1>

<hr/>

<h2 style="color:#2196F3;">🎌 Objective</h2>

This document explains the **reasoning, logic, and design decisions**
behind the deep learning model built in **Task 2**.
The goal is to demonstrate **conceptual clarity in AI/ML fundamentals**
beyond just implementation.

---

<h2 style="color:#FF9800;">🤔 Why This Model Was Chosen</h2>

A **Convolutional Neural Network (CNN)** was selected for this task because:

<ul>
  <li>📷 The problem involves <b>image classification</b>, where spatial patterns are crucial.</li>
  <li>🧩 CNNs exploit <b>local spatial correlations</b> using convolutional filters.</li>
  <li>🔁 Weight sharing makes CNNs <b>computationally efficient</b> compared to fully connected networks.</li>
  <li>📈 CNNs naturally learn <b>hierarchical representations</b>, from low-level features to high-level semantics.</li>
</ul>

The CIFAR-10 dataset consists of small (32×32) RGB images, making it
an ideal candidate for a **custom CNN architecture** without transfer learning.

---

<h2 style="color:#9C27B0;">🧬 How Features Impact Prediction</h2>

CNNs learn features in a **hierarchical manner**, where each layer
captures increasingly abstract representations:

<table>
  <tr>
    <th>Layer Depth</th>
    <th>Learned Features</th>
  </tr>
  <tr>
    <td>Early Convolution Layers</td>
    <td>Edges, color gradients, simple patterns</td>
  </tr>
  <tr>
    <td>Middle Convolution Layers</td>
    <td>Textures, shapes, object parts</td>
  </tr>
  <tr>
    <td>Deeper Layers</td>
    <td>High-level semantic representations of objects</td>
  </tr>
</table>

### 🔹 Role of Key Components

- **Convolution Layers**  
  Extract spatial features using learnable filters.

- **Batch Normalization**  
  Stabilizes feature distributions, accelerates training, and improves generalization.

- **ReLU Activation**  
  Introduces non-linearity and suppresses weak or irrelevant activations.

- **Max Pooling**  
  Reduces spatial dimensions while retaining the most salient features.

- **Global Average Pooling**  
  Reduces model parameters and helps prevent overfitting by summarizing feature maps.

Together, these components allow the network to convert raw pixel values
into meaningful class predictions.

---

<h2 style="color:#E91E63;">🚀 Possible Improvements & Future Work</h2>

While the current model achieves good generalization, several improvements
can further enhance performance:

<ul>
  <li>⏱️ <b>Longer training</b> with learning-rate scheduling</li>
  <li>🔄 <b>Stronger data augmentation</b> strategies</li>
  <li>🧪 <b>Test-Time Augmentation (TTA)</b> for more robust predictions</li>
  <li>🏗️ Deeper architectures such as <b>ResNet</b></li>
  <li>🌍 <b>Transfer learning</b> using pretrained models</li>
  <li>🎯 Fine-tuning hyperparameters (batch size, learning rate)</li>
</ul>

These improvements are commonly used in **production-grade computer vision systems**.

---

<h2 style="color:#607D8B;">✅ Conclusion</h2>

The chosen CNN architecture effectively learns hierarchical features
from image data and generalizes well to unseen samples.

Key takeaways:
<ul>
  <li>✔ Model choice aligns with the nature of the data</li>
  <li>✔ Feature learning follows a logical hierarchy</li>
  <li>✔ Data augmentation significantly improves generalization</li>
  <li>✔ The model demonstrates solid deep learning fundamentals</li>
</ul>


<hr/>

<p style="text-align:center; font-style:italic;">
Prepared as part of the AI Engineer Technical Assignment
</p>
