# Daneel

A practical example to detect and characterize exoplanets.

The full documentation is at https://tiziano1590.github.io/comp_astro_25/index.html

## Installation

### Prerequisites

- Python >= 3.10

### Install from source

```bash
git clone https://github.com/tiziano1590/comp_astro_25.git
cd comp_astro_25
pip install .
```

### Development installation

```bash
git clone https://github.com/tiziano1590/comp_astro_25.git
cd comp_astro_25
pip install -e .
```

## Usage

After installation, you can run daneel from the command line:

```bash
daneel -i <input_file> [options]
```

### Command-line options

- `-i, --input`: Input parameter file (required)
- `-t, -- transit`: Plots the exoplanet light curve
- `-d, --detect`: Initialize detection algorithms for exoplanets
- `-a, --atmosphere`: Atmospheric characterization from input transmission spectrum

### Examples

```bash
# Run plotting of exoplanet light curve
daneel -i parameters.yaml -t

# Run exoplanet detection
daneel -i parameters.yaml -d

# Run atmospheric characterization
daneel -i parameters.yaml -a

# Run both detection and atmospheric analysis
daneel -i parameters.yaml -d -a
```

## Input File Format

The input file should be a YAML file containing the necessary parameters for the analysis.

## License

This project is licensed under the MIT License.

## Author

Tiziano Zingales (tiziano.zingales@unipd.it)
