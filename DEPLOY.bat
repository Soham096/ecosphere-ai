@echo off
REM Deployment script for EcoSphere AI (Windows Batch)

echo.
echo 🚀 EcoSphere AI - Deployment Guide
echo ====================================
echo.
echo Step 1: Create GitHub Repository
echo   - Go to: https://github.com/new
echo   - Repo name: ecosphere-ai
echo   - Make it PUBLIC
echo   - Click "Create repository"
echo.
echo Step 2: After creating the repo, run these commands:
echo.
echo   git remote add origin https://github.com/YOUR_USERNAME/ecosphere-ai.git
echo   git branch -M main
echo   git push -u origin main
echo.
echo   (Replace YOUR_USERNAME with your actual GitHub username)
echo.
echo Step 3: Deploy to Streamlit Cloud
echo   - Go to: https://share.streamlit.io
echo   - Sign in with GitHub
echo   - Click "New app"
echo   - Select your repo: YOUR_USERNAME/ecosphere-ai
echo   - Branch: main
echo   - Main file: app.py
echo   - Click "Deploy"
echo.
echo Your app will be live in ~30 seconds!
echo.
pause
