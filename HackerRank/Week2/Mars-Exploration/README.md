## 🗒️ Problem Description

A space explorer's ship crashed on Mars! They send a series of `SOS` messages to Earth for help.

Letters in some of the `SOS` messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, `s`, determine how many letters of the `SOS` message have been changed by radiation.

## 💡 Notes to solve the problem
- Looping the string in 3 steps since the `SOS` message is with 3 letters.
- In every loop, slice the string `s[i:i+3]` to check the 3 letter and then compare eache alphabet with the `original_signal==SOS`, count the number of alphabets that have been changed.
