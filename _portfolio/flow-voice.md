---
title: "Flow Voice"
collection: portfolio
kind: project
period: "Apr 2026 — Present"
order: 3
permalink: /portfolio/flow-voice/
excerpt: "An open-source system that streams smartphone speech recognition directly into the active text cursor on Windows. Prefix matching and final-transcript reconciliation keep evolving speech results aligned without duplicate text."
author_profile: true
share: false
comments: false
---

**Apr 2026 — Present**

An open-source system that streams smartphone speech recognition directly into the active text cursor on Windows. Prefix matching and final-transcript reconciliation keep evolving speech results aligned without duplicate text.

## Technical work

- Streamed character-level recognition results over WebSocket between a Kotlin/Flutter mobile client and Python/React Windows application.
- Reused smartphone-native, on-device speech recognition without running an inference model on the desktop.
- Implemented prefix matching and final-transcript reconciliation to handle unstable partial recognition results and prevent duplicate or missing text.


**Technologies / topics:** Kotlin / Flutter, Python, React

[Explore the code](https://github.com/WestbrookLong/FlowVoice)
