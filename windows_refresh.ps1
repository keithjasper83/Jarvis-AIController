<#
    Windows PowerShell script to refresh and run the latest working build
    Only runs if a new working tag is detected
    Requires SSH access to GitHub and Docker installed
#>

$repoPath = "C:\Jarvis-AIController"
$tagFile = "$repoPath\last_deployed_tag.txt"

# Fetch latest code and tags
cd $repoPath

git fetch --all
$latestTag = git tag --sort=-creatordate | Select-Object -Last 1

# Read last deployed tag
if (Test-Path $tagFile) {
    $lastTag = Get-Content $tagFile
} else {
    $lastTag = ""
}

if ($latestTag -ne $lastTag) {
    Write-Host "New tag detected: $latestTag (was: $lastTag)"
    # Stop and remove all running containers
    cd "$repoPath\jarvis-mcp"
    docker-compose down

    # Checkout latest tag
    cd $repoPath
    git checkout $latestTag

    # Rebuild and start containers
    cd "$repoPath\jarvis-mcp"
    docker-compose pull
    docker-compose up --build -d

    # Update last deployed tag
    Set-Content -Path $tagFile -Value $latestTag
    Write-Host "Refreshed and running tag: $latestTag"
} else {
    Write-Host "No new tag detected. Current tag: $lastTag"
}