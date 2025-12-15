# 💡 power schedule

A simple and quick Python tool to check the electricity availability (power 'ON' or 'OUT') for specific consumer groups. Just enter the Group, Date, and Time, and get the power status instantly\!

#### [Video Demo](https://youtu.be/FGm4_gQFdPY?si=lUzp5Y38EgdW1MQr)

## 🌟 The Story Behind the Program

In our country, receiving electricity only within certain periods has become a daily reality since 2023. This rotating schedule, which essentially divides consumption into two groups, is disruptive and highly unproductive when making plans.

This simple Python script is my way of solving this problem. It instantly calculates the expected power status, ensuring you know whether a specific location will have electricity at a given moment.

## ✨ Features

  * **Group Status Check:** Determines if power is **ON** or **OUT** for Group A or Group B.
  * **Time Flexibility:** Accepts various time formats (e.g., `'14:30'`, `'4:30pm'`, `'5'`).
  * **Date-Based Rotation:** Accurately tracks the schedule rotation based on the days passed since the reference date (28 November 2025).
  * **Sunday Rule:** Incorporates the special, fixed Sunday schedule for all groups.

## 🛠️ Technology Stack

  * **Python 3**
  * **`datetime` module**
  * **`re` (Regular Expression) module**

## 🚀 How to Use

1.  **Save the Python Code:** Save the provided code as a Python file (e.g., `power_schedule.py`).

2.  **Run the File** in your terminal or command prompt:

    ```bash
    python power_schedule.py
    ```

3.  **Enter the Group** (e.g., `A` or `B`) when prompted.

4.  **Enter the Date** in `dd/mm/yyyy` format (e.g., `15/12/2025`).

5.  **Enter the Time** in any supported format (e.g., `14:30`, `4:30pm`, `5`).

6.  The **Power Status Result** box will instantly update with the detailed status.
