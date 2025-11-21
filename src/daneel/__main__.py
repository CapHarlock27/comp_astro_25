import datetime
import argparse
from daneel.parameters import Parameters
from daneel.detection import *


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        dest = "input_file",
        type = str,
        required = True,
        help = "Input parameter file to pass",
    )

    parser.add_argument(
        "-t",
        "--transit",
        dest = "transit",
        required = False,        
        help = "Plot the light curve of the selected exoplanet",
        action = "store_true",
    )
    

    # parser.add_argument(
    #     "-d",
    #     "--detect",
    #     dest = "detect",
    #     required = False,
    #     help = "Initialise detection algorithms for Exoplanets",
    #     action = "store_true",
    # )

    # parser.add_argument(
    #     "-a",
    #     "--atmosphere",
    #     dest ="complete",
    #     required = False,
    #     help = "Atmospheric Characterisazion from input transmission spectrum",
    #     action = "store_true",
    # )

    args = parser.parse_args()
    
    """Launch Daneel"""
    start = datetime.datetime.now()
    print(f"Daneel starts at {start}")

    input_params = Parameters(args.input_file).params
    
    if args.transit:
        transit = TransitModel(input_params['transit'])
        transit.plot_light_curve()
    elif args.detect:
        pass
    elif args.atmosphere:
        pass

    finish = datetime.datetime.now()
    print(f"Daneel finishes at {finish}")


if __name__ == "__main__":
    main()
