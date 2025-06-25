# Scaling Laws with nanoGPT

![nanoGPT](assets/nanogpt.jpg)

This project explores **scaling laws** in transformer models—how loss, compute (FLOPs), and model size interact—using a modified version of [Andrej Karpathy’s nanoGPT](https://github.com/karpathy/nanoGPT).

It was developed as part of the **Fundamentals of Foundation Models** class at **TUM (Technical University of Munich)**, inspired by the paper [*Scaling Laws for Autoregressive Generative Modeling*](https://arxiv.org/abs/2203.15556).

📌 **Main idea:** Investigate how transformer performance scales, especially in the context of the increasing focus on **AI** and **LLMs**, where training larger models more efficiently is an ongoing challenge.

📓 The full project and results—including code and plots—are available in the notebook in this repo. The work includes training experiments and visualizations that reveal key insights from the original scaling laws literature.

---

## 🔍 What's inside

- 🧪 A Jupyter notebook that reproduces key empirical scaling behavior
- 📊 Visualizations of how loss changes with model size and FLOPs
- 🛠️ Adaptations on top of nanoGPT for controlled experimentation
- 📚 A theoretical and practical breakdown of scaling laws and their significance in modern LLM development

---

## 📁 Notebook & Code

See the notebook file inside this repository for full details on:
- Training experiments
- Graphs and data
- Conclusions about scaling behavior

This repo is a **fork of [nanoGPT](https://github.com/karpathy/nanoGPT)**, retaining its simplicity and flexibility while being adapted for academic exploration.

---

## 🧠 Why Scaling Laws Matter

As foundation models become increasingly central to AI progress, understanding how **compute**, **data**, and **model size** contribute to performance is crucial. Scaling laws help us:
- Predict how performance improves with more resources
- Optimize training strategies for cost-efficiency
- Guide the next generation of large language models

---

## 🛠️ Setup

To run or modify the experiments:

```bash
pip install torch numpy transformers datasets tiktoken matplotlib tqdm
```

You'll also need:
- Python 3.8+
- A CUDA-enabled GPU (for training)

---

## 🔗 Credits

- Base code: [Andrej Karpathy’s nanoGPT](https://github.com/karpathy/nanoGPT)
- Class: Fundamentals of Foundation Models @ TUM
- Paper inspiration: [Kaplan et al. (2022)](https://arxiv.org/abs/2203.15556)

---
