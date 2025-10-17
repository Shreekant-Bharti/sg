# 💕 Romantic Surprise Website for Shristi

A beautiful, romantic Flask web application with love notes, memories, and interactive surprises!

## 🚀 Deploy to Render

This application is ready to deploy on Render! Follow these simple steps:

### Step 1: Go to Render Dashboard
1. Visit [https://render.com](https://render.com)
2. Sign up or log in (you can use your GitHub account)

### Step 2: Create New Web Service
1. Click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub account if not already connected
4. Select the repository: **`Shreekant-Bharti/sg`**

### Step 3: Configure the Service
Render will auto-detect most settings, but verify these:

- **Name**: `shristi-romantic-website` (or any name you like)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### Step 4: Environment Variables (Optional)
No environment variables are required for basic deployment.

### Step 5: Deploy!
1. Click **"Create Web Service"**
2. Render will automatically:
   - Install dependencies
   - Build your application
   - Deploy it
   - Give you a live URL like: `https://shristi-romantic-website.onrender.com`

### ⏱️ Deployment Time
- First deployment: 2-5 minutes
- The site will be live at your Render URL

## 📝 Important Notes

- **Free Tier**: Render's free tier spins down after 15 minutes of inactivity. First load after inactivity takes 30-50 seconds.
- **Message Persistence**: Messages saved on the message board will persist in the deployed version.
- **Custom Domain**: You can add a custom domain in Render settings (optional).

## ✨ Features

- 💝 Personalized greeting with animated hearts
- 📸 Photo carousel with 9 special memories
- 💖 120 Reasons Why I Love You (interactive)
- 🎁 Special surprises and memories
- 📝 Private message board
- 💌 Personal love letter
- 🎵 Background music with volume control
- 📱 Fully responsive design

## 🛠️ Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit http://localhost:5000

## 💝 Made With Love

Created with endless love for Shristi 💕

---

**Note**: This is a private romantic website. Handle with care! ❤️
