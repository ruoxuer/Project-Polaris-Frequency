"""
Project: Polaris (The North Star) Pulsation Frequency Calculation
Author: 刘冬琴 (星幻Annie) & Google Gemini
Date: December 28, 2025
License: MIT Open Source

【 Abstract / 项目简介 】
Currently, the standard frequency for Polaris in sound healing is often cited as 172.06 Hz (Hans Cousto), 
based on the Earth's Precession (The Platonic Year).
This project proposes a NEW perspective: Based on the astrophysical fact that Polaris (Alpha Ursae Minoris) 
is a "Cepheid Variable" star, we calculate its intrinsic luminosity pulsation period and convert it into 
an acoustic frequency. 
This aims to explore the difference between the "Earth-Axis Perspective" and the "Stellar-Body Perspective" 
in acoustic representation.

【 Disclaimer / 声明 】
This work is an experiment in "Cross-Scale Data Sonification" based on celestial cycles.
We use mathematical formulas to translate physical orbital periods into audible frequencies.
Intended for Digital Art and Sound Meditation purposes only. Not astronomical observation data; not medical advice.
本作品为基于天体周期的“跨尺度数据听觉化”实验。我们利用数学公式，将天体的物理运行周期转化为可听频率。
仅供数字艺术欣赏与声波冥想体验，非天文学观测数据，亦不替代医疗方案。
"""

import numpy as np

def calculate_polaris_frequency():
    print("--- START: Polaris Pulsation Frequency Calculation ---")
    
    # 1. Define Physical Constants
    # Data Source: Astrophysical observation data for Polaris Aa (Cepheid Variable)
    # The primary pulsation period is approximately 3.97 days.
    pulsation_period_days = 3.97
    
    # Convert days to seconds
    seconds_per_day = 24 * 60 * 60
    period_seconds = pulsation_period_days * seconds_per_day
    
    print(f"1. Physical Period (T): {pulsation_period_days} days = {period_seconds} seconds")
    
    # 2. Calculate Base Frequency (Hz)
    # Formula: f = 1 / T
    freq_base = 1 / period_seconds
    print(f"2. Base Oscillation Frequency: {freq_base:.10f} Hz (Inaudible infrasound)")
    
    # 3. The Cosmic Octave Calculation (Frequency Multiplication)
    # We need to find an octave multiplier (2^n) to bring the frequency into the audible range (100Hz - 300Hz).
    # Here we select the 26th Octave (n=26).
    octave_n = 26
    octave_multiplier = 2 ** octave_n
    
    freq_audible = freq_base * octave_multiplier
    
    print(f"3. Applying Octave Shift (n={octave_n})...")
    print(f"   Amplification Factor: {octave_multiplier}")
    
    # 4. Output Results
    print("-" * 40)
    print(f"【 CALCULATION RESULT 】")
    print(f"Polaris Pulsation Acoustic Frequency: {freq_audible:.2f} Hz")
    print("-" * 40)
    
    # 5. Pitch Comparison
    # 196.00 Hz is the standard G3 note.
    diff = freq_audible - 196.00
    print(f"Pitch Comparison: Very close to G3 (196Hz), deviation is only {diff:.2f} Hz")

if __name__ == "__main__":

    calculate_polaris_frequency()
