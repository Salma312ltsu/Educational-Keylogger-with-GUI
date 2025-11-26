# Educational-Keylogger-with-GUI
# Educational Keylogger with GUI



A Python-based educational keylogger with a graphical user interface designed for **cybersecurity learning purposes only**. This tool demonstrates how keylogging works to help security professionals understand attack vectors and develop better defensive strategies.

## ⚠️ LEGAL DISCLAIMER

**READ THIS CAREFULLY BEFORE USING THIS SOFTWARE**

This tool is provided for **EDUCATIONAL AND RESEARCH PURPOSES ONLY**. 

### Legal Requirements:
- ✅ **ONLY** use on systems you own or have explicit written permission to test
- ✅ Use in isolated virtual machines or lab environments
- ✅ For cybersecurity education, security research, or authorized penetration testing
- ❌ **NEVER** use on systems without authorization
- ❌ **NEVER** use to monitor others without consent
- ❌ **NEVER** use for malicious purposes

### Legal Consequences:
Unauthorized use of keyloggers is **ILLEGAL** in most jurisdictions and may violate:
- Computer Fraud and Abuse Act (CFAA) in the United States
- Computer Misuse Act in the United Kingdom
- Similar laws worldwide regarding unauthorized access and privacy violations

**Penalties can include:**
- Criminal prosecution
- Heavy fines
- Imprisonment
- Civil lawsuits

**By using this software, you agree to use it responsibly and legally.**

---

## 🎓 Educational Purpose

This project helps cybersecurity students and professionals understand:
- How keyloggers capture keyboard input
- GUI application development for security tools
- Event-driven programming and keyboard hooks
- The importance of protecting systems against such threats
- Detection and prevention strategies

## 🌟 Features

- **Real-time Monitoring** - Capture keystrokes as they happen
- **User-Friendly GUI** - Easy-to-use graphical interface built with Tkinter
- **Session Tracking** - Timestamps for monitoring sessions
- **Statistics** - Track total keys captured
- **Start/Stop Controls** - Simple controls for monitoring
- **Clear Log Function** - Reset captured data easily
- **Visual Warnings** - Prominent disclaimers about ethical use

## 📋 Requirements

- Python 3.7 or higher
- `pynput` library
- `tkinter` (usually included with Python)

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/educational-keylogger.git
cd educational-keylogger
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pynput
```

3. **Run the application:**
```bash
python keylogger_gui.py
```

## 💻 Usage

### Basic Operation

1. Launch the application
2. Read and accept the disclaimer
3. Click **"Start Monitoring"** to begin capturing keystrokes
4. Type in any application to see captured keys in real-time
5. Click **"Stop Monitoring"** to end the session
6. Use **"Clear Log"** to reset the display

### Safe Testing Environment

**Recommended setup for learning:**

1. **Use a Virtual Machine:**
   - VirtualBox
   - VMware
   - Hyper-V

2. **Disconnect from Network:**
   - Ensures data stays local
   - Prevents accidental transmission

3. **Isolated Environment:**
   - Don't use on production systems
   - Keep test data separate

## 🛡️ Defense & Detection

Understanding keyloggers helps you protect against them:

### Detection Methods:
- Monitor running processes for suspicious activity
- Check startup programs and scheduled tasks
- Use anti-malware and anti-keylogger software
- Review file system for unauthorized logs
- Monitor network traffic for data exfiltration
- Check for unusual CPU or disk activity

### Prevention Strategies:
- Keep operating system and software updated
- Use reputable antivirus/anti-malware solutions
- Be cautious with downloaded software
- Use virtual keyboards for sensitive input
- Enable two-factor authentication
- Regular security audits

## 📁 Project Structure

```
educational-keylogger/
│
├── keylogger_gui.py      # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # License information
└── .gitignore          # Git ignore file
```

## 🔧 Technical Details

### How It Works:

1. **Keyboard Hooking:** Uses `pynput.keyboard.Listener` to capture keyboard events
2. **Event Handling:** Processes both regular keys and special keys (Enter, Space, etc.)
3. **GUI Updates:** Uses Tkinter's thread-safe methods to update the interface
4. **Session Management:** Tracks monitoring sessions with timestamps

### Code Overview:

```python
# Key components:
- KeyloggerGUI class: Main application logic
- on_key_press(): Handles key press events
- update_log(): Updates GUI display
- Threading: Runs listener in background
```

## 🎯 Learning Objectives

After using this tool, you should understand:

1. **How keyloggers work** at a technical level
2. **GUI development** for security tools
3. **Event-driven programming** concepts
4. **Threading** in Python applications
5. **Ethical considerations** in security research
6. **Detection and prevention** strategies

## 🔐 Ethical Use Guidelines

### ✅ DO:
- Use on your own devices only
- Test in isolated virtual machines
- Study for defensive security purposes
- Document your research
- Share knowledge responsibly
- Report vulnerabilities through proper channels

### ❌ DON'T:
- Use on systems without authorization
- Deploy in work or shared environments
- Distribute with malicious intent
- Bypass security measures without permission
- Share captured sensitive data
- Use for harassment or stalking

## 🤝 Contributing

Contributions are welcome! Please ensure:

- All contributions maintain educational focus
- Code includes proper warnings and disclaimers
- Documentation emphasizes legal and ethical use
- Features enhance learning, not malicious capability

### How to Contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add educational feature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📚 Further Learning

### Recommended Resources:

**Online Platforms:**
- [TryHackMe](https://tryhackme.com/) - Practical cybersecurity training
- [HackTheBox](https://www.hackthebox.com/) - Penetration testing labs
- [OWASP](https://owasp.org/) - Web application security

**Certifications:**
- CompTIA Security+
- Certified Ethical Hacker (CEH)
- Offensive Security Certified Professional (OSCP)

**Books:**
- "The Web Application Hacker's Handbook"
- "Metasploit: The Penetration Tester's Guide"
- "Black Hat Python"

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note:** The MIT License does NOT grant permission to use this software illegally. You are responsible for ensuring your use complies with all applicable laws.

## ⚠️ Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. The authors and contributors are not responsible for any misuse or damage caused by this software. Users are solely responsible for ensuring their use complies with all applicable laws and regulations.

## 📧 Contact

For questions about educational use or security research:

- Open an issue on GitHub
- Email: salmaahmedccso2024@gmail.com


## 🙏 Acknowledgments

- Inspired by the need for better cybersecurity education
- Thanks to the security research community

---

**Remember: With great power comes great responsibility. Use this knowledge to protect, not to harm.**

---

## 📊 Project Status


**Last Updated:** November 2025
