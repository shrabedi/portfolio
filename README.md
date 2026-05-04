# Portfolio

A curated collection of production-ready projects showcasing full-stack software engineering, data engineering, machine learning, and web development expertise.

## 📚 Projects

### 1. **DataVault** - Data Processing Utility
- **Type**: Python Data Engineering
- **Languages**: Python
- **Technologies**: Pandas, Polars, PySpark
- **Features**: CSV/JSON/Parquet processing, data transformation, validation framework
- **Status**: Production-ready
- **Path**: `projects/01-datavault/`

```bash
# Usage
python -m datavault transform input.csv output.json --format json
python -m datavault validate data.csv --schema schema.json
```

### 2. **TaskMaster** - CLI Task Management Tool
- **Type**: Python CLI Application
- **Languages**: Python
- **Technologies**: Click, JSON persistence
- **Features**: Task management, priority levels, search, statistics, persistent storage
- **Status**: Production-ready
- **Path**: `projects/02-taskmaster/`

```bash
# Usage
taskmaster add "Task name" --priority high --due "2026-05-15"
taskmaster list --status pending
taskmaster stats
```

### 3. **SentimentAnalyzer** - ML Sentiment Analysis
- **Type**: Machine Learning / NLP
- **Languages**: Python
- **Technologies**: NLTK, TextBlob, Transformers, scikit-learn
- **Features**: Multiple models (VADER, TextBlob), REST API, batch processing, confidence scores
- **Status**: Production-ready
- **Path**: `projects/03-sentiment-analyzer/`

```bash
# Usage
from sentiment_analyzer import SentimentAnalyzer
analyzer = SentimentAnalyzer(model='vader')
result = analyzer.predict("I love this!")
```

---

## 🛠️ Tech Stack Overview

| Category | Technologies |
|----------|---------------|
| **Languages** | Python 3.9+ |
| **Data Processing** | Pandas, Polars, NumPy |
| **Machine Learning** | scikit-learn, PyTorch, Transformers |
| **Web/API** | Click, FastAPI |
| **Testing** | pytest, pytest-cov |
| **Code Quality** | Black, flake8, mypy |
| **Data Engineering** | PySpark, Delta Lake, Parquet |

## 📊 Statistics

- **Total Projects**: 3+
- **Lines of Code**: 2000+
- **Test Coverage**: 80%+
- **Documentation**: 100% of projects

## 🚀 Quick Start

Each project is self-contained with its own README, requirements, and setup:

```bash
# Clone portfolio
git clone https://github.com/shrabedi/portfolio.git
cd portfolio

# Choose a project
cd projects/01-datavault

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Use the tool
python -m datavault --help
```

## 📖 Documentation

Each project includes:
- ✅ Comprehensive README
- ✅ Installation instructions
- ✅ Usage examples (library + CLI)
- ✅ Architecture documentation
- ✅ Full test suite
- ✅ Performance metrics
- ✅ Contributing guidelines

## 🧪 Testing

All projects follow test-driven development:

```bash
cd projects/<project-name>
pytest tests/ -v --cov=<module_name>
```

## 🔧 Code Quality

All projects maintain high standards:
- ✅ Type hints throughout
- ✅ Comprehensive docstrings
- ✅ Black formatting
- ✅ flake8 linting
- ✅ 80%+ test coverage
- ✅ No external service dependencies

## 📈 Project Structure

```
portfolio/
├── projects/
│   ├── 01-datavault/              # Data processing utility
│   │   ├── datavault/             # Main package
│   │   ├── tests/                 # Test suite
│   │   ├── requirements.txt        # Dependencies
│   │   └── README.md              # Project docs
│   ├── 02-taskmaster/             # CLI task manager
│   ├── 03-sentiment-analyzer/     # ML sentiment analysis
│   └── ...more projects
├── README.md                       # This file
└── .gitignore                      # Git ignore rules
```

## 🔄 Continuous Updates

This portfolio is regularly updated with:
- ✨ New projects (weekly)
- 🚀 Performance optimizations
- 📚 Enhanced documentation
- 🧪 Additional test cases
- 🔧 Best practices

## 💡 Learning Highlights

### Data Engineering
- ETL pipeline design
- Data transformation patterns
- Schema validation and drift handling
- Incremental processing

### Python Development
- CLI application design
- API development
- Data structure optimization
- Code organization and modularity

### Machine Learning
- Model evaluation and comparison
- NLP techniques
- Batch and real-time predictions
- Performance optimization

### Software Engineering
- Test-driven development
- Clean code principles
- Documentation standards
- Production-ready code

## 📞 Contact

**Hussain Raza Abedi**
- Email: shrabedi@gmail.com
- LinkedIn: linkedin.com/in/syedhussainrazaabedi
- GitHub: github.com/shrabedi

## 📄 License

All projects are licensed under the MIT License.

---

**Last Updated**: May 5, 2026  
**Total Commits**: Growing daily with new projects and improvements


---
**Portfolio by Hussain Raza Abedi** | [LinkedIn](https://linkedin.com/in/syedhussainrazaabedi)
