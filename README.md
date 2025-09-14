# 📖 Description<br>
A simple and minimal app to keep you focused. The main feature is the intentionally annoying window that always stays on top of what you're currently doing, not letting you get sidetracked. It doesn't try to be something else, just a simple reminder that you can't move on to the next thing until this gets done.

# 🚀 Installation & Deployment<br>
```bash
git clone https://github.com/lukakosanovicc/FocusPro.git
```
```bash
cd FocusPro
```
`cd mac` or `cd windows` depending on your OS and then:
```bash
python3 main.py
```
↳ NOTE: you may need to `pip3 install` some modules to run the script
- Or you can run the application by just downloading the release for your OS

# 🎯 Features & Showcase
![FocusPro](https://github.com/user-attachments/assets/5f6288b1-96e2-46b4-a0b7-17032a8c9f2f)
PRO TIP: if you don't want to touch your mouse at all use tab and shift + tab to cycle through options, space to click the selected option

# 📝 Data Format<br>
tasks.txt -> a file to store current tasks that need to be done<br>
done.txt -> a file to store completed tasks<br>

- The tasks are intentionally stored in text files rather than binary, for easier manipulation outside of the application (sacrifising some speed for ease of use)

## 👉 Accessing the files
- tasks.txt is accessed within the application, but both files can also be found in `Documents > FocusPro` on Windows, and on MacOS:
```bash
cd ~/Applications/FocusPro.app/Contents/Resources
```
```bash
open .
```
↳ or open the files with an editor like vim or nano

# 🤝 Contributing<br>
Contributions are welcome! Please open issues or submit pull requests for suggestions, improvements and ideas.
