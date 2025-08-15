# Keylogger

A lightweight Python script that logs keyboard input and saves it into a specified folder.

---

## Table of Contents

1. [About](#about)
2. [Disclaimer](#disclaimer)
3. [Usage](#usage)
4. [Options](#options)
5. [Installation](#installation)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

---

## About

This is a simple keylogging utility written in Python that captures keyboard input and stores it as log files in a folder defined by the user. 
GitHub

---

## Disclaimer

THIS PROJECT IS TO BE USED FOR EDUCATIONAL PURPOSES ONLY.
Unauthorized monitoring or use of this tool for malicious or illegal activities is strictly prohibited. The author is not responsible for any misuse. 
GitHub

---

## Usage

```bash
keylogger -i <interval>
```

`-i <interval>`: Defines the time interval (in seconds) between log captures.

---

## Options

`-q, --quiet`: Suppresses output to stdout (quiet mode).

`-f <folder>, --folder <folder>`: Specifies the destination folder for the log files. 

---

## Installation

### Clone the repository

```bash
git clone https://github.com/SavvyHex/Keylogger.git
cd Keylogger
```

### If using a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies (if any are required)

```bash
pip install -r requirements.txt
```

---

## Examples

Run the keylogger with a 5-second interval and log output visible:

```bash
keylogger -i 5
```

Run quietly and save logs to a specific folder:

```bash
keylogger -i 10 -q -f ./logs
```

## Contributing

Contributions are always welcome! Some ways you can get involved:

1. Add command-line handling (e.g., using argparse) for improved usability
2. Enhance the logging mechanism (e.g., timestamp support, encryption, structured output)
3. Add support for macOS and Linux-specific features
4. Create meaningful error handling and diagnostics
5. Improve documentation and add examples or tests

---

## License

This project is licensed under the MIT License. See the [LICENSE file](LICENSE) for details.
