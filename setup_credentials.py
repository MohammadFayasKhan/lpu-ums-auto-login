"""
LPU UMS Keychain Credential Setup
---------------------------------

This script securely stores your LPU UMS username and password
in the macOS Keychain using Python's `keyring` module.

Once stored, the credentials can be retrieved securely by automation scripts
without hardcoding them into the source code.

Run this **once only** to store your credentials.

Author: @Fayas
GitHub: https://github.com/MohammadFayasKhan/lpu-ums-auto-login
"""

import keyring

# 🔐 Replace these values with your actual credentials
UMS_USERNAME = "Your-Registration-Number"
UMS_PASSWORD = "Your-Ums-Password"

# 🔑 Store credentials in macOS Keychain
keyring.set_password("lpu-ums", "username", UMS_USERNAME)
keyring.set_password("lpu-ums", "password", UMS_PASSWORD)

print("✅ Credentials stored securely in macOS Keychain.")