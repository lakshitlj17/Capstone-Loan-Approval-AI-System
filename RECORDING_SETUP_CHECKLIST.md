# 🎬 OBS Recording Setup Checklist

## Pre-Recording Setup

### 1. Install OBS Studio
```bash
sudo apt update
sudo apt install obs-studio
```

### 2. Launch OBS
```bash
obs
```

### 3. Configure Settings

#### Output Settings
- Click `Settings` → `Output`
- Set **Output Mode**: `Advanced`
- Under **Recording**:
  - **Recording Path**: `/home/ubuntu/Videos/` (or your preferred location)
  - **Recording Format**: `mkv` (or `mp4`)
  - **Encoder**: `libx264` (H.264 for MP4) or `libx265` (HEVC for better quality)
  - **Bitrate**: `6000 Kbps` (good balance)
  - **Keyframe Interval**: `2`

#### Audio Settings
- Click `Settings` → `Audio`
- **Sample Rate**: `48 kHz`
- **Channels**: `Stereo`
- Set your microphone as input device

#### Video Settings
- Click `Settings` → `Video`
- **Base (Canvas) Resolution**: `1920x1080` (Full HD) or `1280x720` (HD)
- **Output (Scaled) Resolution**: Same as base
- **Common FPS Values**: `30` (smooth) or `60` (very smooth)

### 4. Add Video Source

In OBS main window:
1. Click **Sources** section (bottom-left)
2. Click **`+`** button
3. Select **`Screen Capture`** (to record entire screen)
   - OR select **`Window Capture`** (to record just the browser)
4. Click **`Create New`**
5. Select your display/window
6. Click **`OK`**
7. Resize/position in the canvas area

### 5. Add Audio (Microphone)

1. Click **`+`** in Sources
2. Select **`Audio Input Capture`**
3. Click **`Create New`**
4. Select your microphone from dropdown
5. Click **`OK`**

### 6. Test Recording

1. Click **`Start Recording`** (red button at bottom)
2. Record a quick 30-second test
3. Click **`Stop Recording`**
4. Check video file in `/home/ubuntu/Videos/`

---

## Pre-Demo Preparation

### Terminal Preparation

**Terminal 1 Setup** (Backend):
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
# Make sure .env file exists with valid API keys
ls -la .env
```

**Terminal 2 Setup** (Frontend):
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
streamlit config show  # Verify Streamlit installation
```

### Application Readiness

1. **Check .env file**:
   ```bash
   cat "/home/ubuntu/Desktop/Capstone Project/Loan AI Project/.env"
   ```
   Should have:
   ```
   LLMGW_API_KEY=your_key_here
   LLMGW_BASE_URL=https://llmgw-wp.tekstac.com
   ```

2. **Verify Python packages**:
   ```bash
   pip list | grep -E "fastapi|streamlit|langgraph|langchain"
   ```

3. **Check port availability**:
   ```bash
   # Make sure ports 8000 and 8501 are free
   netstat -tuln | grep -E "8000|8501"
   ```

---

## Recording Day Schedule

### 60 Minutes Before
- [ ] Clear desk/screen clutter
- [ ] Restart computer for clean state
- [ ] Test microphone levels in OBS
- [ ] Close unnecessary applications

### 30 Minutes Before
- [ ] Start OBS Studio
- [ ] Configure all settings (above)
- [ ] Do a 1-minute test recording
- [ ] Verify audio and video quality
- [ ] Check output file location

### 15 Minutes Before
- [ ] Open 3 terminals
- [ ] Navigate to project directory in each
- [ ] Have the DEMO_RECORDING_SCRIPT.md ready
- [ ] Open browser (but don't navigate yet)
- [ ] Have test data written down (optional)

### Recording Start (5 Minutes Before)
1. **Terminal 1**: Start backend
   ```bash
   cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
   python -m uvicorn api:app --host 127.0.0.1 --port 8000 --reload
   ```

2. **Terminal 2**: Start frontend
   ```bash
   cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
   streamlit run app.py --server.port 8501
   ```

3. **Terminal 3**: Keep ready for API testing
   ```bash
   cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
   ```

4. **Wait** until you see:
   - "Uvicorn running on http://127.0.0.1:8000"
   - "You can now view your Streamlit app in your browser at http://localhost:8501"

5. **In OBS**: Click **`Start Recording`**

6. **Open browser** and navigate to: `http://localhost:8501`

---

## During Recording

### Best Practices
- [ ] Speak clearly and at moderate pace
- [ ] Click slowly so actions are visible
- [ ] Pause between sections (can edit later)
- [ ] Point out important details
- [ ] Allow time for results to load
- [ ] Test 2-3 scenarios with different data
- [ ] Show terminal outputs clearly

### Recommended Narration Pacing
- **Introduction**: 90 seconds
- **Code walkthrough**: 3-4 minutes
- **Architecture explanation**: 2-3 minutes
- **Demo walkthrough**: 8-10 minutes
- **Conclusion**: 1 minute

---

## Post-Recording

### Immediate After
1. Click **`Stop Recording`** in OBS
2. Wait 10 seconds for file to finalize
3. Check the output file exists:
   ```bash
   ls -lh ~/Videos/*.mkv
   ```

### File Verification
```bash
# Check file size and duration
ffmpeg -i ~/Videos/loan_system_demo.mkv

# Play the file
vlc ~/Videos/loan_system_demo.mkv
```

### File Organization
```bash
# Move to a specific location if needed
mv ~/Videos/loan_system_demo.mkv "/home/ubuntu/Desktop/Capstone Project/demo_video.mkv"
```

---

## Troubleshooting

### Audio Issues
- **No audio**: Check microphone selected in OBS Audio settings
- **Low volume**: Adjust microphone gain (right-click audio source)
- **Background noise**: Use noise suppression (Filters → Add → Noise Suppression)

### Video Issues
- **Laggy recording**: Reduce bitrate or resolution
- **Choppy playback**: Use lower FPS (30 instead of 60)
- **API timeouts**: Ensure stable internet connection

### Application Issues
- **Backend won't start**: Check port 8000 isn't in use: `lsof -i :8000`
- **Frontend won't start**: Check port 8501 isn't in use: `lsof -i :8501`
- **API errors**: Verify .env file has correct credentials

### OBS Won't Record
```bash
# Check if OBS crashed
journalctl -e | grep obs

# Restart OBS and try again
killall obs; obs
```

---

## Quick Commands Reference

**Start Backend**:
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project" && python -m uvicorn api:app --host 127.0.0.1 --port 8000 --reload
```

**Start Frontend**:
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project" && streamlit run app.py --server.port 8501
```

**Test API**:
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 35, "income": 85000, "employment": "Full-time", "loan_amount": 120000}'
```

**Find Video File**:
```bash
find ~/Videos -name "*.mkv" -o -name "*.mp4" | sort -rn | head -1
```

---

## File Locations

| Item | Path |
|------|------|
| Project Root | `/home/ubuntu/Desktop/Capstone Project/` |
| Backend Code | `/home/ubuntu/Desktop/Capstone Project/Loan AI Project/api.py` |
| Frontend Code | `/home/ubuntu/Desktop/Capstone Project/Loan AI Project/app.py` |
| Orchestrator | `/home/ubuntu/Desktop/Capstone Project/Loan AI Project/orchestrator.py` |
| Agents | `/home/ubuntu/Desktop/Capstone Project/Agents/` |
| Demo Script | `/home/ubuntu/Desktop/Capstone Project/DEMO_RECORDING_SCRIPT.md` |
| Video Output | `/home/ubuntu/Videos/` |

---

**Ready to record? Start with the Pre-Recording Setup section!**
