param(
  [Parameter(Mandatory=$true)][string]$Out,
  [string]$Params = ""
)
# Rend une carte LinkedIn Cresceo (card.html) en PNG via navigateur headless.
# Les valeurs des paramètres peuvent contenir espaces/accents : elles sont URL-encodées ici.
# Ex : .\render.ps1 -Out "..\drafts\weekly\2026-W41-plain-pied.png" -Params "type=tips&kicker=Prévention · HSE&title=Chutes de *plain-pied*&t1=...&t2=...&t3=..."
$ErrorActionPreference = "Stop"
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$tpl = Join-Path $dir "card.html"

$edge = @(
  "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
  "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
  "C:\Program Files\Google\Chrome\Application\chrome.exe",
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw "Edge ou Chrome introuvable." }

$enc = ($Params -split '&' | ForEach-Object {
  if ($_ -eq "") { return }
  $kv = $_ -split '=', 2
  if ($kv.Count -eq 2) { $kv[0] + '=' + [uri]::EscapeDataString($kv[1]) } else { $_ }
}) -join '&'

$url = "file:///" + ($tpl -replace '\\','/')
if ($enc) { $url += "?" + $enc }

& $edge --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --virtual-time-budget=6000 --window-size=1080,1080 ("--screenshot=" + $Out) $url | Out-Null
Write-Host "Rendu -> $Out"
