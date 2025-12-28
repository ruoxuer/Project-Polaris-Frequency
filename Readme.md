# Project Polaris: The Pulse of the North Star
# 北极星频率研究计划：寻找北极星的心跳

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.x-yellow.svg)

> **"As above, so below."**
> **"在天成象，在地成形。"**

## 🌌 Introduction / 项目简介

In the field of sound healing and planetary frequencies, the standard frequency for Polaris (The North Star) is often cited as **172.06 Hz** (Hans Cousto), based on the Earth's Precession (Platonic Year).
在声音疗愈领域，北极星的通用频率常被定为 **172.06 Hz**（汉斯·库斯托），这是基于地球岁差周期计算的。

However, from an astrophysical perspective, Polaris (Alpha Ursae Minoris) is a **Cepheid variable star** that physically pulsates.
然而，从天体物理学角度看，北极星（勾陈一）是一颗**造父变星**，它本身就在进行物理上的脉动。

**This project proposes a new frequency: 195.64 Hz.**
**本项目提出了一个新的频率标准：195.64 Hz。**

This is the sound of the star's own heartbeat, calculated from its luminosity pulsation period, bridging the gap between Astrophysics and Sound Healing.
这是星星自己的心跳声，基于其光度脉动周期计算得出，旨在连接天体物理学与声音疗愈。

---

## 📐 The Math & Logic / 计算原理

We use the **Cosmic Octave** formula to translate macro-cosmic cycles into micro-cosmic audible frequencies.
我们使用**宇宙八度音**公式，将宏观天体周期转化为微观可听频率。

$$ f = \frac{1}{T} \times 2^n $$

### Calculation Process / 计算过程

1.  **Source Data (数据源):**
    The primary pulsation period of Polaris Aa is approximately **3.97 days**.
    北极星 Aa 的主脉动周期约为 **3.97 天**。

2.  **Conversion (换算):**
    $$ T = 3.97 \times 24 \times 60 \times 60 = 343,008 \text{ seconds} $$

3.  **Base Frequency (基频):**
    $$ f_{base} = 1 / 343,008 \approx 0.000002915 \text{ Hz} $$

4.  **Octave Shift (倍增):**
    We multiply the base frequency by $2^{26}$ to bring it into the audible range.
    我们将基频乘以 2 的 26 次方，将其提升至人耳听觉范围。
    
    $$ f = 0.000002915 \times 67,108,864 \approx \mathbf{195.64 \text{ Hz}} $$

**Conclusion:**
*   **195.64 Hz** matches the note **G3**.
*   It represents the **"Axis"** and **"Stability"**.
*   北极星频率对应音高 **G3**，代表**“中轴”**与**“定力”**。

---

## 📂 File Structure / 文件说明

*   `polaris_pulsation_frequency.py`:
    The core calculation script. Prints the math derivation process.
    核心计算脚本，展示数学推导过程。

*   `polaris_pure_tone_generator.py`:
    Generates a pure sine wave at **195.64 Hz** with a gentle "breathing" envelope (simulating stellar pulsation). No binaural beats.
    生成 **195.64 Hz** 的纯正弦波音频，带有柔和的“呼吸”包络（模拟星体脉动）。不含双耳节拍。

*   `polaris_theta_meditation.py`:
    (Optional) Generates 195.64 Hz + 5.5 Hz Binaural Beats for deep meditation.
    (可选) 生成带 5.5 Hz Theta 脑波的双耳节拍版本，用于深层冥想。

---

## 🧘‍♀️ Usage / 如何使用

1.  Ensure you have Python installed.
    确保已安装 Python。
2.  Install dependencies:
    安装依赖库：
    ```bash
    pip install numpy scipy matplotlib
    ```
3.  Run the script to generate audio:
    运行脚本生成音频：
    ```bash
    python polaris_pure_tone_generator.py
    ```

---
## 【项目声明 / Project Disclaimer】

实验性质： 本项目属于数字艺术与声学心理学的跨界探索，旨在通过编程与可视化手段，探索频率对意识的潜在影响。它不应被视为严谨的天文学科研成果或天体物理学数据报告。
方法论说明： 我们采用的是基于**“宇宙八度音 (The Cosmic Octave)”理论的跨尺度转换模型**。
众所周知，真空无法传播声波。
本项目中的声音，并非对天体的直接录音，而是将其宏观的**“运行周期 (Period)”，通过数学倍增算法，映射（Mapping）至人耳可听的微观“声学频率 (Frequency)”。这是一次数据听觉化 (Data Sonification)** 的实验。

Nature of Project: This project is an interdisciplinary exploration of Digital Art and Psychoacoustics. It aims to visualize frequencies and explore their potential effects on consciousness. It should NOT be cited as professional astronomical research or astrophysical data.
Methodology: We utilize a Cross-Scale Conversion Model based on "The Cosmic Octave" theory.
It is acknowledged that sound cannot travel through a vacuum.
The sounds in this project are not direct recordings of celestial bodies. Instead, they are the result of Data Sonification: mapping macro-cosmic Orbital/Pulsation Cycles into micro-cosmic Audible Frequencies through mathematical octave multiplication.

## ⚖️ Disclaimer / 免责声明

This project is an exploration of Digital Art and Psychoacoustics. It is not a substitute for professional medical treatment.
本项目属于数字艺术与声学心理学的探索，不替代任何专业医疗手段以及天文学研究。

**Creator:** 刘冬琴（Dongqin Liu）& AI Assistant
**Date:** Dec 2025