"""
Project: Polaris Pure Breath Audio Generator
Author: 刘冬琴 (星幻Annie) & AI Assistant & Google Gemini
Date: December 28, 2025
License: MIT Open Source

【 Description 】
Generates a pure sine wave based on the calculated Polaris frequency (195.64 Hz).
Features a slow "Breathing" envelope and Binaural Beats for Theta state induction.

【 Disclaimer / 声明 】
This work is an experiment in "Cross-Scale Data Sonification" based on celestial cycles.
Intended for Digital Art and Sound Meditation purposes only. Not astronomical observation data; not medical advice.
"""

import numpy as np
from scipy.io.wavfile import write

def generate_audio():
    print("Generating Polaris Pure Breath Audio...")

    # Configuration
    sample_rate = 44100
    duration = 32  # 32 Seconds (Demo Length)
    filename = 'DongQin_Polaris_Pure_Breath.wav'

    # Create time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # --- 1. Frequency Settings ---
    # Core Frequency: Polaris (Calculated via Pulsation)
    base_freq = 195.64

    # Binaural Target: Theta Wave (5.5 Hz)
    # Theta is associated with intuition, subconscious connection, and the central axis.
    target_beat = 5.5

    # --- 2. Generate Pure Waveforms ---
    # Left Ear: Base Frequency
    # Right Ear: Base + Target Beat
    left_ear = np.sin(2 * np.pi * base_freq * t)
    right_ear = np.sin(2 * np.pi * (base_freq + target_beat) * t)

    # --- 3. Breathing Pulse (LFO) ---
    # Simulates a slow, deep breath cycle.
    # Set to complete one cycle every 8 seconds (4s Inhale, 4s Exhale).
    # This slow rhythm forces the listener's breathing to slow down.
    breath_speed = 1.0 / 8.0  # 0.125 Hz
    
    # Create the LFO wave (0 to 1 range)
    pulse = (np.sin(2 * np.pi * breath_speed * t) + 1) * 0.5 

    # Adjust Pulse Depth:
    # The sound never goes silent; it oscillates between 40% and 100% volume.
    # This creates a continuous, supporting feeling.
    pulse_depth = 0.4 + (pulse * 0.6)

    # Apply the pulse to the audio
    left_ear = left_ear * pulse_depth
    right_ear = right_ear * pulse_depth

    # --- 4. Fade In / Out (Envelope) ---
    # 5 seconds fade to prevent popping sounds at start/end.
    fade_samples = int(5.0 * sample_rate) 
    fade = np.linspace(0, 1, fade_samples)
    
    # Apply Fade In
    left_ear[:fade_samples] *= fade
    right_ear[:fade_samples] *= fade
    
    # Apply Fade Out
    left_ear[-fade_samples:] *= fade[::-1]
    right_ear[-fade_samples:] *= fade[::-1]

    # --- 5. Normalization & Export ---
    # Normalize to prevent clipping, leaving 10% headroom (0.9)
    max_val = np.max(np.abs(np.array([left_ear, right_ear])))
    data_left = (left_ear / max_val) * 0.9
    data_right = (right_ear / max_val) * 0.9

    # Combine into Stereo and convert to 16-bit PCM
    data = np.array([data_left, data_right]).T
    scaled = np.int16(data * 32767)
    
    write(filename, sample_rate, scaled)

    print(f"[SUCCESS] Audio saved to: {filename}")
    print("Features: Pure Sine Wave, No Bells, 8s Breathing Rhythm.")

if __name__ == "__main__":

    generate_audio()
