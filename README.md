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
- `-t, -- transit`: Plots the exoplanet transit light curve
- `-d, --detect`: Initialize detection algorithms for exoplanets
- `-a, --atmosphere`: Atmospheric characterization from input transmission spectrum

### Examples

```bash
# Run exoplanet transit light curve plot
daneel -i parameters.yaml -t

# Run exoplanet detection
daneel -i parameters.yaml -d

# Run atmospheric characterization
daneel -i parameters.yaml -a

# Run both detection and atmospheric analysis
daneel -i parameters.yaml -d -a
```

## Input File Format

The input file should be a YAML file containing the necessary parameters for the analysis.\
In this dictionary, consider following the *batman* library parameters format while also adding a key with the name of the selected exoplanet.

### Example

```bash
name: "K2-18_b"                       # name of the exoplanet
t0: 0                                 # time of inferior conjunction
per: 32.939623                        # orbital period
rp: 0.0212                            # planet radius (in units of stellar radii)
a: 30.73                              # semi-major axis (in units of stellar radii)
inc: 89.5785                          # orbital inclination (in degrees)
ecc: 0.2                              # eccentricity
w: 354.3                              # longitude of periastron (in degrees)
u: [0.391617, 0.019183]               # limb darkening coefficients [u1, u2]
limb_darkening_model: "quadratic"     # limb darkening model
```

## License

This project is licensed under the MIT License.

## Author

Tiziano Zingales (tiziano.zingales@unipd.it)
