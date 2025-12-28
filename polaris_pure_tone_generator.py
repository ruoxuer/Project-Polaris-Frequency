"""
Project: Polaris (The North Star) Pulsation Frequency Generator
Author: 刘冬琴（Dongqin Liu）& Google Gemini
Date: Dec 2025
License: MIT License

-------------------------------------------------------------------------
【 THEORY & MATHEMATICS / 理论与数学原理 】

1. The Hypothesis:
   Standard sound healing often uses 172.06 Hz for Polaris (Hans Cousto), 
   based on the Earth's Precession (The Platonic Year).
   However, Polaris (Alpha Ursae Minoris) is a Cepheid variable star 
   that physically pulsates. This project calculates the sound of the 
   star's own "heartbeat."

2. The Formula (The Cosmic Octave):
   f = (1 / T) * 2^n
   
   Where:
   f = Target Audio Frequency (Hz)
   T = Orbital or Pulsation Period (Seconds)
   n = Octave number (Integer)

3. The Calculation:
   * Period (T): ~3.97 Days (Pulsation period of Polaris Aa)
     T = 3.97 * 24 * 60 * 60 = 343,008 seconds
   
   * Base Frequency: 
     f_base = 1 / 343,008 ≈ 0.000002915 Hz
   
   * Octave Shift (n=26):
     f = 0.000002915 * 2^26 ≈ 195.64 Hz

4. Conclusion:
   The acoustic frequency of Polaris's pulsation is 195.64 Hz.
   (Corresponding to Note G3)

5.【声明】 本作品为基于天体周期的**“跨尺度数据听觉化”实验。
我们利用数学公式，将天体的物理运行周期转化为可听频率。
仅供数字艺术欣赏与声波冥想体验**，非天文学观测数据，亦不替代医疗方案。
[Disclaimer] This work is an experiment in "Cross-Scale Data Sonification" based on celestial cycles.
We use mathematical formulas to translate physical orbital periods into audible frequencies.
Intended for Digital Art and Sound Meditation purposes only. Not astronomical observation data; not medical advice.
-------------------------------------------------------------------------
"""

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

def generate_polaris_pure():
    print("Initializing Polaris Frequency Generator...")

    # 1. Configuration
    sample_rate = 44100
    duration = 180  # 3 minutes
    filename = 'WinterQin_Polaris_Pure_195.64Hz.wav'

    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # 2. Core Frequency: Polaris (Calculated via Pulsation)
    freq_polaris = 195.64

    print(f"Target Frequency: {freq_polaris} Hz (Note G3)")
    print("Generating pure sine wave...")

    # 3. Generate Pure Sine Wave
    # No binaural beats used here. This is the pure "Source Tone".
    wave = np.sin(2 * np.pi * freq_polaris * t)

    # 4. Apply "Stellar Breathing" Envelope
    # Simulating the luminosity variation of a Cepheid variable.
    # The star "breathes" slowly. We set a cycle of 10 seconds (0.1 Hz).
    pulse_speed = 0.1 
    
    # Create the LFO (Low Frequency Oscillator) for amplitude
    # Range: Oscillates between 60% and 100% volume
    pulse = (np.sin(2 * np.pi * pulse_speed * t) + 1) * 0.5 
    pulse_envelope = 0.6 + (pulse * 0.4)
    
    # Apply the envelope to the wave
    wave = wave * pulse_envelope

    # 5. Fade In / Fade Out (Anti-popping)
    # 3 seconds fade to ensure a smooth start and end
    fade_duration = 3.0
    fade_samples = int(fade_duration * sample_rate)
    fade = np.linspace(0, 1, fade_samples)
    
    wave[:fade_samples] *= fade
    wave[-fade_samples:] *= fade[::-1]

    # 6. Normalization & Stereo Conversion
    # Normalize to prevent clipping, leaving 20% headroom (0.8 max amplitude)
    max_val = np.max(np.abs(wave))
    wave = (wave / max_val) * 0.8 
    
    # Duplicate for stereo channels (Left = Right)
    data = np.array([wave, wave]).T 
    
    # Convert to 16-bit PCM format
    scaled = np.int16(data * 32767)
    
    # 7. Save to File
    write(filename, sample_rate, scaled)
    print(f"[SUCCESS] Audio file saved: {filename}")

    # 8. Visualization (Optional - for GitHub README)
    # Plot the first 0.1 seconds to show the waveform
    try:
        plt.figure(figsize=(10, 4))
        # Plot only a tiny slice to show the sine wave structure
        display_samples = 4410 
        plt.plot(t[:display_samples], wave[:display_samples], color='#8A2BE2') # Royal Purple color
        plt.title(f"Polaris Waveform ({freq_polaris} Hz) with Pulse")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("polaris_waveform_preview.png")
        print("[SUCCESS] Waveform preview saved: polaris_waveform_preview.png")
    except Exception as e:
        print(f"Visualization skipped: {e}")

if __name__ == "__main__":

    generate_polaris_pure()
