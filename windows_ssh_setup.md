# Windows SSH Setup for Private GitHub Repo

1. Open PowerShell and run:
   ```powershell
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   Press Enter to accept defaults.

2. Add the public key to GitHub:
   - Copy the contents of `C:\Users\<YourUser>\.ssh\id_ed25519.pub`
   - Go to GitHub > Settings > SSH and GPG keys > New SSH key
   - Paste and save.

3. Test SSH access:
   ```powershell
   ssh -T git@github.com
   ```
   You should see a success message.

4. Clone the repo using SSH:
   ```powershell
   git clone git@github.com:keithjasper83/Jarvis-AIController.git C:\Jarvis-AIController
   ```

Now you can run `windows_refresh.ps1` for automated updates.