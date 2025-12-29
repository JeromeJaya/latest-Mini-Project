# VisioLearn AI - Interactive Learning Platform

# Project link https://jeromejaya.github.io/latest-Mini-Project/

A comprehensive AI-powered educational platform that transforms traditional study materials into interactive, visual learning experiences.

## Features

### 📚 Core Learning Tools

- **Interactive Learning Stories** - Transform text content into engaging visual narratives
- **Smart Scheduler** - AI-powered study planning with personalized daily segments
- **Material Management** - Upload, organize, and track study materials
- **AI Quiz Generator** - Auto-generate quizzes from your study content
- **Progress Dashboard** - Visualize learning consistency and completion rates

### 🎯 Additional Features

- **Text Capture** - Extract text from images using camera
- **Job Finder** - Search and save job listings in India
- **AI Assistant** - Chat with AI about your progress and schedule
- **Image Generator** - Create visual aids for learning

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **AI Integration:** NVIDIA API (Llama 3.1), OpenAI-compatible endpoints
- **APIs:** JSearch (Jobs), RapidAPI services

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd latest-mini-project
   ```

2. **Install dependencies**

   ```bash
   pip install fastapi uvicorn python-multipart jinja2 openai
   ```

3. **Run the application**

   ```bash
   uvicorn txtToTxt:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application**
   - Open your browser and navigate to: `http://localhost:8000`

## Usage

### Materials Management

1. Navigate to the home page
2. Click "Manage My Learning materials" or go to `/materials.html`
3. Upload files (PDF, DOCX, TXT, etc.) or manually add materials
4. Organize by type: Theory, Diagrammatic, Problematic, Programming

### Study Scheduler

1. Go to `/scheduler.html`
2. Add tasks with deadlines and priorities
3. View AI-generated learning segments
4. Track progress on calendar view

### Interactive Learning

1. Select a material from your collection
2. Click "Learn" to start interactive learning
3. Generate visual story slides from content
4. Use voice narration and toggle between original/story modes

### Quiz Generation

1. Complete learning segments in the scheduler
2. Click "Take Quiz" on completed tasks
3. AI generates 10 multiple-choice questions
4. Review results and track scores

### Job Search

1. Navigate to `/job.html`
2. Search for jobs by keywords and location
3. Filter by employment type and posting date
4. Save jobs for later review

## Project Structure

```
latest-mini-project/
├── txtToTxt.py           # Main FastAPI application
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── materials.html    # Material management
│   ├── scheduler.html    # Study planner
│   ├── shorts.html       # Interactive learning
│   ├── quiz.html         # Quiz interface
│   ├── dashboard.html    # Progress tracking
│   ├── job.html          # Job finder
│   ├── camera.html       # Text capture
│   ├── assistant.html    # AI assistant
│   └── ...               # Other templates
└── .gitignore           # Git ignore rules
```

## API Configuration

The application uses the following APIs:

- **NVIDIA API**: For AI chat and content generation
- **JSearch API**: For job listings (via RapidAPI)
- **OpenAI-compatible endpoints**: For various AI features

API keys are configured in the respective template files. Update them as needed.

## Features Details

### Smart Scheduler

- Calendar view with drag-and-drop tasks
- AI-generated daily learning segments
- Progress tracking and statistics
- Time-based task organization
- Deadline notifications

### Interactive Learning

- Story mode: Transforms content into narrative format
- Image generation for visual aids
- Voice narration support
- Progress tracking per slide
- Toggle between original and story content

### Material Management

- File upload support (PDF, DOCX, TXT, PY, etc.)
- Automatic content extraction
- Deadline tracking
- Progress visualization
- Schedule generation from materials

### Dashboard Analytics

- Study consistency charts
- Material completion rates
- Job-specific progress tracking
- Motivational quotes with voice
- 3D progress visualization

## Browser Compatibility

- Chrome (Recommended)
- Firefox
- Edge
- Safari

## Local Storage

The application uses browser localStorage to save:

- Study materials
- Learning schedules
- Quiz results
- Saved jobs
- User preferences

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Built with ❤️ for learners everywhere**
