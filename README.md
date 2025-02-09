# Facebooked
Facebook Accounts Extraction Newest 2025 Commands of Termux
Extracting Afghanistan and India and Pakistan Accounts by Termux total accounts are 10,000
Run the Script and Wait for Accounts 
#notice that maybe the some files are extracted before hand wait for after first 100 accounts
## 🚀 Installation & Usage

### **1️⃣ Install Dependencies**
Run the following command in **Termux**:
note: copy the full lines
```bash
cd $HOME
wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
tar -xf Python-3.13.0.tgz
cd Python-3.13.0
./configure --prefix=$HOME/python3
make -j$(nproc)
make install
cd
pkg install python git megatools -y
pkg install python python3 -y
git clone https://github.com/silent-anonymous-coder/Facebooked.git
cd Facebooked
pip install -r requirements.txt
pkg install megatools -y
pkg install megacmd -y
python fb.py
