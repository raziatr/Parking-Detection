# AOL Computer Vision Parking Detection

A computer vision project for detecting parking space occupancy using OpenCV and image processing techniques. This application analyzes parking lot footage and determines whether parking spots are occupied or available in real-time.

## Features

* Real-time parking space detection
* Occupied vs empty parking classification
* Bounding box visualization
* OpenCV-based image processing
* Video stream analysis
* Lightweight and simple implementation

## Tech Stack

* Python
* OpenCV
* NumPy
* Pickle

## Project Structure

```bash
aol_comvis/
│
├── image_classifier.py      # Main parking detection script
├── CarParkPos              # Saved parking slot coordinates
├── carPark.mp4             # Input parking video
├── README.md
└── ...
```

## How It Works

The system works by:

1. Reading parking lot video footage
2. Defining parking slot coordinates
3. Cropping each parking area
4. Applying image preprocessing:
5. Counting non-zero pixels inside each slot
6. Determining whether the slot is occupied or empty based on a threshold

## Installation

Clone the repository:

```bash
git clone https://github.com/ilhamptr/aol_comvis.git
cd aol_comvis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main detection script:

```bash
python app.py
```

Controls:

* Press `q` to quit the application

## Parking Slot Setup

Parking positions are stored using Python Pickle in the `CarParkPos` file.

You can create or modify parking slot positions manually or using a helper script if available.

## Example Workflow

```text
Video Input
   ↓
Frame Extraction
   ↓
Image Preprocessing
   ↓
Pixel Analysis
   ↓
Parking Status Classification
   ↓
Visualization Output
```

## Future Improvements

* Better robustness for lighting/weather conditions
* Dynamic thresholding
* Web dashboard integration
* Parking analytics
* License plate recognition

## Use Cases

* Smart parking systems
* Campus parking management
* Mall parking monitoring
* IoT smart city applications
* Traffic management research
  
## License

This project is for educational and research purposes.
