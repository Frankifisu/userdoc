Add-Type -assembly System.Windows.Forms

# Function definitions and some default settings
$ErrorActionPreference = "Inquire" # Instead of closing the screen, pause the code at an error.
$ProgressPreference = "SilentlyContinue" # no progress bar, it significantly slows down downloads

Write-Host "Welcome to the AMS Repository download script." -ForegroundColor Cyan
Write-Host "This script will interactively help you download a copy of the AMS repository for offline usage of AMSpackages."
""
Write-Host "You will receive several prompts."
Write-Host "Please provide the necessary information in the interactive GUI prompts." 
Write-Host "Afterwards, the download will commence automatically."
Write-Host "This process may take a while, depending on your connection."
Write-Host "The overall download size is about 15GB." -ForegroundColor Yellow

$proceed = [System.Windows.Forms.MessageBox]::Show((New-Object System.Windows.Forms.Form -Property @{TopMost = $true }), "This script will help you download a copy of the repository used by AMSpackages. To continue, you will need to provide the file list. Please download and provide the list that matches your version of AMS. You can find the list at https://downloads.scm.com/Downloads/packages/listings/.", "About this script", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information) 
if ($proceed -ne "OK") {
        Write-Host "Operation was cancelled by the user." -ForegroundColor Red
        Read-Host -Prompt "You can safely close this window."
        exit                
} 

Write-Host "Please provide the file containing the download, using the gui prompt." -ForegroundColor Magenta
$listingdialog = New-Object System.Windows.Forms.OpenFileDialog
$listingdialog.initialDirectory = Join-Path $env:userprofile "Downloads"
$listingdialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
$listingdialog.Title = "Provide the download list"

if ($listingdialog.ShowDialog((New-Object System.Windows.Forms.Form -Property @{TopMost = $true })) -eq [System.Windows.Forms.DialogResult]::OK) {
    $listpath = $listingdialog.FileName
    Write-Host "Read download list from $listpath"
}
else {
    Write-Host "Operation was cancelled by the user." -ForegroundColor Red
    Read-Host -Prompt "You can safely close this window."
    exit
}


Write-Host "Please provide the download destination, using the gui prompt." -ForegroundColor Magenta
$dialog = New-Object System.Windows.Forms.FolderBrowserDialog
$dialog.Description = "Select a directory to store the repository"
$dialog.SelectedPath = Join-Path $env:userprofile "Downloads"
if ($dialog.ShowDialog((New-Object System.Windows.Forms.Form -Property @{TopMost = $true })) -eq [System.Windows.Forms.DialogResult]::OK) {
    $dlpath = $dialog.SelectedPath
    Write-Host "Directory selected is $dlpath" 
}
else {
    Write-Host "Operation was cancelled by the user." -ForegroundColor Red
    Read-Host -Prompt "You can safely close this window." 
    exit
}


Write-Host "You will now be prompted for credentials." -ForegroundColor Magenta
$cred = Get-Credential -Message "Please provide your SCM login details."

$startdownload = [System.Windows.Forms.MessageBox]::Show((New-Object System.Windows.Forms.Form -Property @{TopMost = $true }), "Proceed with the download? This will take a while depending on your connection. The overall download size is about 15Gb (about 30 minutes at 1 MB/s).", "Continue?", [System.Windows.Forms.MessageBoxButtons]::YesNo, [System.Windows.Forms.MessageBoxIcon]::Question) 
switch ($startdownload) {
    "YES" {
        # Continue even if downloads fail due to permissions.
        $ErrorActionPreference = "Continue"  
        $files = Get-Content $listpath

        ForEach ($file in $files) {    
            Write-Host "Downloading" $file -ForegroundColor Yellow
            $file_url = [System.Uri]$file
            $file_path = Join-Path $dlpath ($file_url.LocalPath).Trim("/")    
            [void](New-Item (Split-Path $file_path) -Force -ItemType Directory)
            Invoke-WebRequest -Credential $cred $file_url -OutFile $file_path    
        }

        Write-Host ""
        Write-Host "All done!" -ForegroundColor Green
        Write-Host "Your download is located in $dlpath"
    } 
    "NO" {
        Write-Host "Operation was cancelled by the user." -ForegroundColor Red
        Read-Host -Prompt "You can safely close this window."
        exit                
    } 
}

while (1) {
    Read-Host -Prompt "You can safely close this window."
}
