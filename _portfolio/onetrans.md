---
title: "OneTrans"
collection: portfolio
kind: research
order: 5
permalink: /portfolio/onetrans/
excerpt: "Ported a TensorFlow reference implementation into a modular training project, preserving heterogeneous feature tokenization and pyramid-style compression. Added schema-aware data loading, mixed precision, evaluation, and resumable checkpoints."
author_profile: true
share: false
comments: false
---

**PyTorch reimplementation · Mar–Apr 2026**

Ported a TensorFlow reference implementation into a modular training project, preserving heterogeneous feature tokenization and pyramid-style compression. Added schema-aware data loading, mixed precision, evaluation, and resumable checkpoints.

## Technical work

- Preserved heterogeneous sequential/non-sequential feature tokenization, token-specific parameter sharing, and pyramid-style representation compression.
- Extended the reference demonstration into modular data loading, schema-aware tensorization, model wrappers, training and validation loops, accuracy/AUC evaluation, and configurable CLI experiments.
- Added scaled dot-product attention, CUDA mixed precision, optional activation checkpointing, and resumable training state.

This is a reading-and-reimplementation project based on an existing TensorFlow reference, with a training pipeline built around the port.


**Technologies / topics:** Recommender systems / Transformers / PyTorch

[Implementation](https://github.com/WestbrookLong/OneTrans_Pytorch)
