# 실행 명령어
# Set-ExecutionPolicy Bypass -Scope Process
# .\develop_win.ps1

# 현재 스크립트가 위치한 폴더 (프로젝트 폴더)
$projectDir = (Get-Item -Path ".\").Parent.FullName

Write-Host $projectDir
# 상위 폴더에 가상환경 생성
$venvPath = Join-Path $projectDir "venv"

# 설치 requirements.txt 이름
$requirementsname = "dev_requirements.txt"

# dev_requirements.txt 경로
$requirementsPath = Join-Path $projectDir $requirementsname

Write-Host $requirementsPath

# 1. 가상환경 생성 확인
if (-Not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath..."
    python -m venv $venvPath
} else {
    Write-Host "Virtual environment already exists at $venvPath."
}

# 2. 가상환경 활성화
$activateScript = Join-Path $venvPath "Scripts\Activate"
Write-Host "Activating virtual environment..."
& $activateScript

# 3. 가상환경 내 pip 연결
$venvPip = Join-Path $venvPath "Scripts\pip.exe"

# 4. 패키지 설치 확인 및 설치
if (Test-Path $requirementsPath) {
    $installedPackages = & $venvPip list | Out-String
    $requirements = Get-Content $requirementsPath

    foreach ($package in $requirements) {
        $packageName = $package -split '==' | Select-Object -First 1
        if ($installedPackages -like "*$packageName*") {
            Write-Host "$packageName is already installed."
        } else {
            Write-Host "Installing $packageName..."
            & $venvPip install $package
        }
    }
} else {
    Write-Host "requirements.txt not found. Skipping package installation."
}

Write-Host "Setup completed!"
