# Chart Pattern Recognition Spike on BTC Charts

In this spike, we utilize the "Model Card for YOLOv8s Stock Market Pattern Detection" to recognize chart patterns in BTC trading.

## Features
- **Real-time Detection**: Identifies key chart patterns in the BTC market as they unfold, providing immediate insights for decision-making.
- **Advanced Pattern Recognition**: Utilizes the cutting-edge YOLOv8s technology for accurate and efficient pattern recognition.
- **Seamless Integration**: Designed for easy integration into existing live BTC trading systems, enhancing analysis capabilities without disrupting workflows.
- **Data-Driven Decisions**: Empowers traders with AI-driven insights, enabling more informed and strategic trading decisions.
- **Automated Analysis**: Reduces the need for manual chart analysis, saving time and minimizing human error.
- **Scalability and Flexibility**: Capable of handling large volumes of data and adaptable to various trading strategies and market conditions.

## Warning
- **Model Accuracy**: Please be aware that this model is not 100% accurate. It's based on algorithms that can have inherent limitations and may not capture all market nuances.
- **Test and Entertainment Only**: This model is intended for testing and entertainment purposes only. It should not be used in any serious projects or production environments where financial decisions are made.
- **No Financial Advice**: The outputs of this model are not financial advice. Users should exercise caution and not rely solely on this model for making trading decisions.

Using AI for detecting chart patterns in BTC trading offers significant advantages. It enhances the speed and accuracy of pattern recognition, enables real-time decision making, and automates complex analytical processes, thereby providing traders with a powerful tool to navigate the dynamic cryptocurrency market.


## Prerequisites
1. Python 3.11
2. Git
3. Git LFS (Large File Storage - Make sure you have git-lfs installed https://git-lfs.com)
4. Model Card for YOLOv8s Stock Market Pattern Detection on Live Trading Video Data

## Quick Start

### Windows Specific Notes!
For Windows users:
- Use PowerShell or Git Bash for shell commands.
- Ensure `Docker Desktop for Windows` is set to `Linux` containers.
- Python commands may require using `py` instead of `python` or `python3`.

### Clone the Repo
```commandline
git clone https://github.com/SMARTSHEEP-IO/chart-pattern-recognition-spike.git
```

### Clone the Model
```commandline
git lfs install
git clone https://huggingface.co/foduucom/stockmarket-pattern-detection-yolov8
```

### Install Locally
```commandline
pip3 install virtualenv

python3.11 -m venv chartrectenv
source chartrectenv/bin/activate

pip3 install -r requirements.txt
```

### Run from Terminal (Manually)
```commandline
python3 app.py
```

### Teardown the Virtualenv
```commandline
deactivate
```

## Support and Subscribe to Our YouTube Channels
- Farsi Channel - [Dr. Samizadeh](https://www.youtube.com/@dr.samizadeh)
- English Channel - [Programming in 10 Minutes](https://www.youtube.com/channel/UCK-R2WyThSVk1i5Ac9PLtIA)

## Credits and Acknowledgments
- [Hugging Face](https://huggingface.co/)
- [Model Card for YOLOv8s Stock Market Pattern Detection on Live Trading Video Data](https://huggingface.co/foduucom/stockmarket-pattern-detection-yolov8T)
- The Open Source Community

## References
1. https://huggingface.co/foduucom/stockmarket-pattern-detection-yolov8
2. https://git-lfs.com
3. https://git-scm.com/downloads
4. https://www.python.org/downloads/

## Citation
If you use this spike in your research or project, please cite it as follows:
```bibtex
@article{YOLOv8sBTC,
    title={Chart Pattern Recognition Spike on BTC Charts using YOLOv8s},
    author={Iman Samizadeh},
    journal={GitHub Repository},
    year={2023},
    url={https://github.com/SMARTSHEEP-IO/chart-pattern-recognition-spike}
}
```
